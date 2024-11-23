from django.db import models

class Booking(models.moidel):
    name = model.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeFIeld()

    def __str__(self)
        return self.name
