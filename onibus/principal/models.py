from django.db import models

class Veiculos(models.Model):
    choices_dia=(('SE','Segunda'),
                 ('QA','Quarta'),
                 ('SA','Sabado'))
    
    choices_destino=(('SP','São Paulo'),
                 ('CA','Campinas'),
                 ('RI','Rio de  Janeiro'))
    
    choices_horario=(('MA','Manhã'),
                 ('TA','Tarde'),
                 ('NO','Noite'))

    dia=models.CharField(max_length=2,choices=choices_dia)
    destino=models.CharField(max_length=2,choices=choices_destino)
    horario=models.CharField(max_length=2,choices=choices_horario)
    p1=models.BooleanField(default=False)
    p2=models.BooleanField(default=False)
    p3=models.BooleanField(default=False)
    p4=models.BooleanField(default=False)
    p5=models.BooleanField(default=False)
    p6=models.BooleanField(default=False)
    p7=models.BooleanField(default=False)
    p8=models.BooleanField(default=False)
    p9=models.BooleanField(default=False)
    p10=models.BooleanField(default=False)
    p11=models.BooleanField(default=False)
    p12=models.BooleanField(default=False)
    p13=models.BooleanField(default=False)
    p14=models.BooleanField(default=False)
    p15=models.BooleanField(default=False)
    p16=models.BooleanField(default=False)