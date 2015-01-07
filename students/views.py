# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, redirect
from students.models import Student
from django import forms

import logging

logger = logging.getLogger(__name__)


class StudentForm(forms.Form):
    standard = 'SD'
    gold = 'GD'
    vip = 'VP'
    package_view = (
        (standard, 'Standard'),
        (gold, 'Gold'),
        (vip, 'VIP'),
    )
    name = forms.CharField(label=u"Имя:",
                           max_length=60,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': u"Введите имя..."
                               }
                           ))
    surname = forms.CharField(label=u"Фамилия:",
                              max_length=60,
                              widget=forms.TextInput(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': u"Введите фамилию..."
                                  }
                              ))
    birth_date = forms.DateField(label=u"Дата рождения:",
                                 widget=forms.DateInput(
                                     attrs={
                                         'class': 'form-control',
                                         'placeholder': u'Введите дату рож-я'
                                     }
                                 ))
    email = forms.EmailField(label=u"Email:",
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': u'Введите Email...'
                                 }
                             ))
    phone = forms.CharField(label=u"Телефон:",
                            max_length=60,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': u'Введите телефон...'
                                }
                            ))
    package = forms.ChoiceField(label=u"Пакет:",
                                widget=forms.RadioSelect,
                                choices=package_view,
                                error_messages={
                                    'required': u'Пакет указан некорректно.'
                                },
                                help_text=u"Укажите вид обучающего пакета... ")


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
            logger.info(
                u'Изменен студент %s %s.' % (student.name, student.surname)
            )
            return redirect('students:student-detail', student.id)
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


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        logger.info(u'Удален студент %s %s.' % (student.name, student.surname))
        return redirect('students:index')
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
    return render(request, 'students/student_delete.html', {'form': form})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = Student(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                birth_date=form.cleaned_data['birth_date'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                package=form.cleaned_data['package']
            )
            student.save()
            logger.info(
                u'Создан студент %s %s.' % (student.name, student.surname)
            )
            return redirect('students:index')
    else:
        form = StudentForm()
    return render(request, 'students/student_create.html', {'form': form})