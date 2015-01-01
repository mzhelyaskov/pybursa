# -*- coding: utf-8 -*-

from courses.models import Course
from django import forms
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('venue',)


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    context_object_name = 'course'
    success_url = '/courses/'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Создание нового курса"
        return context


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    context_object_name = 'course'
    success_url = '/courses/'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Редактирование курса"
        return context


class CourseDeleteView(DeleteView):
    model = Course
    context_object_name = 'course'
    success_url = '/courses/'


class CoursesListView(ListView):
    model = Course
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'