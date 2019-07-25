from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic.base import TemplateView, View
from django.http import HttpResponse

# Create your views here.

def calcular(v, v1):
    print('testando o power mode!')
    return v / v1

# TODO: Refatorar para usar threads assim que possivel
def home(request):
    # debug modo hard
    # import pdb; pdb.set_trace()
    # value1 = 10
    # value2 = 20
    # res = calcular(value1, value2)#, {'result': res}
    return render(request, 'home.html')
#
# def new(request):
#     return render(request, 'person_form.html')
# FIXME: Corrigir bug....
def my_logout(request):
    logout(request)
    return redirect('home')

def my_view(request):

    username = request.POST['username']
    password = request.POSt['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('login')

#CBV

class HomePageView(TemplateView):
    template_name = 'home2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minhaVariavel'] = 'olá, seja bem vindo(a)'
        return context

class MyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home3.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')
