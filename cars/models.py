from django.contrib.auth.models import User
from django.db import models

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars")
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.JSONField(help_text="Provide tags in JSON format",blank=True,null=True)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)  # Image field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="car_images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.car.title}"
