from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Subject,Enrolled,Assistant
from datetime import date
def subject_transform(subject):
    hours=[{"day":h.day,"hour":h.hour} for h in subject.hours.all()]
    return {
        'id': subject.id,
        'name': subject.name,
         'hours':hours,
        'teacher': {
            'id': subject.teacher.id,
            'first_name': subject.teacher.first_name,
            'last_name': subject.teacher.last_name,
            'email': subject.teacher.email,
        }
    }

@csrf_exempt
def list_subjects(request,student_id):
    en=Enrolled.objects.filter(student_id=student_id,period=date.today().year)
    subjects = Subject.objects.exclude(enrollments__in=en)
    serialized_subjects = [subject_transform(subject) for subject in subjects]
    status = 200 if subjects else 204
    return JsonResponse({'response': serialized_subjects}, status=status)

@csrf_exempt
def add_subject(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            subject = Subject.objects.create(**data)
            response = {'message': 'Subject added successfully', 'subject': subject_transform(subject)}
            return JsonResponse(response, status=200)
        except Exception as e:
            response = {'message': f'Error: {str(e)}'}
            return JsonResponse(response, status=400)

def get_subject(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        response = {'response': subject_transform(subject)}
        return JsonResponse(response, status=200)
    except Subject.DoesNotExist:
        response = {'message': 'Subject not found'}
        return JsonResponse(response, status=404)

def get_enrolled(request, student_id):

    subjects = Subject.objects.filter(enrollments__student_id=student_id)
    serialized_subjects = [subject_transform(subject) for subject in subjects]
    status = 200 if subjects else 204
    return JsonResponse({'response': serialized_subjects}, status=status)

def get_by_teacher(request, teacher_id):
    subjects = Subject.objects.filter(teacher_id=teacher_id)
    serialized_subjects = [subject_transform(subject) for subject in subjects]
    status = 200 if subjects else 204
    return JsonResponse({'response': serialized_subjects}, status=status)



@csrf_exempt
def enroll(request):
    if request.method == "POST":
        try:

            data = json.loads(request.body)
            data['period']=date.today().year
            print(data)
            en = Enrolled.objects.create(**data)
            response = {'message': 'Subject added successfully', 'subject': subject_transform(en.subject)}
            return JsonResponse(response, status=200)
        except Exception as e:
            response = {'message': f'Error: {str(e)}'}
            return JsonResponse(response, status=400)

def assistant_serialized(assistance):
    ans=dict()
    ans['date']=assistance.date
    ans['day']=assistance.hour.day
    ans['assisted']=assistance.assisted
    return ans   

def get_assistant(request,student_id,subject_id):
    try:
        en=Enrolled.objects.get(student_id=student_id,
                                subject_id=subject_id,
                                period=date.today().year)
        assistants= Assistant.objects.filter(enrolled=en)
        status=200 if assistants.count() else 204
        response=dict()
        if assistants.count()!=0:
            response['percent']=round(100*assistants.filter(assisted=True).count()/assistants.count())
        else:
            response['percent']='N/A'
        response['assist_list']=[assistant_serialized(assistant) for assistant in assistants]
        return JsonResponse(response,status=status) 
    except Enrolled.DoesNotExist:
        return JsonResponse({"message":"this student is not enrolled in this subject"},status=404)
