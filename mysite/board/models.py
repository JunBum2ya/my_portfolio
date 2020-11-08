from django.db import models
from member.models import User

# Create your models here.
class Board(models.Model):
    title=models.CharField(max_length=50,blank=False,null=False)
    user_id=models.ForeignKey('member.User',on_delete=models.CASCADE)
    user_name=models.CharField(max_length=20)
    create_date=models.DateTimeField(null=False)
    update_date=models.DateTimeField()
    detail=models.TextField(max_length=500,null=False)
    count=models.IntegerField(null=False)
    attachment=models.FileField(upload_to='user_upload_files/%Y%m%d/',blank=True,null=True)

class Reply(models.Model):
    board_id=models.ForeignKey(Board,on_delete=models.CASCADE)
    user_id=models.ForeignKey('member.User',on_delete=models.CASCADE)
    detail=models.TextField(max_length=300,null=False)
    
    