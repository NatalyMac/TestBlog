from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
        title = models.CharField(max_length=128)
        slug = models.SlugField()
        body = models.TextField()
        published = models.BooleanField(default=True)
        date_posted = models.DateTimeField(auto_now_add=True)

        class Meta:
            ordering = ('-date_posted',)

        def __unicode__(self):
            return self.title

        @models.permalink
        def get_absolute_url(self):
            return ('blog:post', [str(self.id)])

        

