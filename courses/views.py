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







# def courses_list(request):
#     courses = Course.objects.all()
#     context = {'courses': courses}
#     return render(request, 'courses/course_list.html', context)
#
#
# def course_item(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     context = {'course': course}
#     return render(request, 'courses/course_detail.html', context)
#
#
# def course_edit(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     if request.method == 'POST':
#         form = CourseModelForm(request.POST, instance=course)
#         if form.is_valid():
#             course = form.save()
#             return redirect('result-message')
#     else:
#         form = CourseModelForm(instance=course)
#     return render(request, 'courses/course_edit.html', {'form': form})
#
#
# def course_delete(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     if request.method == 'POST':
#         course.delete()
#         return redirect('result-message')
#     else:
#         form = CourseModelForm(instance=course)
#     return render(request, 'courses/course_delete.html', {'form': form})
#
#
# def course_create(request):
#     if request.method == 'POST':
#         form = CourseModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('result-message')
#     else:
#         form = CourseModelForm()
#     return render(request, 'courses/course_create.html', {'form': form})