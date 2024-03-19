from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = (
            "id",
            "curso",
            "nome",
            "email",
            "comentario",
            "avaliacao",
            "criacao_em",
            "ativo",
        )


class CursoSerializer(serializers.ModelSerializer):
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ("id", "titulo", "url", "criacao_em", "ativo", "avaliacoes")
