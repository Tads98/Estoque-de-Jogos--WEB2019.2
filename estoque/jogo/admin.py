from django.contrib import admin
from .models import Jogo

# Register your models here.
@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
	list_display = (
		'__str__',
		'importado',
		'ncm',
		'preco',
		'estoque',
		'estoque_minimo',
	)
	search_fields = ('jogo',)
	list_filter = ('importado',)