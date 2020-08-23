from django.db import models

# Create your models here.
class userdata(models.Model):
    wltaddr = models.CharField(primary_key=True, max_length=50, null = False) #portis wallet address
    gamestate = models.CharField(max_length=1000) #current game value
    #best score on logout
    