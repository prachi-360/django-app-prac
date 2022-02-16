from django.shortcuts import render
from .models import Student

def studentData(request):
    students = Student.objects.all().values()  #it will return dictionary
    # students = Student.objects.all().values_list() #it will return list of tuple

    students1 = Student.objects.filter(student_name__startswith='a').values()
    # students2 = Student.objects.filter(student_name__constraints='r').values()

    #lookup methods...
    # students3 = Student.objects.filter(role_id__gt=1).values()


    print(students[0].get('id'))
    print(students[0])
    studentlist = []
    for i in students1[0].values():
        studentlist.append(i)
   
    print("Student List..",studentlist)

    # for student in students:
    #     print(list(student[0]))
    # print(students.keys(),end=''))
    # print(students.views)
    context = {
        'students':studentlist
    }
    return render(request,'orm/student.html',context)
