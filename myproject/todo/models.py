from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)  # 할 일 제목
    completed = models.BooleanField(default=False)  # 완료 여부

    def __str__(self):
        return self.title