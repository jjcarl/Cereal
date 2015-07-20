from django.db import models
from django.db.models import signals
from django.core.mail import send_mail


def send_confirm_email(sender, instance, created, **kwargs):
    send_mail('New Cereal %s' % instance.name, 'The Maker is %s.' % instance.manufacturer, 'jcarl9000@gmail.com', ['jcarl9000@gmail.com'], fail_silently=False)


class CerealMaker(models.Model):
    manufacturer = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.manufacturer


class Cereal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    manufacturer = models.ForeignKey('main.CerealMaker', null=True, blank=True)
    kind = models.CharField(max_length=50, null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    protein = models.IntegerField(null=True, blank=True)
    fat = models.IntegerField(null=True, blank=True)
    sodium = models.IntegerField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    sugars = models.IntegerField(null=True, blank=True)
    potassium = models.IntegerField(null=True, blank=True)
    vitamins = models.IntegerField(null=True, blank=True)
    shelf = models.IntegerField(null=True, blank=True)
    serving_size_weight = models.FloatField(null=True, blank=True)
    cups_per_serving = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Cereal'
        verbose_name_plural = 'Cereals'

signals.post_save.connect(send_confirm_email, sender=Cereal)
