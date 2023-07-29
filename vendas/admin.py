from django.contrib import admin

from vendas.models import Cliente, Pedido, ItemPedido


class ClienteAdmin(admin.ModelAdmin):

    list_display = ['nome', 'email', 'cpf']
    search_fields = ['nome', 'email', 'cpf']


class PedidoAdmin(admin.ModelAdmin):

    list_display = ['cliente', 'data']


class ItemAdmin(admin.ModelAdmin):

    list_display = ['pedido', 'produto', 'quantidade', 'preco']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido, ItemAdmin)
