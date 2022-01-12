from django.db import models

# Create your models here.

from django.utils import timezone




class Farm(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Trcks(models.Model):

    name = models.CharField(max_length=50, null=True)
   

    def __str__(self):
        return self.name


class chacks(models.Model):
    farms = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True)
    trucks = models.ForeignKey(Trcks, on_delete=models.CASCADE, null=True)
    alw = models.FloatField(blank=True, null=True )
    doa = models.IntegerField(blank=True, null=True)
    total_condemenna = models.IntegerField(blank=True, null=True)
    ascites = models.IntegerField(blank=True, null=True)
    septicemia = models.IntegerField(blank=True, null=True)
    runts_culls = models.IntegerField(blank=True, null=True)
    dermatitis = models.IntegerField(blank=True, null=True)
    others = models.IntegerField(blank=True, null=True)
    gangrene = models.IntegerField(blank=True, null=True)
    whuole_bruises = models.IntegerField(blank=True, null=True)
    peneumodermia = models.IntegerField(blank=True, null=True)
    synovitis_arthritis = models.IntegerField(blank=True, null=True)
    jaundice = models.IntegerField(blank=True, null=True)
    over_scaled = models.IntegerField(blank=True, null=True)
    poor_bleeding = models.IntegerField(blank=True, null=True)
    machine_damage = models.CharField(max_length=20, default='', blank=True)
    wing_bruises = models.CharField(max_length=20, default='', blank=True)
    wing_broken = models.CharField(max_length=20, default='', blank=True)
    wing_dislocation = models.CharField(max_length=20, default='', blank=True)
    breast_bruises = models.CharField(max_length=20, default='', blank=True)
    breast_skin_lesion = models.CharField(max_length=20, default='', blank=True)
    breast_laceration = models.CharField(max_length=20, default='', blank=True)
    legs_bruises  = models.CharField(max_length=20,default='', blank=True)
    legs_scrach = models.CharField(max_length=20,default='', blank=True)
    legs_old_injury = models.CharField(max_length=20, default='', blank=True)
    legs_fractures = models.CharField(max_length=20, default='', blank=True)
    feet_ammonia_burn = models.CharField(max_length=20,default='', blank=True)
    feet_broken = models.CharField(max_length=20, default='', blank=True)
    
    date = models.DateField(default=timezone.now)


    def __str__(self):
        return str(self.trucks)
