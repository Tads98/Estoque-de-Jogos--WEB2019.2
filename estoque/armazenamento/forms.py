from django import forms
from .models import Armazenamento, ArmazenamentoItens


class ArmazenamentoForm(forms.ModelForm):

   class Meta: 
   	  model = Armazenamento
   	  fields = '__all__'


class ArmazenamentoItensForm(forms.ModelForm):

   class Meta: 
   	  model = ArmazenamentoItens
   	  fields = '__all__'