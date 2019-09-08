from django.contrib import admin
from .models import *
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

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'
    tem_foto.short_description = 'Possui foto'



class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ('cpf',)

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)