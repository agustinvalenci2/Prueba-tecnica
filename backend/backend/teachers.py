from .genericview import *

def teacher_transform(s):
    response={'id':s.id,
            'first_name':s.first_name,
            'last_name':s.last_name,
            "email":s.email 
            }
    return response

def list_teachers(request):
    teachers=Teacher.objects.all()
    status=200 if teachers.count() else 204
    serialized={"response":[
        teacher_transform(s)
         for s in teachers
    ]}
    return JsonResponse(serialized,status=status)

@csrf_exempt
def add_teacher(request):
    if request.method == "POST":
        body=json.loads(request.body)
        print(body)
        try:
            teachers=Teacher(**body)
            status=200
            response="User Added"
            teachers.save()
        except Teacher.DoesNotExist:
            response="Error user can't add"
            status=204
        finally:
            return JsonResponse({'response':response},status=status)
        


def get_teacher(request,id):
    if request.method == "GET":
        id=int(id)
        try:
            s=Teacher.objects.get(id=id)
            status=200
            response=teacher_transform(s)
        except Teacher.DoesNotExist:
            response="Error user does not exist"
            status=204
        finally:
            return JsonResponse({'response':response},status=status)