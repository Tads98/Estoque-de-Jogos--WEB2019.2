import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "estoque.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from estoque.jogo.models import Jogo


class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class JogoClass:

    @staticmethod
    def criar_jogos(jogos):
        Jogo.objects.all().delete()
        aux = []
        for jogo in jogos:
            data = dict(
                jogo=jogo,
                importado=choice((True, False)),
                ncm=Utils.gen_digits(8),
                preco=random() * randint(100, 500),
                estoque=randint(10, 200),
            )
            obj = Jogo(**data)
            aux.append(obj)
        Jogo.objects.bulk_create(aux)


jogos = (
	'Days Gone',
	'Call Of Duty: Modern Warfare',
	'God Of War (2018)',
	'Marvel Spider-Man',
	'Call Of Duty: Black Ops 4',
	'Shadow Of The Tomb Raider',
	'Detroit Become Human',
	'battlefield V',
	'Horizon Zero Dawn',
	'Cyberpunk 2077',
	'The Last Of Us Part II',
	'Dying Light 2',
	'RainbowSix Quarantine',
)

tic = timeit.default_timer()

JogoClass.criar_jogos(jogos)


toc = timeit.default_timer()

print('Tempo:', toc - tic)