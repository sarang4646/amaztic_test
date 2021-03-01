from django.contrib import admin
from .models import User, Profile
from .forms import UserAdmin
from django.contrib.auth.models import Group

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Profile)
