from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from models import Usuario

class AdminUsuario(ModelAdmin):
    list_display = ('cdUsuario','deUsuario',)


admin.site.register(Usuario, AdminUsuario)
