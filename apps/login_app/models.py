from __future__ import unicode_literals
from django.db import models
from time import localtime, strftime, strptime
from datetime import date, datetime

class CategoriesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if Categories.objects.filter(name__iexact=postData['add_category']):
            errors['add_category'] = "Category already exists"
            return errors
        if len(postData['add_category']) < 2:
            errors['category_name'] = "Category Name must be at least 3 characters long"
        return errors

class Categories(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CategoriesManager()

class SubCategoriesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if SubCategories.objects.filter(name__iexact=postData['add_subcategory']):
            errors['add_subcategory'] = "Course/Subcategory already exists"
            return errors
        if len(postData['add_subcategory']) < 2:
            errors['subcategory_name'] = "Course/Subcategory Name must be at least 3 characters long"
        return errors

class SubCategories(models.Model):
    name = models.CharField(max_length = 255)
    mainCategory = models.ForeignKey(Categories, related_name = 'subcategories')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 
    objects = SubCategoriesManager()

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if 'first_name' in postData:
            birthday = datetime.strptime(postData['birthday'], '%Y-%M-%d')
            age = calculate_age(birthday)

            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name must be at least two characters long"
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name must be at least two characters long"
            if postData['birthday'] > strftime("%Y-%m-%d", localtime()):
                errors['birthday'] = "Birthday should be in the past"
            if age < 18:
                errors['age'] = "Must be 18 years old or older"
            if len(postData['regPassword']) < 8:
                errors['pw_length'] = "Password must be at least eight characters long"
            if postData['regPassword'] != postData['confPassword']:
                errors['pw_match'] = "Passwords do not match!"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255) 
    pw_hash = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    credits = models.IntegerField(default = 3)
    desc = models.TextField(max_length = 255, default = "")
    skills_to_teach = models.ManyToManyField(SubCategories, related_name = "teachers")
    skills_to_learn = models.ManyToManyField(SubCategories, related_name = "students")
    location = models.TextField(max_length = 255, default = "")
    objects = UserManager()

def calculate_age(born):
    today = date.today()
    return today.year - born.year - \
           ((today.month, today.day) < (born.month, born.day))