from django.db import models

# Create your models here.

class Location(models.Model):
    buildingName = models.CharField(max_length=100)
    roomNumber = models.CharField(max_length=100)
    def __str__(self):
        return self.buildingName + " " + self.roomNumber

class foodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.IntegerField()
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name + ": $" + str(self.price) + " " + str(self.calories) + " cal" + " " + str(self.protein) + "g protein" + " " + str(self.fat) + "g fat" + " " + str(self.carbs) + "g carbs"

class Menu(models.Model):
    name = models.CharField(max_length=100)
    foodItem = models.ManyToManyField(foodItem)
    def __str__(self):
        return self.name

class restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
