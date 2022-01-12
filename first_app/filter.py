import django_filters
from .models import chacks 
from django_filters import rest_framework as filters
import django.forms
import django.forms.utils
import django.forms.widgets
from django_filters.filters import DateFromToRangeFilter







class chacksFilter(django_filters.FilterSet):
    
    

    class Meta:
        model = chacks
        fields = '__all__' 
        exclude = ['farms','trucks','alw','doa','total_condemenna','ascites'
        ,'septicemia','runts_culls','dermatitis','others','gangrene','whuole_bruises'
        ,'peneumodermia','synovitis_arthritis','jaundice','over_scaled','poor_bleeding','machine_damage'
        ,'wing_bruises','wing_broken','wing_dislocation','breast_bruises','breast_skin_lesion','breast_laceration'
        ,'legs_bruises','legs_scrach','legs_old_injury','legs_fractures','feet_ammonia_burn','feet_broken'] 

       
class chacksDate(django_filters.FilterSet):
    
    date = DateFromToRangeFilter()

    class Meta:
        model = chacks
        fields = '__all__' 
        exclude = ['farms','trucks','alw','doa','total_condemenna','ascites'
        ,'septicemia','runts_culls','dermatitis','others','gangrene','whuole_bruises'
        ,'peneumodermia','synovitis_arthritis','jaundice','over_scaled','poor_bleeding','machine_damage'
        ,'wing_bruises','wing_broken','wing_dislocation','breast_bruises','breast_skin_lesion','breast_laceration'
        ,'legs_bruises','legs_scrach','legs_old_injury','legs_fractures','feet_ammonia_burn','feet_broken'] 
       