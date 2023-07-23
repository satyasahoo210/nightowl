from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


TYPES = [
    ("pub", _("Pub")),
    ("resturant", _("Resturant")),
    ("cafe", _("Cafe")),
]


# Create your models here.
class User(AbstractUser):
    address = models.TextField(_("address"), null=True)
    phone = models.CharField(_("phone"), max_length=15, null=True)
    age = models.IntegerField(
        _("age"), null=True, validators=[validators.MinValueValidator(0)]
    )
    _dp = models.FileField(db_column="dp", upload_to="uploads/dp/", null=True)

    @property
    def dp(self):
        if self._dp:
            return reverse("profile_picture", kwargs={"username": self.username})
        else:
            return self.first_name[0].upper()


class Establishment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    address1 = models.TextField(null=True)
    address2 = models.TextField(null=True)
    street = models.TextField(null=True)
    district = models.TextField(null=True)
    state = models.TextField(null=True)
    pin = models.CharField(max_length=6, null=True)
    rating = models.IntegerField(
        null=True, validators=[validators.MinValueValidator(0)]
    )
    type = models.CharField(max_length=20, choices=TYPES)
    contact = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
    
    def get_address(self) -> str:
        addr = ', '.join((
            self.address1,
            self.address2,
            self.street,
            self.district,
            self.state
        ))

        full_addr = ' - '.join((addr, self.pin))

        return full_addr
    
    def calculated_rating(self):
        return int(Review.objects.filter(establishment = self, active=True).aggregate(models.Avg('rating')).get('rating__avg', 0) or 0)
        


class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.FileField(upload_to="uploads/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
