from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)  # A short text field for the name of the task
    description = models.TextField()         # A larger text field for the task description
    deadline = models.DateTimeField()        # A date and time field for the task deadline

    def __str__(self):
        return self.name