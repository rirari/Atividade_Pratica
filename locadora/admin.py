from django.contrib import admin

# Register your models here.

from .models import Filme, Locacao, Categoria, Cliente
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nome','email')
    
@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display=('titulo','valor','categoria')

@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display=('nome','data','filme','cliente')