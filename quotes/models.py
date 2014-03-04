from django.db import models

# Create your models here.

class quote(models.Model):
    quotetypes = (
       ("quote", "quote"),
       ("question", "question")
    )
    content = models.CharField(max_length = 300)
    respos = models.CharField(max_length = 350)
    resneg = models.CharField(max_length = 350)
    quotetype = models.CharField(max_length = 8, choices = quotetypes)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)

    def  __unicode__(self):
        return "%s > %s"  %(self.id, self.content[:20])