from django.db import models

# Create your models here.
class Usuario(models.Model):

        cdUsuario = models.CharField(max_length=30)
        deUsuario = models.CharField(max_length=100)
        deSenha = models.CharField(max_length=10)
        flAtivo = models.BooleanField()

        class Meta:
            abstract = True

        def __unicode__(self):
            return self.deUsuario


class Teste(Usuario):

        deTeste = models.CharField(max_length=23)