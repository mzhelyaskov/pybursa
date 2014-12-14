from django.shortcuts import get_object_or_404, render
from courses.models import Course


def courses_list(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/courses_list.html', context)


def course_item(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    context = {'course': course}
    return render(request, 'courses/course_item.html', context)