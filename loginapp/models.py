from django.db import models

# Create your models here.
class signupp(models.Model):
    username=models.TextField(unique=True)
    name = models.TextField()
    #password=models.TextField()
    phone=models.TextField()
    #auth=models.BooleanField(default=0)
    #vote=models.TextField(null=True,blank=True)
    confirm_bucks = models.TextField(default=500)
    provision_bucks=models.TextField(default=0)
    def register_u(self):
        self.save()
    def __str__(self):
        return self.username
class eventlist(models.Model):
    username=models.TextField(unique=True)
    event1= models.TextField(default=0)
    event2 = models.TextField(default=0)
    event3 = models.TextField(default=0)
    event4 = models.TextField(default=0)
    event5 = models.TextField(default=0)
    def register_u(self):
        self.save()
    def __str__(self):
        return self.username
class eventpass(models.Model):
    username=models.TextField(unique=True)
    pass1= models.TextField(default=0)
    pass2 = models.TextField(default=0)
    pass3 = models.TextField(default=0)
    pass4 = models.TextField(default=0)
    pass5 = models.TextField(default=0)
    def register_u(self):
        self.save()
    def __str__(self):
        return self.username