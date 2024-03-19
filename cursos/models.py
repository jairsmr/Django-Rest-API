from uuid import uuid4
from django.db import models


class ModelBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    criacao_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(ModelBase):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.titulo


class Avaliacao(ModelBase):
    curso = models.ForeignKey(
        Curso, related_name="avaliacoes", on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default="")
    avaliacao = models.DecimalField(max_digits=20, decimal_places=1)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        unique_together = ("email", "curso")

    def __str__(self):
        return f"{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}"
