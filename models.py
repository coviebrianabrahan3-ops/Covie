from django.db import models

class Part(models.Model):
    part_number = models.CharField(max_length=100)
    oem = models.CharField(max_length=100)
    description = models.TextField()
    shelf = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    row_position = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.part_number} - {self.description}"
