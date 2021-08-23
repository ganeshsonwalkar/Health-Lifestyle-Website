from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class nutrifact(models.Model):
    Food = models.CharField(max_length=100)
    Serving = models.CharField(max_length=100)
    Calories = models.CharField(max_length=100)
    Carbs = models.CharField(max_length=100)
    Total_Fats = models.CharField(max_length=100)
    Sat_fats = models.CharField(max_length=100)
    Trans_Fat = models.CharField(max_length=100)
    Chol = models.CharField(max_length=100)
    Fiber = models.CharField(max_length=100)
    Sugar = models.CharField(max_length=100)
    Protien = models.CharField(max_length=100)
    Calcium = models.CharField(max_length=100)
    Iron = models.CharField(max_length=100)


class calorieintake(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.CharField(max_length=100)


class bmi(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.CharField(max_length=100)


class bodyf(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.CharField(max_length=100)


class exercise(models.Model):
    type = models.CharField(max_length=100)
    link = models.CharField(max_length=500, primary_key=True)


class proexe(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)


class article(models.Model):
    imgurl = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    bline = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)


class Bmeal(models.Model):
    imgurl = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    cal = models.CharField(max_length=100)
    carb = models.CharField(max_length=100)
    protien = models.CharField(max_length=100)
    ytb = models.CharField(max_length=100)


class Lmeal(models.Model):
    imgurl = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    cal = models.CharField(max_length=100)
    carb = models.CharField(max_length=100)
    protien = models.CharField(max_length=100)
    ytb = models.CharField(max_length=100)


class Emeal(models.Model):
    imgurl = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    cal = models.CharField(max_length=100)
    carb = models.CharField(max_length=100)
    protien = models.CharField(max_length=100)


class Dmeal(models.Model):
    imgurl = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    cal = models.CharField(max_length=100)
    carb = models.CharField(max_length=100)
    protien = models.CharField(max_length=100)
    ytb = models.CharField(max_length=100)


class prinfo(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    cal = models.CharField(max_length=100)
    meta = models.CharField(max_length=100)


class pbmeal(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    imgurl = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    cal = models.CharField(max_length=100)
    carb = models.CharField(max_length=100)
    protien = models.CharField(max_length=100)
    ytb = models.CharField(max_length=100)


class plmeal(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    imgurl = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    cal = models.CharField(max_length=100)
    carb = models.CharField(max_length=100)
    protien = models.CharField(max_length=100)
    ytb = models.CharField(max_length=100)


class pemeal(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    imgurl = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    cal = models.CharField(max_length=100)
    carb = models.CharField(max_length=100)
    protien = models.CharField(max_length=100)
    ytb = models.CharField(max_length=100)


class pdmeal(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    imgurl = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    cal = models.CharField(max_length=100)
    carb = models.CharField(max_length=100)
    protien = models.CharField(max_length=100)
    ytb = models.CharField(max_length=100)
