from django.urls import path
from estoque.armazenamento import views as v


app_name = 'armazenamento'


urlpatterns = [
	path('', v.armazenamento_entrada_list, name='armazenamento_entrada_list'),
	path('<int:pk>/', v.armazenamento_entrada_detail, name='armazenamento_entrada_detail'),
	path('add/', v.armazenamento_entrada_add, name='armazenamento_entrada_add'),
]