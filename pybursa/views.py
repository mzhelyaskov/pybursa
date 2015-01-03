# -*- coding: utf-8 -*-

from django import forms
from django.views.generic import FormView
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from coaches.models import Coach
from students.models import Student


class MailForm(forms.Form):
    theme = forms.CharField(label=_(u'Тема'))
    email = forms.EmailField(label='Email')
    coach = forms.ModelChoiceField(queryset=Coach.objects.all(),
                                   widget=forms.Select,
                                   empty_label=None)
    student = forms.ModelChoiceField(queryset=Student.objects.all(),
                                     widget=forms.Select,
                                     empty_label=None)
    message_body = forms.CharField(label=_(u'Тело письма'),
                                   widget=forms.Textarea())


class MailView(FormView):
    form_class = MailForm
    template_name = 'mail'

    def form_valid(self, form):
        theme = form.cleaned_data['theme']
        coach = form.cleaned_data['coach']
        student = form.cleaned_data['student']
        message_body = form.cleaned_data['message_body']

        mail_body = render_to_string('email/mail_text.html',
                                     {'coach': coach,
                                      'student': student,
                                      'body': message_body})

        send_mail(theme, mail_body, self.request.GET.get('email-from'),
                  [coach.email], fail_silently=False)
        messages.success(self.request, 'Your message successfully sent')
        return redirect('mail')

    def get_context_data(self, **kwargs):
        context = super(MailView, self).get_context_data(**kwargs)
        context['title'] = _(u"Форма отправки почты преподавателю")
        return context