from django.db import models

# Create your models here.
class Contact(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=50, blank=False, null=False)
  age = models.IntegerField()
  dob = models.DateField(auto_now=True, blank=False, null=False)
  email = models.EmailField()
  number = models.IntegerField()
  address = models.CharField(max_length=100, blank=False, null=False)
  gender = models.CharField(max_length=50, blank=False, null=False)
  image = models.ImageField(upload_to='images/')


  def __str__(self):
    return self.name