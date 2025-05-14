from django.db import models

# Create your models here.
from datetime import datetime

# Create your models here.
class Users(models.Model):
    title = models.CharField(max_length=12)
    photo = models.IntegerField(default=20)
    addtime=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title+":"+self.photo

    #自定义对应的表名，默认表名：myapp_users
    class Meta:
       db_table="myapp_user"
