from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_email


class Profile(BaseModel):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)

class Clubs(BaseModel):
    club_name = models.CharField(max_length=50)
    club_locality = models.CharField(max_length=50)
    club_joined = models.BooleanField(default=False)
    club_members = models.IntegerField(null=True)
    club_presdent = models.CharField(max_length=50)
    club_desc = models.TextField()
    club_events = models.ManyToManyField('Events' , related_name='+' ,blank=True , null=True)

    def __str__(self):
        return str(self.club_name)

class JoinedClubs(BaseModel):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='joined_club_user')
    clubs = models.ManyToManyField(Clubs , null=True)
    test = models.CharField(max_length=10 , null=True)

class Events(BaseModel):
    event_name = models.CharField(max_length=40)
    event_club = models.ForeignKey(Clubs , on_delete=models.CASCADE)
    event_date = models.DateField(null=True , blank=True , auto_now=False , auto_now_add=False)
    event_time = models.TimeField(null=True , blank=True , auto_now=False , auto_now_add=False)
    event_desc = models.TextField(null=True )
    event_registered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.event_name)

class UserEvents(BaseModel):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='event_user')
    user_events = models.ManyToManyField(Events , blank=True)

@receiver(post_save , sender = User)
def send_email_token(sender , instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email , email_token)
    except Exception as e:
        print(e)