from django import forms
from courses.models import Course , Video , UserCourse 
class InstrucForm(forms.Form):
    name = forms.CharField(max_length = 50)
    slug = forms.CharField(max_length = 50  )
    description = forms.CharField(max_length = 200 )
    price = forms.IntegerField()
    discount = forms.IntegerField() 
    active = forms.BooleanField()
    thumbnail = forms.ImageField() 
    date = forms.DateTimeField() 
    resource =forms.FileField()
    length = forms.IntegerField()
    
    title  = forms.CharField(max_length = 100)
   
    serial_number = forms.IntegerField()
    video_id = forms.CharField(max_length = 100)
    is_preview = forms.BooleanField()