from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=230)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class team_member(models.Model):
    name1 = models.CharField(max_length=230)
    imgs = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.name1
