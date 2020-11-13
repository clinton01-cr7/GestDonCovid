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


class Utilisateur(models.Model):
    Utilisateur_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=250)
    role = models.CharField(max_length=10)
    datej = models.DateField(auto_now_add=True)

class Donateur(Utilisateur):
    dateNais = models.DateField()


class Hopital(models.Model):
    hopital_id = models.AutoField(primary_key=True)
    nomH = models.CharField(max_length=25)
    adresse = models.CharField(max_length=25)
    num_compte = models.CharField(max_length=25)
    gouvernorat_FK = models.ForeignKey(Gouvernorat,on_delete=models.CASCADE)
    donateur_FK = models.ManyToManyField(Donateur,through='Don')



class Don(models.Model):
    Utilisateur_id = models.AutoField(primary_key=True)
    donateur_FK = models.ForeignKey(Donateur,on_delete=models.CASCADE)
    hopital_FK = models.ForeignKey(Hopital,on_delete=models.CASCADE)
    montant = models.FloatField()
    dateD = models.DateField(auto_now_add=True)




  


