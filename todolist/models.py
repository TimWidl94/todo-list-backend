from django.db import models
from django.conf import settings
from datetime import date



# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateField(default=date.today)
    checked = models.BooleanField(default=False)
    
    def __str__(self):
        return f'({self.id}) {self.title}'