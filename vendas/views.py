from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import *

class Dashboard(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso negado meu filho!')
        return super(Dashboard, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = {'media': Venda.objects.media(),
                'media_desc': Venda.objects.media_desconto(),
                'min': Venda.objects.min(),
                'max': Venda.objects.max(),
                'm_ped': Venda.objects.m_ped(),
                'nfe_ped': Venda.objects.nfe_ped(),
            }
        return render(request, 'vendas/dashboard.html', data)
