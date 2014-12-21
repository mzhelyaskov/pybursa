from django.shortcuts import get_object_or_404, render, redirect
from courses.models import Course
from django import forms


def courses_list(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/courses_list.html', context)


def course_item(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    context = {'course': course}
    return render(request, 'courses/course_item.html', context)


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'programming_len', 'description',
                  'teacher', 'assistant', 'start_date', 'end_date', 'slug')


def course_edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect('result-message')
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/course_edit.html', {'form': form})


def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('result-message')
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/course_delete.html', {'form': form})


def course_create(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result-message')
    else:
        form = CourseModelForm()
    return render(request, 'courses/course_create.html', {'form': form})