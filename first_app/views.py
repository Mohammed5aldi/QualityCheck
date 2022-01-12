from django.shortcuts import render
from django.http import HttpResponse
from .models import Farm, Trcks, chacks
from .forms import truckInfo
from .filter import chacksFilter
from django.utils import timezone
import django_filters
import django
import datetime
from django.http import HttpResponse, request
import xlwt
from django.contrib.auth.models import User
from django.db.models import Q
import import_export
import csv






  # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////# Save data in database and  view Last input data

# Create your views here.
def index(request):
    trcs =  chacks.objects.all()
    chack = truckInfo(request.POST)
    trc = chacks.objects.all()
    # x = request.GET.get('date')
    # trcs = chacks.objects.latest().filter()
   
    
    if request.method == 'POST':
        chack.save()

    obj= chacks.objects.filter().order_by('-id')[:12]      #View Last data 
        
       
    return render(request, 'index.html', {'data': truckInfo,  'shows':obj })

# ----------------------------------------------------------------------------------------- View Data for Export Excel File
#  

def view_dataExcel(request):
    
    x = request.GET.get('date')
    if request.method == 'GET':
       
        trck = Trcks.objects.all()
        farms = Farm.objects.all()
        trcs = chacks.objects.all()
       
        myfilter = chacksFilter(request.GET, queryset=trcs)
        trc = myfilter.qs[:17]
      

        a = {
            'view_dataExcel': trc,
            'strc': trck,
            'farms': farms,
            'myfilter': myfilter,  
            'date':x,
            # 'dat':z
        }
        return render(request, 'show.html', a)

  # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////   Search Btween Tow Dates                                         #  


def Redate(request):
    
    if request.method == 'POST':
        x = request.POST['fromdate']
        z = request.POST['todate']
        # r = request.POST['farms']
        re = chacks.objects.filter(Q(date__gte=x) & Q(date__lte=z))
        
        d = {
            
            're':re ,
            'x':x ,
            'z':z ,
            }

        return render(request , 'search.html',  d) 
    return render(request,'search.html') 



#//////////////////////////////////////////////////////////////////////////////// print data as Excel File                         
def export_excel(request):
    
    
    response = HttpResponse(content_type='test/csv')
   #response['Content-Disposition'] ="attachment; filename='report.csv'"
       
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Chack')
    row_num = 0                         
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    # a = Farm.objects.filter(date=x)
    columns = ['Farms','Tracks','Date','AOW','DOA','Total Condemenna','Ascites','Septicemia','Runts & Culls','Dermatitis'
                    ,'Others','Gangrene','Whuole Bruises','Pneumodermia','Synovitis','Jaundice','Over scaled','Poor Bleeding','Machine Damage',
                    'Wing Bruises','Wing Broken','Wing Dislocation','Breast Bruises','Breast Skin lesion','Breast Laceration','Legs Bruises',
                    'Legs Scratch','Legs Old Injury','Legs Fractures','Feet Ammonia Burn','Feet Broken']     
    x = request.GET.get('date')
    for col_num in range(len(columns)):                            
        ws.write(row_num, col_num, columns[col_num], font_style)
    rows = chacks.objects.filter(date=str(x)).values_list(
    'farms__name','trucks__name','date','alw','doa','total_condemenna','ascites'
        ,'septicemia','runts_culls','dermatitis','others','gangrene','whuole_bruises'
        ,'peneumodermia','synovitis_arthritis','jaundice','over_scaled','poor_bleeding','machine_damage'
        ,'wing_bruises','wing_broken','wing_dislocation','breast_bruises','breast_skin_lesion','breast_laceration'
        ,'legs_bruises','legs_scrach','legs_old_injury','legs_fractures','feet_ammonia_burn','feet_broken')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response
    



# /////////////////////////////////////////////////////////////////  Just test

# def indexx(request):
#     trcs =  chacks.objects.all()
#     chack = truckInfo(request.POST)
#     trc = chacks.objects.all()
#     # trcs = chacks.objects.latest().filter()
   
    
#     if request.method == 'POST':
#         chack.save()

#     obj= chacks.objects.filter().order_by('-id')[:13]
        
#     myfilter = chacksFilter(request.GET, queryset=trcs)
#     trc = myfilter.qs[:17]
       
#     return render(request, 'test.html', {'data': truckInfo,  'shows':obj })

