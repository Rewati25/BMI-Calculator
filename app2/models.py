from django.db import models

class BMIRecord(models.Model):
    name = models.CharField(max_length = 100)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    category = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.name} - BMI: {self.bmi} ({self.category})"

# Create your models here.
