from django.db import models
from django.contrib.auth.models import User
class employee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    age=models.PositiveIntegerField()
    designation=models.CharField(max_length=255)
    salary=models.PositiveBigIntegerField()
    emailid=models.CharField(max_length=255)
    password=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class details(models.Model):
  
    productname=models.CharField(max_length=255)
    amount=models.PositiveBigIntegerField()
    description=models.CharField(max_length=255)
    discount=models.CharField(max_length=100)
    photo=models.ImageField(upload_to="images/",blank=True)

    def __str__(self) -> str:
        return self.productname
    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/images/user.jpg"







