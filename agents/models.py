from django.db import models


class Persona(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Agent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_time_agent = models.BooleanField()
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
