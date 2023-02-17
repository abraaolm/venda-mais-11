from django.contrib import admin
from . models import  Atendimento

@admin.register(Atendimento)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('servico','status','data_do_servico','atendente','helper')
    list_filter = ('data_de_cadastro',)