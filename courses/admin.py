from django.contrib import admin
from .models import *
# Register your models here.

class CoursesTakenInline(admin.TabularInline):
    model = CoursesTaken

class UserAdmin(admin.ModelAdmin):
    inlines = [CoursesTakenInline,]

admin.site.register(User, UserAdmin)
admin.site.register(GeneralTopic)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(CoursesTaken)
admin.site.register(Country)