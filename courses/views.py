from django.shortcuts import render
from courses.models import Course


def courses_list(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/courses_list.html', context)


def course_item(request, student_id):
    course = Course.objects.get(id=student_id)
    context = {'course': course}
    return render(request, 'courses/course_item.html', context)