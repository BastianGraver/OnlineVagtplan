from re import T
from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Users(models.Model):
    type = models.CharField(
        max_length=20,
        choices= [
        ('Super', 'Super'),
        ('Volunteer', 'Volunteer'),
    ],
        default='Volunteer'  # Set the default choice to 'Volunteer'
    )
    id = models.AutoField(primary_key=True)
    registered = models.DateField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    shifts_taken = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    # getter methods
    def get_type(self):
        return self.type
    def get_id(self):
        return self.id
    def get_registered(self):
        return self.registered
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_shifts_taken(self):
        return self.shifts_taken
    
    # setter methods
    def set_name(self, name):
        self.name = name
        self.save()
    def set_email(self, email):
        self.email = email
        self.save()
    def set_phone(self, phone):
        self.phone = phone
        self.save()
    
    # other methods
    def book_shift(self, shift):
        self.shifts_taken += 1
        shift.UsersId = self.id
        shift.save()
    
    def eligible_to_become_super(self):
        time_since_registration = datetime.now().date() - self.registered

        # Check if the time difference is greater than or equal to 365 days (1 year)
        return time_since_registration >= timedelta(days=365)
    
class Movies(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    movie_duration = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    Poster = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Shifts(models.Model):
    type = models.CharField(max_length=20)
    date = models.DateField()
    shift_duration = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE , null=True)
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE , null=True)
    
    def __str__(self):
        return self.type + " " + str(self.date) + " " + self.movie_id.title