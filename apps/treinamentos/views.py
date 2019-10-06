from django.contrib.messages.views import SuccessMessageMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from apps.pessoas.models import Pessoa
from apps.treinamentos.models import Treinamento


def create_treinamento(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)
    TreinamentoFormset = inlineformset_factory(Pessoa, Treinamento,
                                               fields=('treinamento', 'imagem', ),
                                               can_delete=True, extra=1)
    
    if request.method == 'POST':
        formset = TreinamentoFormset(request.POST, instance=pessoa)
        if formset.is_valid():
            formset.save()
            
            redirect('treinamentos/treinamento_form.html', pessoa_id=pessoa.id)
    
    formset = TreinamentoFormset(instance=pessoa)
    
    return render(request, 'treinamentos/treinamento_form.html', {'pessoa': pessoa,
                                                                  'formset':  formset})

