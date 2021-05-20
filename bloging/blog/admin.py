from django.contrib import admin
from .models import Post,Contact
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(Contact)
class contactus(admin.ModelAdmin):
    list_display = ['id','name','email','phone','message']
