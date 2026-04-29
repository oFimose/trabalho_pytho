from django.contrib import admin
from .models import Produto, Categoria, Cliente, Administrador
# Register your models here.


admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Administrador)