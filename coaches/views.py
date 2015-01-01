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