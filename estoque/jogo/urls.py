from django.urls import path
from estoque.jogo import views as v


app_name = 'jogo'


urlpatterns = [
	path('', v.jogo_list, name='jogo_list'),
	path('<int:pk>/', v.jogo_detail, name='jogo_detail'),
	path('add/', v.JogoCreate.as_view(), name='jogo_add'),
	path('<int:pk>/edit/', v.JogoUpdate.as_view(), name='jogo_edit'),
	path('<int:pk>/json/', v.jogo_json, name='jogo_json'),
]