# -*- coding: utf-8 -*-

from django import forms
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from coaches.models import Coach


class CoachModelForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ('name', 'surname', 'user', 'birth_date', 'email', 'phone')


class CoachCreateView(CreateView):
    model = Coach
    form_class = CoachModelForm
    context_object_name = 'coach'
    success_url = '/coaches/'

    def get_context_data(self, **kwargs):
        context = super(CoachCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Создание нового преподавателя"
        return context


class CoachUpdateView(UpdateView):
    model = Coach
    form_class = CoachModelForm
    context_object_name = 'coach'
    success_url = '/coaches/'

    def get_context_data(self, **kwargs):
        context = super(CoachUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Редактирование реквизитов преподавателя"
        return context


class CoachDeleteView(DeleteView):
    model = Coach
    context_object_name = 'coach'
    success_url = '/coaches/'


class CoachesListView(ListView):
    model = Coach
    context_object_name = 'coaches'


class CoachDetailView(DetailView):
    model = Coach
    context_object_name = 'coach'





# def coaches_list(request):
#     coaches = Coach.objects.all()
#     context = {'coaches': coaches}
#     return render(request, 'coaches/coach_list.html', context)
#
#
# def coach_item(request, coach_id):
#     coach = get_object_or_404(Coach, id=coach_id)
#     print '\n'.join(dir(coach.photo))
#     context = {'coach': coach}
#     return render(request, 'coaches/coach_detail.html', context)
#
#
# class CoachModelForm(forms.ModelForm):
#     class Meta:
#         model = Coach
#         fields = ('name', 'surname', 'user', 'birth_date', 'email', 'phone')
#
#
# def coach_edit(request, coach_id):
#     coach = get_object_or_404(Coach, id=coach_id)
#     if request.method == 'POST':
#         form = CoachModelForm(request.POST, instance=coach)
#         if form.is_valid():
#             coach = form.save()
#             return redirect('result-message')
#     else:
#         form = CoachModelForm(instance=coach)
#     return render(request, 'coaches/coach_edit.html', {'form': form})
#
#
# def coach_delete(request, coach_id):
#     coach = get_object_or_404(Coach, id=coach_id)
#     if request.method == 'POST':
#         coach.delete()
#         return redirect('result-message')
#     else:
#         form = CoachModelForm(instance=coach)
#     return render(request, 'coaches/coach_delete.html', {'form': form})
#
#
# def coach_create(request):
#     if request.method == 'POST':
#         form = CoachModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('result-message')
#     else:
#         form = CoachModelForm()
#     return render(request, 'coaches/coach_create.html', {'form': form})