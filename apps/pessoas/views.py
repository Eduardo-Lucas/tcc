from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.pessoas.models import Pessoa


class PessoaListView(ListView):
    model = Pessoa
    template_name = 'pessoas/pessoa_list.html'
    
    def get_queryset(self):
        valor = self.request.GET.get('q')
        if valor:
            object_list = self.model.objects.filter(
                Q(nome__icontains=valor) |
                Q(data_de_nascimento__icontains=valor) |
                Q(sexo__icontains=valor)
            )
        else:
            object_list = self.model.objects.all()

        paginator = Paginator(object_list, 6)  # Show n produtos per page

        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)
        
        return queryset


class PessoaCreateView(SuccessMessageMixin, CreateView):
    model = Pessoa
    fields = ['nome', 'data_de_nascimento', 'sexo', 'imagem', ]
    success_message = 'O registro de  %(nome)s foi criado com sucesso!'
    

class PessoaDetailView(DetailView):
    model = Pessoa


class PessoaUpdateView(SuccessMessageMixin, UpdateView):
    model = Pessoa
    fields = ['nome', 'data_de_nascimento', 'sexo', 'imagem', ]
    success_message = 'O registro de %(nome)s foi atualizado com sucesso!'


class PessoaDeleteView(SuccessMessageMixin, DeleteView):
    model = Pessoa
    success_url = reverse_lazy('pessoa_list')
