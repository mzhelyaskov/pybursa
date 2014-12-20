# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, redirect
from students.models import Student
from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(max_length=60)
    surname = forms.CharField(max_length=60)
    birth_date = forms.DateField()
    email = forms.EmailField()
    phone = forms.CharField(max_length=60)
    standard = 'SD'
    gold = 'GD'
    vip = 'VP'
    package_view = (
        (standard, 'Standard'),
        (gold, 'Gold'),
        (vip, 'VIP'),
    )
    package = forms.ChoiceField(widget=forms.RadioSelect, choices=package_view)


def students_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/students_list.html', context)


def student_item(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {'student': student}
    return render(request, 'students/student_item.html', context)


def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student.name = form.cleaned_data['name']
            student.surname = form.cleaned_data['surname']
            student.birth_date = form.cleaned_data['birth_date']
            student.email = form.cleaned_data['email']
            student.phone = form.cleaned_data['phone']
            student.package = form.cleaned_data['package']
            student.save()
            return redirect('student-edit', student_id=student.id)
    else:
        context = {
            'name': student.name,
            'surname': student.surname,
            'birth_date': student.birth_date,
            'email': student.email,
            'phone': student.phone,
            'package': student.package
        }
        form = StudentForm(initial=context)
    return render(request, 'students/student_edit.html', {'form': form})