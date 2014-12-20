from django.shortcuts import get_object_or_404, render
from coaches.models import Coach


def coaches_list(request):
    coaches = Coach.objects.all()
    context = {'coaches': coaches}
    return render(request, 'coaches/coaches_list.html', context)


def coach_item(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    print '\n'.join(dir(coach.photo))
    context = {'coach': coach}
    return render(request, 'coaches/coach_item.html', context)