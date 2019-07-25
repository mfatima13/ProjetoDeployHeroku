from django.urls import path
from home.views import home, my_logout,  HomePageView, MyView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', home, name='home'),
    # path('new/', new, name='new'),
    path('logout/', my_logout, name='logout'),
    path('home2/', TemplateView.as_view(template_name='home2.html'), name='home2'),#mas isso só mostra um arquivo html puro -\
    path('home3/',  HomePageView.as_view(template_name='home3.html'), name='home3'),
    path('view/', MyView.as_view()),
]