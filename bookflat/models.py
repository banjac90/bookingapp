from django.db import models

class Flat(models.Model):
    name = models.CharField(max_length=100)
  
    def __str__(self):
        return self.name

class Booking(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        # Just return the booking id and the flat name, it is easier to read
        return f"Book {self.pk} for {self.flat.name}"