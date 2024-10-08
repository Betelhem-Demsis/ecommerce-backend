from django.db import models
from django.contrib.auth.models import User
from item.models import Item
# Create your models here.

class Connection(models.Model):
    item=models.ForeignKey(Item,related_name='connections',on_delete=models.CASCADE)
    members=models.ManyToManyField(User,related_name='connections')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-modified_at']

class Conversation(models.Model):
    converse=models.ForeignKey(Connection,related_name='message',on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='created_message',on_delete=models.CASCADE)