from django.urls import path

from apps.treinamentos.views import create_treinamento

app_name = 'treinamentos'

urlpatterns = [
    # path('list', PerguntaListView.as_view(),  name='pergunta_list'),
    path('create/<int:pessoa_id>', create_treinamento, name='treinamento_create'),
    # path('detail/<int:pk>', PerguntaDetailView.as_view(),  name='pergunta_detail'),
    # path('update/<int:pk>', TreinamentoUpdateView.as_view(),  name='treinamento_update'),
    # path('delete/<int:pk>', PerguntaDeleteView.as_view(),  name='pergunta_delete'),

]
