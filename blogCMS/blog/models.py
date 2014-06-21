#!/usr/bin/env python
# encoding: utf-8


from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

    """Docstring for Post. """

    title = models.CharField(u'标题',max_length=128)
    author = models.ForeignKey(User)
    content = models.TextField(u'内容')
    pub_date= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'pk': self.pk})

    def __init__(self):
        """@todo: to be defined1. """
        models.Model.__init__(self)

    def __unicode__(self):
        return self.title



