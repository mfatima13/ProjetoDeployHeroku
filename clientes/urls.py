from django.urls import path
from clientes.views import *
from home.views import home
from .views import PersonList
from .views import PersonDetail
from .views import PersonCreate
from .views import PersonUpdate
from .views import PersonDelete

urlpatterns = [
    path('', home),
    path('list/', person_list, name='person_list'),
    path('new/', person_new, name='person_new'),
    path('update/<int:id>/', person_update, name='person_update'),
    path('delete/<int:id>/', person_delete, name='person_delete'),
    path('person_list/', PersonList.as_view(), name='person_listCBV'),
    path('person_detail/<int:pk>/', PersonDetail.as_view(), name='personDeteilCBV'),
    path('person_create/', PersonCreate.as_view(), name='person_create'),
    path('person_update/<int:pk>/', PersonUpdate.as_view(), name='person_updateCBV'),
    path('person_delete/<int:pk>/', PersonDelete.as_view(), name='person_deleteCBV'),
]
