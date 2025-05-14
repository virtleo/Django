from django.db import models
from datetime import datetime

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=16)
    addtime=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name+":"+self.phone

    #自定义对应的表名，默认表名：myapp_users
    class Meta:
       db_table="myapp_users"
