import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Criado às", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado às", auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


# Create your models here.
class BaseModelUuid(models.Model):
    id = models.UUIDField(
        verbose_name="Indentificador",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(verbose_name="Criado às", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado às", auto_now=True)

    class Meta:
        abstract = True


class Variable(models.Model):
    key = models.SlugField(
        verbose_name="Indentificador",
        max_length=100,
        primary_key=True,
    )
    value = models.TextField(verbose_name="Valor")
    created_at = models.DateTimeField(verbose_name="Criado às", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado às", auto_now=True)

    class Meta:
        verbose_name = "Variavel"
        verbose_name_plural = "Variaveis"
        ordering = ["key"]

    def __str__(self):
        return self.key
