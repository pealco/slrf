from django.db import models

STATUS_CHOICES = (
    ('F', 'Faculty'),
    ('S', 'Student'),
    ('O', 'Other'),
)

class Session(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    leader      = models.CharField(max_length=200)
    place       = models.CharField(max_length=200)
    time        = models.CharField(max_length=50)
    size        = models.PositiveIntegerField()


class Person(models.Model):
    first_name     = models.CharField(max_length=25)
    last_name      = models.CharField(max_length=25)
    email          = models.EmailField()
    affiliation    = models.CharField(max_length=200)
    status         = models.CharField(max_length=1, choices=STATUS_CHOICES)
    session        = models.ForeignKey(Session)
    
    def __unicode__(self):
        return "%s" % (self.full_name + ' ' + self.last_name)



    