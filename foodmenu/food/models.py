from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Item(models.Model):
    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=8)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500, 
        default="https://images.jdmagicbox.com/comp/darjeeling/h1/9999px354.x354.181016125224.y3h1/catalogue/random-fast-food-pedong-darjeeling-fast-food-b66reu0l8c-250.jpg")

    def get_absolute_url(self):
        return reverse("food:details", kwargs={"pk": self.pk})
    