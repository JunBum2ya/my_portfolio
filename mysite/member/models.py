from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=20)
    user_email=models.EmailField()
    user_id=models.CharField(max_length=20,primary_key=True)
    user_password=models.CharField(max_length=100)
    user_validate=models.BooleanField(default=False)
    user_phonenumber=models.CharField(max_length=15)
    
    def getid(self):
        return self.user_id