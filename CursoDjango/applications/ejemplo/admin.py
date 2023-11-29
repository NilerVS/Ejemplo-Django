from django.contrib import admin
from .models import Usuario
# Register your models here.

class usuarioadmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellidoPaterno',
        'apellidoMaterno',

    )

admin.site.register(Usuario,usuarioadmin)