from django.contrib import admin
from .models import Series, Comment, Rating

admin.site.register(Series)
admin.site.register(Comment)
admin.site.register(Rating)
  # เพิ่ม Category ใน admin
