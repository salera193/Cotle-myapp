from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 標準Userを使用　いずれ変更予定

# 募集投稿
class Recruit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recruit_owner')
    title = models.CharField(max_length=80)    
    content = models.TextField(max_length=1000)
    appcount = 0
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
# フレンド    
class Friend(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
# 募集に対する参加申請
class Apply(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apply_owner')
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)