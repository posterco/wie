from django.contrib import admin
from .models import *
# Register your models here.


class ClubsAdmin(admin.ModelAdmin):
    list_display = ['club_name' , 'club_locality' , 'club_members']
admin.site.register(Clubs , ClubsAdmin)
admin.site.register(JoinedClubs)
admin.site.register(UserEvents)
admin.site.register(Events)