from .genericview import *
from django.db.models import Value, CharField
from django.db.models.functions import Concat
def student_transform(s):
    response={'id':s.id,
            'first_name':s.first_name,
            'last_name':s.last_name,
            "email":s.email 
            }
    return response

def list_students(request):
    students=Student.objects.all()
    status=200 if students.count() else 204
    serialized={"response":[
        student_transform(s)
         for s in students
    ]}
    return JsonResponse(serialized,status=status)

@csrf_exempt
def add_student(request):
    if request.method == "POST":
        body = json.loads(request.body)
        try:
            student = Student.objects.create(**body)
            response = "User Added"
            status = 200
        except Exception as e:
            response = f"Error: {str(e)}"
            status = 400

        return JsonResponse({'response': response}, status=status)
        


def get_student(request,id):
    if request.method == "GET":
        id=int(id)
        try:
            s=Student.objects.get(id=id)
            status=200
            response=student_transform(s)
        except Student.DoesNotExist:
            response="Error user does not exist"
            status=204
        finally:
            return JsonResponse({'responde':response},status=status)
        




@csrf_exempt
def search_students_by_name(request):
    if request.method == "GET":
        # Obtener el parámetro 'name' de la consulta (query parameter)
        student_name = request.GET.get('name', None)
        print(student_name)
        if student_name is not None:
            # Realizar la búsqueda de estudiantes por nombre
            students = (
                Student.objects
                .annotate(full_name=Concat('first_name', Value(' '), 'last_name', output_field=CharField()))
                .filter(full_name__icontains=student_name)
            )

            # Verificar si se encontraron resultados
            if students.exists():
                serialized_students = [
                    student_transform(student)
                    for student in students
                ]
                return JsonResponse({'response': serialized_students}, status=200)
            else:
                return JsonResponse({'message': 'No se encontraron estudiantes con ese nombre'}, status=204)
        else:
            return JsonResponse({'message': 'El parámetro "name" es requerido'}, status=400)

    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)