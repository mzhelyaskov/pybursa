from django.shortcuts import render
from students.models import Student


def students_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/students_list.html', context)


def student_item(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {'student': student}
    return render(request, 'students/student_item.html', context)