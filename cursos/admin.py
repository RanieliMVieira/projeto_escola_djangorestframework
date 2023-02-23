from django.contrib import admin

from .models import Avaliacao, Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'avaliacao',
                    'criacao', 'atualizacao', 'ativo')


admin.site.register(Avaliacao, AvaliacaoAdmin)
