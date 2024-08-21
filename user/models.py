from django.db import models
from django.contrib.auth.models import User
from car.models import Car

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='purchases')
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user_name = self.user.first_name if self.user.first_name else self.user.username
        return f"{user_name} bought {self.car.car_name}"
