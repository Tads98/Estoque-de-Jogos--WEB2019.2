from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Jogo
from .forms import JogoForm


def jogo_list(request):
	template_name = 'jogo_list.html'
	objects = Jogo.objects.all()
	context = {'object_list': objects}
	return render(request, template_name, context)


def jogo_detail(request, pk):
	template_name = 'jogo_detail.html'
	obj = Jogo.objects.get(pk=pk)
	context = {'object': obj}
	return render(request, template_name, context)


def jogo_add(request):
	template_name = 'jogo_form.html'
	return render(request, template_name)


class JogoCreate(CreateView):
	model = Jogo
	template_name = 'jogo_form.html'
	form_class = JogoForm

class JogoUpdate(UpdateView):
	model = Jogo
	template_name = 'jogo_form.html'
	form_class = JogoForm

def jogo_json(request, pk):
	'''Retorna o jogo id e armazenamento '''
	jogo = Jogo.objects.filter(pk=pk)
	data = [item.to_dict_json() for item in jogo]
	return JsonResponse({'data' : data})