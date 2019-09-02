from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import PersonForm
from gestao_clientes import urls

from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
# Create your views here.

# A class objects é um class especial nos manages para manipular os dados
@login_required()
def person_list(request):
    pesquisa = request.GET.get('nome', None)
    if pesquisa:
        persons = Person.objects.filter(first_name__icontains=pesquisa)
    else:
        persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})

@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

# update no django, atenção pois é diferente do update de controleGastos
@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'person': person})

#listView com CBV
class PersonList(ListView):
    model = Person
    #template_name = 'home3.html'

class PersonDetail(DetailView):
    model = Person

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['vendas'] = Venda.objects.filter(
            pessoa_id=self.object.id
        )
        return context

class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/accounts/profile/person_list'

class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_listCBV')

class PersonDelete(DeleteView):
    model = Person
    #success_url = reverse_lazy('person_listCBV')

    def get_success_url(self):
        return reverse_lazy('person_listCBV')

class produtosBulk(View):
    def get(self, request):#Deixar esse trecho comentado pq sempre que atualizar a pagina faz request
        # produtos = ['banana', 'macan', 'limão', 'laranja', 'Pera', 'Abacate']
        # lits_produtos = []
        #
        # for produto in produtos:
        #     p = Produto(descricao=produto, preco=10)
        #     lits_produtos.append(p)
        #
        # Produto.objects.bulk_create(lits_produtos)
        return HttpResponse('Funcionou')