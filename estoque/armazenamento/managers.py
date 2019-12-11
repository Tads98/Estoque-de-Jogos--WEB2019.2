from django.db import models

class ArmazenamentoEntradaManager(models.Manager):

	def get_queryset(self):
		return super(ArmazenamentoEntradaManager, self).get_queryset().filter(movimento='e')


class ArmazenamentoSaidaManager(models.Manager):

	def get_queryset(self):
		return super(ArmazenamentoSaidaManager, self).get_queryset().filter(movimento='s')
