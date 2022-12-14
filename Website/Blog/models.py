from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 100)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[1:20]

    def pub_date(self):
        return self.publish_date.strftime('%b %e,%y')

    def __str__(self):
        return self.title
