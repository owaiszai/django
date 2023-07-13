from django.contrib import admin
from courses.models import Course ,UserCourse, Tag ,Prerequisite , Learning , Video
from django.utils.html import format_html
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class VideoAdmin(admin.TabularInline):
    model = Video

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin , LearningAdmin , PrerequisiteAdmin , VideoAdmin]
    list_display = ["name" , 'get_price' , 'get_discount' , 'active']
    list_filter = ("discount" , 'active')

    def get_discount(self , course):
        return f'{course.discount} %'
    
    def get_price(self , course):
        return f'${course.price}'
    
    get_discount.short_description= "Discount"
    get_price.short_description = "Price"



  

admin.site.register(Course , CourseAdmin)
admin.site.register(Video)
admin.site.register(UserCourse)