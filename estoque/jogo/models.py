from django.db import models
from django.urls import reverse_lazy
# Create your models here.

class Jogo(models.Model):
	 importado = models.BooleanField(default=False)
	 ncm = models.CharField('NCM', max_length=8)
	 jogo = models.CharField(max_length=100, unique=True)
	 preco = models.DecimalField('preço', max_digits=7, decimal_places=2)
	 estoque = models.IntegerField('estoque atual')
	 estoque_minimo = models.PositiveIntegerField('estoque_minimo', default=0)

class Meta:
	ordering = ('jogo',)


	def __str__(self):
		return self.jogo

	def get_absolute_url(self):
		return reverse_lazy('jogo:jogo_detail', kwargs={'pk': self.pk})

	def to_dict_json(self):
		return {
			'pk': self.pk,
			'jogo': self.jogo,
			'armazenamento': self.armazenamento,
		}