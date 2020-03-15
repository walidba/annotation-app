from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.content
class Annotation(models.Model):
    annotator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reponse = models.CharField(max_length=5,choices=[('1','Oui'), ('0','Non'),('2','Autre')],default='1')
    terms = models.CharField(max_length=100,blank=True)

