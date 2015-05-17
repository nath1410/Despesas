from django.db import models

# Create your models here.
class Usuario(models.Model):

        cdUsuario = models.CharField(max_length=30)
        deUsuario = models.CharField(max_length=100)
        deSenha = models.CharField(max_length=10)
        flAtivo = models.BooleanField()

        def __unicode__(self):
            return self.deUsuario


