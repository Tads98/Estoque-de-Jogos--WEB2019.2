from django.urls import path
from estoque.armazenamento import views as v


app_name = 'armazenamento'


urlpatterns = [
	path('', v.armazenamento_entrada_list, name='armazenamento_entrada_list'),
	path('<int:pk>/', v.armazenamento_entrada_detail, name='armazenamento_entrada_detail'),
	path('add/', v.armazenamento_entrada_add, name='armazenamento_entrada_add'),
	path('saida/', v.armazenamento_saida_list, name='armazenamento_saida_list'),
	path('saida/<int:pk>/', v.armazenamento_saida_detail, name='armazenamento_saida_detail'),
	path('saida/add/', v.armazenamento_saida_add, name='armazenamento_saida_add'),
]