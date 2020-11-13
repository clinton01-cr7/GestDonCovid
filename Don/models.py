from django.db import models

class Gouvernorat(models.Model):
    gouvernorat_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=25)

class Statistique(models.Model):
    statistiqu_id = models.AutoField(primary_key=True)
    cas_positif = models.IntegerField()
    deces = models.IntegerField()
    guerison = models.IntegerField()
    cas_actif = models.IntegerField()
    datest = models.DateField()
    gouvernorat_FK = models.ForeignKey(Gouvernorat,on_delete=models.CASCADE)