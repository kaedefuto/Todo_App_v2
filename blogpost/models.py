from django.db import models
from django.utils import timezone

# Create your models here.

"""
class SampleModel(models.Model):
    title=models.CharField(max_length=100)
    number = models.IntegerField()
"""

"""
class Folder(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
"""


#CATEGORY = (('business','ビジネス'),('life','生活'),('other','その他'))
class BlogModel(models.Model):

    STATUS_CHOICES = [(1, '未完了'),(2, '作業中'),(3, '完了')]
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length = 50)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    #category = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True)
    """
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )
    """
    def __str__(self):
        return self.title
