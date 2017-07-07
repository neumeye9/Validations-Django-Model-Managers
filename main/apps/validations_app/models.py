from __future__ import unicode_literals

from django.db import models

# Create your models here.

  # Inside your app's models.py file

class UserManager(models.Manager):
    def login(self, email, password):
        print ("login logic here!")
        print ("if successful login occurs pass back a tuple with (True, user)")
        print ("if not successful return a tuple with (False, 'Login unsuccessful')")
        return ("I will be a future login method made by coding dojo students!")

    def register(self, **kwargs):
        # yes we are going to force you guys to parse through some kwards and pass
        # **kwargs(maybe the argument **request.POST)???
        print ("Register login here")
        print ("if successful login occurs pass back a tuple with (True, user)")
        print ("if not successful return a tuple with (False, 'Register unsuccessful)")
        pass
 
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    """
    models come with a hidden key:
    objects = models.Manager()
    we are going to overwrite this!
    """

    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    userManager = UserManager()
    # *************************