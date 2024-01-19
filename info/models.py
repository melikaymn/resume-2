from django.db import models

# Create your models here.

class professional_skills(models.Model):
    title=models.CharField(max_length=500,null=True)
    desc=models.CharField(max_length=500,null=True)
    datetime=models.CharField(max_length=500,null=True)
    place=models.CharField(max_length=550,null=True)

    def __str__(self):
        return self.title

class education(models.Model):
    title = models.CharField(max_length=500,null=True)
    desc = models.CharField(max_length=500,null=True)
    place = models.CharField(max_length=500,null=True)
    date = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.title

class skills(models.Model):
    title = models.CharField(max_length=500, null=True)
    persent = models.IntegerField(null=True)

    def __str__(self):
        return self.title



class personal_info(models.Model):
    name= models.CharField(max_length=500,null=True)
    field= models.CharField(max_length=500,null=True)
    about_me = models.TextField(max_length=500,null=True)
    age = models.IntegerField(max_length=500,null=True)
    phone_number = models.IntegerField(max_length=500,null=True)
    address = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name




class skills_2(models.Model):
    title = models.CharField(max_length=550, null=True)
    persent = models.IntegerField(null=True)

    def __str__(self):
        return self.title





