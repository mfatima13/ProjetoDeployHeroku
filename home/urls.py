from django.urls import path
from home.views import home, my_logout

urlpatterns = [
    path('', home, name='home'),
    # path('new/', new, name='new'),
    path('logout/', my_logout, name='logout'),
 #   path('login/', my_view, name='login')
]