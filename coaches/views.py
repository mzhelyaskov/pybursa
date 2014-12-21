from django.shortcuts import get_object_or_404, render, redirect
from coaches.models import Coach
from django import forms


def coaches_list(request):
    coaches = Coach.objects.all()
    context = {'coaches': coaches}
    return render(request, 'coaches/coaches_list.html', context)


def coach_item(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    print '\n'.join(dir(coach.photo))
    context = {'coach': coach}
    return render(request, 'coaches/coach_item.html', context)


class CoachModelForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ('name', 'surname', 'user', 'birth_date', 'email', 'phone')


def coach_edit(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    if request.method == 'POST':
        form = CoachModelForm(request.POST, instance=coach)
        if form.is_valid():
            coach = form.save()
            return redirect('result-message')
    else:
        form = CoachModelForm(instance=coach)
    return render(request, 'coaches/coach_edit.html', {'form': form})


def coach_delete(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    if request.method == 'POST':
        coach.delete()
        return redirect('result-message')
    else:
        form = CoachModelForm(instance=coach)
    return render(request, 'coaches/coach_delete.html', {'form': form})


def coach_create(request):
    if request.method == 'POST':
        form = CoachModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result-message')
    else:
        form = CoachModelForm()
    return render(request, 'coaches/coach_create.html', {'form': form})