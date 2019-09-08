from django.contrib import admin
from django.urls import path, include

from clientes import urls as clientes_urls
from home import urls as home_urls
from produtos import urls as produtos_urls
from vendas import urls as vendas_urls

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include(home_urls)),
    path('produtos/', include(produtos_urls)),
    path('vendas/', include(vendas_urls)),
    path('accounts/profile/', include(clientes_urls), name='clientes'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

admin.site.site_header = 'Gestão de Clientes'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Bem Vindo ao GC'