from django.db import models

class Rol(models.Model):
    rol_name = models.CharField(max_length=50)
    rol_description = models.TextField()
    class Meta:
        db_table = 'rol'
        
class Depart(models.Model):
    Rol = models.ForeignKey(Rol,null=True,on_delete=models.SET_NULL)
    depart_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'depart'

class Emp(models.Model):
    Depart = models.ForeignKey(Depart,null=True,on_delete=models.SET_NULL)
    emp_name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'emp'



