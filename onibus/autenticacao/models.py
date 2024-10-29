from django.db import models

# class Passagem (models.Model):
#     dia=models.CharField(max_length=2)
#     destino=models.CharField(max_length=2)
#     horario=models.CharField(max_length=2)

class Cliente(models.Model):
    usuario=models.CharField(max_length=150,null=True)
    dia=models.CharField(max_length=2,null=True)
    destino=models.CharField(max_length=2,null=True)
    horario=models.CharField(max_length=2,null=True)

