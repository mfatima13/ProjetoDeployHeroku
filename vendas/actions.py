def mod_nfe(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)

mod_nfe.short_description = 'nfe - emitida'    

def mod_nfe_no(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)

mod_nfe_no.short_description = 'nfe - não emitida'