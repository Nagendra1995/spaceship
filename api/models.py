# from django.db import models
from django.db import models


# Create your models here.
class spaceship(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ship_id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, unique=True)
    model = models.CharField(max_length=30, unique=False)
    # city=models.CharField(max_length=30, unique=False)
    # planet=models.CharField(max_length=30, unique=False)
    loc = models.ForenignKey(location, on_delete=models.SET_NULL, null=True)
    STATUS_CHOICES = (
        ('decommissioned', 'decommissioned'),
        ('maintenance', 'maintenance '),
        ('operational', 'operational'),
    )
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=None)


class location(models.Model):
    # id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    loc_id = models.PositiveSmallIntegerField(primary_key=True)
    city = models.CharField(max_length=30)
    capacity = models.PositiveSmallIntegerField(default=10)
    PLANET_CHOICES = (
        ('mercury', 'mercury'),
        ('venus', 'venus'),
        ('earth', 'earth'),
        ('mars', 'mars'),
        ('jupiter', 'jupiter'),
        ('saturn', 'saturn'),
        ('uranus', 'uranus'),
        ('neptune', 'neptune')
    )
    planet = models.CharField(max_length=30)

    class Meta:
        unique_together = ("city", "planet")
