from django.contrib import admin
from .models import Armazenamento, ArmazenamentoItens

# Register your models here.

class ArmazenamentoItensInline(admin.TabularInline):
	model = ArmazenamentoItens
	extra = 0


@admin.register(Armazenamento)
class ArmazenamentoAdmin(admin.ModelAdmin):
	inlines = (ArmazenamentoItensInline,)
	list_display = ('__str__', 'nf', 'funcionario',)
	search_fields = ('nf',)
	list_filter = ('funcionario',)
	date_hierarchy = 'created'