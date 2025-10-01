from django.contrib import admin
from .models import Ingrediente, ItemCardapio, RequisitoReceita, Compra

# Personalização da exibição de Ingredientes
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "quantidade", "unidade", "preco_por_unidade")
    search_fields = ("nome",)

# Personalização da exibição de Itens do Cardápio
class ItemCardapioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "preco_venda", "pode_ser_feito")
    list_filter = ("pode_ser_feito",)
    search_fields = ("titulo",)

# Personalização da exibição de Requisitos de Receita
class RequisitoReceitaAdmin(admin.ModelAdmin):
    list_display = ("item_cardapio", "ingrediente", "quantidade")
    list_filter = ("item_cardapio", "ingrediente")

# Personalização da exibição de Compras
class CompraAdmin(admin.ModelAdmin):
    list_display = ("item_cardapio", "momento_compra")
    list_filter = ("momento_compra",)

# Registar os models com as suas respetivas personalizações
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(ItemCardapio, ItemCardapioAdmin)
admin.site.register(RequisitoReceita, RequisitoReceitaAdmin)
admin.site.register(Compra, CompraAdmin)
