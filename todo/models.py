from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    # reation
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owners')
    assigned_to = models.ManyToManyField(User, related_name='assigneds')
    # information
    title = models.CharField('Title', max_length=50)
    description = models.TextField()
    deadline = models.DateTimeField()
    complated = models.BooleanField(default=False)
    
    # moderatior
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    