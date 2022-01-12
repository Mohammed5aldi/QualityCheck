from .models import Trcks, Farm, chacks  
from django import forms
from django.forms import ModelForm, IntegerField
import django.forms
# import django.forms.utils
# import django.forms.widgets


class truckInfo(forms.ModelForm):
    class Meta:
        model = chacks
        fields = ['farms','trucks','alw','doa','total_condemenna','ascites'
        ,'septicemia','runts_culls','dermatitis','others','gangrene','whuole_bruises'
        ,'peneumodermia','synovitis_arthritis','jaundice','over_scaled','poor_bleeding','machine_damage'
        ,'wing_bruises','wing_broken','wing_dislocation','breast_bruises','breast_skin_lesion','breast_laceration'
        ,'legs_bruises','legs_scrach','legs_old_injury','legs_fractures','feet_ammonia_burn','feet_broken'] 
       
        
class view_dataExcel(forms.ModelForm):
    class Meta:
        model = Trcks
        fields = '__all__'
