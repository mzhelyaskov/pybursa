from django.shortcuts import render
from coaches.models import Coach


def coaches_list(request):
    coaches = Coach.objects.all()
    context = {'coaches': coaches}
    return render(request, 'coaches/coaches_list.html', context)


def coach_item(request, student_id):
    coach = Coach.objects.get(id=student_id)
    context = {'coach': coach}
    return render(request, 'coaches/coach_item.html', context)