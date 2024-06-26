from django.db import models
import datetime
from django.core.exceptions import ValidationError


class PersonExample(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(default=datetime.date.today)

    class Meta:
        abstract = True


class Parent(PersonExample):
    post = models.TextField()

    def __str__(self) -> str:
        return self.name


class Child(PersonExample):
    is_under_18 = models.BooleanField(default=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


def validate_positive(value):
    if value < 0:
        raise ValidationError(f"Value must be zero or a positive number, got {value}")


class IceCream(models.Model):
    QTYPE_CHOICES = [("C", "Chocolate"), ("V", "Vanilla"), ("M", "Mint")]
    flavor = models.CharField(choices=QTYPE_CHOICES, max_length=300)
    price = models.IntegerField(validators=[validate_positive])

    def __str__(self) -> str:
        return self.flavor


class IceCreamKiosk(models.Model):
    address = models.CharField(max_length=200)
    IceCream = models.ManyToManyField(IceCream, related_name="iceCreams")

    def __str__(self) -> str:
        return self.address
