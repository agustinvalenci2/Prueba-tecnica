from .genericview import *


def hour_transform(s):
    response={'id':s.id,
            'day':s.day,
            'hour':s.hour,
            "subject_id":s.subject_id 
            }
    return response

def list_hours(request,subject_id):
    subject_id=int(subject_id)
    hours=Hours.objects.filter(subject_id=subject_id)
    status=200 if hours.count() else 204
    serialized={"response":[
        hour_transform(s)
         for s in hours
    ]}
    return JsonResponse(serialized,status=status)

@csrf_exempt
def add_hour(request):
    if request.method == "POST":
        body=json.loads(request.body)
        print(body)
        try:
            teachers=Hours(**body)
            status=200
            response="Hour Added"
            teachers.save()
        except Teacher.DoesNotExist:
            response="Error hour can't add"
            status=204
        finally:
            return JsonResponse({'responde':response},status=status)
        


def get_hour(request,id):
    if request.method == "GET":
        id=int(id)
        try:
            s=Hours.objects.get(id=id)
            status=200
            response=hour_transform(s)
        except Teacher.DoesNotExist:
            response="Error hour does not exist"
            status=204
        finally:
            return JsonResponse({'responde':response},status=status)