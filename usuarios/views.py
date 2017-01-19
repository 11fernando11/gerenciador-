from django.shortcuts import render, redirect
from usuarios.forms import UserModelForm
from django.http import HttpResponse

def index(request):
	return HttpResponse("OK")

def cadastro(request):
	form = UserModelForm(request.POST or None)
	context = {'form':form}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/cadastro')
	return render(request,'usuarios/cadastro.html', context)