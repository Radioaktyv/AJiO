from django.db import models


# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


class Dish(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name, self.description


