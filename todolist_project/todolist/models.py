from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class TodoList(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    date_created=models.DateTimeField(default=datetime.utcnow)
    completed=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
