# -*- coding: utf8 -*-
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_template

class ContactVacinou(forms.Form):

	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='E-mail')

	def send_mail(self):
	    subject = 'Contato'
	    context = {
	        'name': self.cleaned_data['name'],
	        'email': self.cleaned_data['email'],
	    }
	    template_name = 'contact_email.html'
	    send_mail_template(
	        subject, template_name, context, [settings.CONTACT_EMAIL]
	    )