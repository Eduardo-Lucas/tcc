from django.urls import path

from apps.pessoas.views import *

urlpatterns = [
    path('list', PessoaListView.as_view(), name='pessoa_list'),
    path('create', PessoaCreateView.as_view(), name='pessoa_create'),
    path('detail/<int:pk>', PessoaDetailView.as_view(), name='pessoa_detail'),
    path('update/<int:pk>', PessoaUpdateView.as_view(), name='pessoa_update'),
    path('delete/<int:pk>', PessoaDeleteView.as_view(), name='pessoa_delete'),

]
