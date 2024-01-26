def enrolled_transform(e):
    subject=dict()
    subject['id']=e.subject.id
    subject['name']=e.subject.name
    subject['subject']={'id':e.subject.teacher.id,
            'first_name':e.subject.teacher.first_name,
            'last_name':e.subject.teacher.last_name,
            "email":e.subject.teacher.email 
            }
    
    student={'id':e.student.id,
            'first_name':e.student.first_name,
            'last_name':e.student.last_name,
            "email":e.student.email 
            }
    return {"subject":subject,"student":student}