from django.db import models

# Create your models here.
class Components(models.Model):
    #ImageSlider
    imageslider_id= models.AutoField
    imageslider_image= models.ImageField(upload_to="static/images",default="")

    #Jumbotron
    verse_id=models.AutoField
    verse= models.CharField(max_length=300)