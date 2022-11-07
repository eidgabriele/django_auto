from django.db import models

# Create your models here.


class Paslauga(models.Model):
    pavadinimas = models.CharField('pavadinimas', max_length = 250, null=False)
    kaina = models.IntegerField('kaina', null = False)
    
    def __str__(self) -> str:
        return f"{self.pavadinimas} {self.kaina}"
    
    class Meta:
        ordering = ['pavadinimas']

class AutomobilioModelis(models.Model):
    marke = models.CharField('marke', max_length = 250, null=False)
    modelis = models.CharField('modelis', max_length = 250)

    def __str__(self) -> str:
        return f"{self.marke} {self.modelis}"
    
    class Meta:
        ordering = ['marke', 'modelis']

class Automobilis(models.Model):
    valstybinis_nr = models.CharField('valstybinis_nr', max_length=13, null=False)
    automobilio_modelis = models.ForeignKey(AutomobilioModelis, on_delete= models.SET_NULL, null= True, blank= True )
    vin_kodas = models.CharField('vin_kodas', max_length = 15, null= False)
    klientas = models.CharField('klientas', max_length= 250, null= False)

    def __str__(self) -> str:
        return f"{self.valstybinis_nr}, {self.automobilio_modelis.modelis}, {self.vin_kodas}, {self.klientas}"

    class Meta:
        ordering = ['klientas', 'valstybinis_nr']

class Uzsakymas(models.Model):
    data = models.DateField('data', null=False)
    automobilis = models.ForeignKey(Automobilis, on_delete=models.SET_NULL, null=True, blank=True)
    suma = models.FloatField('suma', null=False)

    def __str__(self) -> str:
        return f"{self.data} {self.automobilis} {self.suma}"

    class Meta:
        ordering = ['data']

class UzsakymoEilute(models.Model):
    paslauga = models.ForeignKey(Paslauga, on_delete= models.SET_NULL, null= True, blank= True)
    uzsakymas = models.ForeignKey(Uzsakymas, on_delete= models.SET_NULL, null= True, blank= True)
    kiekis = models.IntegerField('kiekis', null= False)
    kaina = models.FloatField('kaina', null= False)

    def __str__(self) -> str:
        return f"{self.paslauga.pavadinimas}, {self.uzsakymas}, {self.kiekis}, {self.kaina}"