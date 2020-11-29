from django.db import models
# Create your models here.


class Escolas(models.Model):
    nome_Escolas = models.CharField(max_length=200)
    foto = models.ImageField(null=True, blank=True)
    desc_Escolas = models.TextField
    tipo_Escolas = models.CharField(max_length=200)
    conceito_Escolas = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_Escolas
