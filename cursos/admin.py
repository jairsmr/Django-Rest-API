from django.contrib import admin
from .models import Curso, Avaliacao


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "url", "criacao_em", "atualizado_em", "ativo")


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = (
        "curso",
        "nome",
        "comentario",
        "email",
        "avaliacao",
        "criacao_em",
        "atualizado_em",
        "ativo",
    )
