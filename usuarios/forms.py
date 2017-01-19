# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class UserModelForm(forms.ModelForm):
	User._meta.get_field('email').blank=False
	User._meta.get_field('first_name').blank=False
	User._meta.get_field('last_name').blank=False
	User._meta.get_field('username').blank=False

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255,'placeholder': 'First name'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255,'placeholder': 'Last name'}),	
			'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255,'placeholder': 'email'}),
			'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255,'placeholder': 'username'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 255,'placeholder': 'password'}),
		}

		error_messages = {
			'first_name' : {
				'required' : 'Este campo é obrigatório'
			},
			'last_name' : {
				'required' : 'Este campo é obrigatório'
			},
			'email' : {
				'required' : 'Este campo é obrigatório'
			},
			'username' : {
				'required' : 'Este campo é obrigatório'
			},
			'password' : {
				'required' : 'Este campo é obrigatório'
			},
		}
	def save(self,commit=True):
		user = super(UserModelForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user