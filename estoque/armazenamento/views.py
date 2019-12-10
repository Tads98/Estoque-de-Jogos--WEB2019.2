from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from estoque.jogo.models import Jogo
from .models import Armazenamento, ArmazenamentoItens
from .forms import ArmazenamentoForm, ArmazenamentoItensForm

# Create your views here.

def armazenamento_entrada_list(request):
	template_name = 'armazenamento_entrada_list.html'
	objects = Armazenamento.objects.filter(movimento='e')
	context = {'object_list': objects}
	return render(request, template_name, context)

def armazenamento_entrada_detail(request, pk):
	template_name = 'armazenamento_entrada_detail.html'
	obj = Armazenamento.objects.get(pk=pk)
	context = {'object': obj}
	return render(request, template_name, context)

"""
def dar_baixa_armazenamento(request):
	# Pega os jogos a partir da instancia do formulario (Armazenamento)
	jogos = form.armazenamento.all()
	for item in jogos:
		jogo = Jogo.objects.get(pk=item.jogo.pk)
		jogo.armazenamento = item.saldo
		jogo.save()
	print('Armazenamento atualizado com sucesso. ')
"""

'''
Se aprofundar nos conceitos de entrada_add para compreender
melhor a lógica da def armazenamento_entrada_add(Ler artigo)
'''
def armazenamento_entrada_add(request):
	template_name = 'armazenamento_entrada_form.html'
	armazenamento_form = Armazenamento()
	item_armazenamento_formset = inlineformset_factory(
		Armazenamento,
		ArmazenamentoItens,
		form=ArmazenamentoItensForm,
		extra=0,
		min_num=1,
		validate_min=True,
	)
	if request.method == 'POST':
		form = ArmazenamentoForm(request.POST, instance=armazenamento_form, prefix='main')
		formset = item_armazenamento_formset(
			request.POST,
			instance=armazenamento_form,
			prefix='armazenamento'
		)
		if form.is_valid() and formset.is_valid():
			form = form.save()
			formset.save()
			#dar_baixa_armazenamento(form)
			url = 'armazenamento:armazenamento_entrada_detail'
			return HttpResponseRedirect(resolve_url(url, form.pk))
	else:
		form = ArmazenamentoForm(instance=armazenamento_form, prefix='main')
		formset = item_armazenamento_formset(instance=armazenamento_form, prefix='armazenamento')
	
	context = {'form': form, 'formset': formset}		
	return render(request, template_name, context)
