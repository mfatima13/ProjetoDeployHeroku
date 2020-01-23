from django.contrib import admin
from .models import *
<<<<<<< HEAD
class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {
            "fields": (
                ('first_name', 'last_name', 'age', 'photo', 'doc')
            ),            
        }),
        ('Dados complementares', {
            "classes": ('collapse',),
            "fields": (
                ('bio', 'salary')
            )
        }),
    )
    list_filter = ('salary', 'age')
    #fields = (('first_name', 'last_name'), 'age', 'salary', 'bio', 'photo', 'doc')
    #exclude = ('bio', )
    list_display = ('first_name', 'last_name', 'age', 'salary', 'tem_foto', 'doc')
    search_fields = ('id', 'first_name')
    autocomplete_fields = ['doc',]

=======
from .actions import *
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {
            "fields": (
                ('first_name', 'last_name', 'age', 'photo', 'doc')
            ),            
        }),
        ('Dados complementares', {
            "classes": ('collapse',),
            "fields": (
                ('bio', 'salary')
            )
        }),
    )
    list_filter = ('salary', 'age')
    #fields = (('first_name', 'last_name'), 'age', 'salary', 'bio', 'photo', 'doc')
    #exclude = ('bio', )
    list_display = ('first_name', 'last_name', 'age', 'salary', 'tem_foto', 'doc')
    search_fields = ('id', 'first_name')
    autocomplete_fields = ['doc',]

>>>>>>> 8c07669162aa3f3460f16081fa2c03c066068a25
    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'
    tem_foto.short_description = 'Possui foto'

<<<<<<< HEAD

=======
class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id','pessoa', 'get_total', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__cpf')
    autocomplete_fields = ['pessoa', 'produtos']
    readonly_fields = ('valor',)
    #filter_horizontal = ['produtos',]

    actions = [mod_nfe, mod_nfe_no]

    Venda.get_total.short_description = 'Venda'
    """def total(self, obj):
        return obj.get_total()

    total.short_description = 'total'"""

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')
    search_fields = ('id', 'descricao')
>>>>>>> 8c07669162aa3f3460f16081fa2c03c066068a25

class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ('cpf',)

admin.site.register(Person, PersonAdmin)
<<<<<<< HEAD
admin.site.register(Documento, DocumentoAdmin)
=======
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Venda, VendaAdmin)
>>>>>>> 8c07669162aa3f3460f16081fa2c03c066068a25
