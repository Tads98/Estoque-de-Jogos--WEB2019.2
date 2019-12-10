from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from estoque.core.models import TimeStampedModel
from estoque.jogo.models import Jogo

# Create your models here.

MOVIMENTO = (
	('e', 'entrada'),
	('s','saida'),
)

class Armazenamento(TimeStampedModel):
	funcionario = models.ForeignKey(User, on_delete = models.CASCADE)
	nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
	movimento = models.CharField(max_length=1, choices=MOVIMENTO)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%y'))

	def get_absolute_url(self):
		return reverse_lazy('armazenamento:armazenamento_entrada_detail', kwargs={'pk': self.pk})

	def nf_formated(self):
		return str(self.nf).zfill(3)


class ArmazenamentoItens(models.Model):
	armazenamento = models.ForeignKey(Armazenamento,
	 on_delete=models.CASCADE, 
	 related_name='armazenamentos'
	 )
	jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
	quantidade = models.PositiveIntegerField()
	saldo = models.PositiveIntegerField()

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {} - {}'.format(self.pk, self.armazenamento.pk, self.jogo)


 