from django.contrib import admin
from .models import Post
from .models import Feedback

# Register your models here.

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display= ['id','title','author','desc']

@admin.register(Feedback)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'name','email', 'address','message']