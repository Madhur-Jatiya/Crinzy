from django.db import models
from datetime import datetime
# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length = 100,default = "")
    description = models.TextField()
    image = models.ImageField(upload_to = 'img/images/')
    url = models.URLField(blank = True)
    popular = models.BooleanField(default = False)
    dateofcourse = models.DateTimeField(default = datetime.now())
    def __str__(self):
        return self.title + '  is popular : ' + str(self.popular)