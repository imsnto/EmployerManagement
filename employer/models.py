from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Employer(models.Model):
    company_name = models.CharField(max_length=200)
    contact_person_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=14)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employers')


    def __str__(self):
        return f"{self.contact_person_name} at {self.company_name}"
