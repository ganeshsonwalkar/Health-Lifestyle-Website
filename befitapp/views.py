from django.contrib.messages.storage.base import Message
from befitapp.models import nutrifact
from django.shortcuts import render
from django.contrib.auth.models import User ,auth
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
import re
from django.shortcuts import redirect
from .models import *
from .models import calorieintake
from .models import bodyf
from django.core.paginator import Paginator
# Create your views here.
lc=None
cal=None
bodyff=None

def reca(request):
    btn=request.POST['rec']

    if request.user.is_authenticated:
        cal=prinfo.objects.latest('id')
        cal69=getattr(cal,'cal')
        cala=int(cal69)*20/100
        calb=int(cal69)*20/100
        calc=int(cal69)*15/100
        cald=int(cal69)*20/100
      
    if(btn =='loose'):
        return render(request,'befitapp/looseweight.html',{
            'breakf':Bmeal.objects.all(),'lunch':Lmeal.objects.all(),
            'even':Emeal.objects.all(),'dinner':Dmeal.objects.all(),
            'first':cala,'second':calb,'third':calc,'fourth':cald,
            'breakf1':Bmeal.objects.all(),'lunch1':Lmeal.objects.all(),
            'even1':Emeal.objects.all(),'dinner1':Dmeal.objects.all()
        })          

    if(btn =='gain'):
        return render(request,'befitapp/gainweight.html',{
            'breakf':Bmeal.objects.all(),'lunch':Lmeal.objects.all(),
            'even':Emeal.objects.all(),'dinner':Dmeal.objects.all(),
            'first':cala,'second':calb,'third':calc,'fourth':cald,
            'breakf1':Bmeal.objects.all(),'lunch1':Lmeal.objects.all(),
            'even1':Emeal.objects.all(),'dinner1':Dmeal.objects.all()
    })      



def home(request):
    articled=article.objects.all()
    return render(request,'befitapp/index.html',{
        'articled':articled
    })
    
def article1(request):
    if request.method == "POST":
        name1=int(request.POST['arti'])
        articled=article.objects.all()
        messages.info(request,name1)
        print(name1)
        return render(request,'befitapp/article.html',{
            'articled':articled
        })    
def gainw(request):
    return render(request,'befitapp/gainweight.html')

def loosew(request):
        return render(request,'befitapp/looseweight.html',{
            'brea':Bmeal.objects.all(),'lunch':Lmeal.objects.all(),
            'even':Emeal.objects.all(),'dinner':Dmeal.objects.all(),
            'breakf1':Bmeal.objects.all(),'lunch1':Lmeal.objects.all(),
            'even1':Emeal.objects.all(),'dinner1':Dmeal.objects.all()
        })              

def fitc(request):
    return render(request,'befitapp/cal.html')

def nutrit(request):
    nutridata=nutrifact.objects.all()
    return render(request,'befitapp/nutri.html',{
        'nutridata':nutridata
    })
    

def yoga(request):
    exer=exercise.objects.all()
    return render(request,'befitapp/yoga.html',{
        'exer':exer
    })
def hiit(request):
    exer=exercise.objects.all()
    return render(request,'befitapp/hiit.html',{
        'exer':exer
    })
def cardio(request):
    exer=exercise.objects.all()
    return render(request,'befitapp/cardio.html',{
        'exer':exer
    })
def heavyw(request):
    exer=exercise.objects.all()
    return render(request,'befitapp/heavy.html',{
        'exer':exer
    })
def aero(request):
    exer=exercise.objects.all()
    return render(request,'befitapp/aero.html',{
        'exer':exer
    })
def loginreg(request):
    return render(request,'befitapp/loginreg.html') 
def profile(request):
    if request.user.is_authenticated:
        profile = request.user   
        prinf=prinfo.objects.all()
        bdf=bodyf.objects.all()
        bbmi=bmi.objects.all()
        pexer=proexe.objects.all()
        prob=pbmeal.objects.all()
        prol=plmeal.objects.all()
        proe=pemeal.objects.all()
        prod=pdmeal.objects.all()
        prinf1=None
        bdf1=None
        bbmi1=None
        pexer1=[]
        prob1=None
        prol1=None
        proe1=None
        prod1=None


        for x in prinf:
            if(x.profile==profile):      
                prinf1=x
        for a in bdf:                    
            if(a.profile==profile):      
                bdf1=a          
        for b in bbmi:                    
            if(b.profile==profile):      
                bbmi1=b 
        for c in bbmi:                    
            if(c.profile==profile):      
                bbmi1=c 
        for d in pexer:                    
            if(d.profile==profile):      
                pexer1.append(d)
        for e in prob:                    
            if(e.profile==profile):      
                prob1=e
        for f in prol:                    
            if(f.profile==profile):      
                prol1=f
        for g in proe:                    
            if(g.profile==profile):      
                proe1=g
        for h in prod:                    
            if(h.profile==profile):      
                prod1=h
        return render(request,'befitapp/profile.html',{
            'prinf':prinf1,'bdf1':bdf1,'bbmi':bbmi1,'pexer':pexer1,'prob':prob1,'prol':prol1,'proe':proe1,'prod':prod1
        })

def addexer(request):
    if request.user.is_authenticated:
        profile = request.user
        ytblink=request.POST['addtop']
        link=proexe.objects.create(profile=profile,link=ytblink)
        link.save()
        messages.info(request,'Added to playlist.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def register(request):
    try:
        if request.method == "POST":
            name1=request.POST['rname']
            mail1=request.POST['remail']
            pass1=request.POST['rpass']
            if not re.match(r'^[a-zA-Z ]+$', name1):
                messages.info(request,'Invalid name.')
                return render(request,'befitapp/loginreg.html') 
            elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', mail1):
                messages.info(request,'Invalid email.')
                return render(request,'befitapp/loginreg.html') 
            elif len(pass1)==0:
                messages.info(request,'Fields cannot be empty.')
                return render(request,'befitapp/loginreg.html')     
            user=User.objects.create_user(name1,mail1,pass1)
            user.save()
            messages.info(request,'Successfully registered.')
            print("Saved")
    except IntegrityError:
        messages.info(request,'Username already exist.')
    return render(request,'befitapp/loginreg.html') 

def loginu(request):
    if request.method == "POST":
        username = request.POST.get("lemail")
        password = request.POST.get("lpass")  
        if len(username)==0:
                messages.info(request,'Fields cannot be empty.')
                return render(request,'befitapp/loginreg.html')  
        elif len(password)==0:
            messages.info(request,'Fields cannot be empty.')
            return render(request,'befitapp/loginreg.html')  
        user = authenticate(request, username=username,password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.info(request,'Successful login.')
            articled=article.objects.all()
            return render(request,'befitapp/index.html',{
                'articled':articled
            })
        else:
            messages.info(request,'Invalid credentials.')
            return render(request,'befitapp/loginreg.html') 
    else:
        return render(request,'befitapp/loginreg.html')

def logout(request): 
    auth.logout(request)
    messages.info(request,'Logged Out.')
    articled=article.objects.all()
    return render(request,'befitapp/index.html',{
            'articled':articled
    })

def calo(request):
    try:
        cw=0.0
        var5=0.0
        if request.method == "POST":
            age1=int(request.POST['age'])
            gender1=request.POST['gender']
            h1=float(request.POST['ht'])   
            w1=float(request.POST['wt']) 
            lg=request.POST['weight'] 
            act=request.POST['act'] 
        if len(str(age1))==0 and  len(str(h1))==0 and len(str(w1))==0 :
            messages.info(request,'Fields cannot be empty.')
            return render(request,'befitapp/cal.html')  
        h1=round(h1/2.54)
        w1=round(h1*2.205)
        if gender1=='female':
            var1=w1*4.35
            var2=h1*4.7
            var3=var1+var2
            var4=age1*4.7
            var5=var3-var4+665
            
            if act=='none':
                cw=var5*1.2
            if act=='light':
                cw=var5*1.375   
            if act=='mod':
                cw=var5*1.55  
            if act=='very':
                cw=var5*1.725  
            if lg=='loose':
                lc=round(cw-500)
                msg='Your metabolic rate is '+str(var5)+' and you will have to take '+str(lc)+' calories to loose 0.5kg weight in a week'
                print(msg)
                messages.info(request,msg)
            if lg=='gain':
                lc=round(cw+500)
                msg='Your metabolic rate is '+str(var5)+' and you will have to take '+str(lc)+' calories to gain 0.5kg weight in a week'
                print(msg)
                messages.info(request,msg)

        if gender1=='male':
            var1=w1*6.23
            var2=h1*12.7
            var3=var1+var2
            var4=age1*6.8
            var5=var3-var4+665
            if act=='none':
                cw=var5*1.2
            if act=='light':
                cw=var5*1.375   
            if act=='mod':
                cw=var5*1.55  
            if act=='very':
                cw=var5*1.725  
            if lg=='loose':
                lc=round(cw-500)
                print(var5)
                print(lc)
                msg='Your metabolic rate is '+str(var5)+' and you will have to take '+str(lc)+' calories to loose 0.5kg weight in a week'
                print(msg)
                messages.info(request,msg)
            if lg=='gain':
                lc=round(cw+500)
                msg='Your metabolic rate is '+str(var5)+' and you will have to take '+str(lc)+' calories to gain 0.5kg weight in a week'
                print(msg)
                messages.info(request,msg) 
        if request.user.is_authenticated:
            profile = request.user
            user1=calorieintake.objects.create(profile=profile,num=str(lc))
            user1.save()
            print('Saved')

        return render(request,'befitapp/cal.html')  
    except MultiValueDictKeyError :
        messages.info(request,'You forgot to click on radio buttons .')
        return render(request,'befitapp/cal.html') 
    except ValueError:
        messages.info(request,'Fields cannot be empty.')
        return render(request,'befitapp/cal.html') 
def bmi1(request):
    try:
        if request.method == "POST":
            age2=request.POST['age1']
            h2=float(request.POST['ht1'])   
            w2=float(request.POST['wt1']) 
            if len(age2)==0  and len(str(h2))==0 and len(str(w2))==0:
                messages.info(request,'Fields cannot be empty.')
                return render(request,'befitapp/cal.html') 
            cal=w2/(h2*h2)
            cal=round(cal, 2)
            if cal <18.5 :
                str4='Your BMI is '+str(cal)+' and you are Underweight.'
                print(str4)
                messages.info(request,str4)
            elif  18.5<cal <24.9 : 
                str1='Your BMI is '+str(cal)+' and you have Normal or Healthy Weight.'
                messages.info(request,str1)
                print(str1)
            elif  25.0<cal <29.9 :
                str2='Your BMI is '+str(cal)+' and you are Overweight.'
                print(str2)
                messages.info(request,str2)    
            elif  cal >30.0 : 
                str3='Your BMI is '+str(cal)+' and you are Obese.'
                print(str3)
                messages.info(request,str3)
            if request.user.is_authenticated:
                profile = request.user
                user2=bmi.objects.create(profile=profile,num=str(cal))
                user2.save()
                print('Saved')        
        return render(request,'befitapp/cal.html') 
    except MultiValueDictKeyError:
        messages.info(request,'You forgot to click on radio buttons .')
        return render(request,'befitapp/cal.html')  
    except ValueError:
        messages.info(request,'Fields cannot be empty.')
        return render(request,'befitapp/cal.html') 
def bodyf1(request):
    try:
        if request.method == "POST":
            age3=int(request.POST['age2'])
            gender3=request.POST['gender2']
            bmi=float(request.POST['bmi'])   
            if len(str(age3))==0 and len(gender3)==0 and len(str(bmi))==0 :
                messages.info(request,'Fields cannot be empty.')
                return render(request,'befitapp/cal.html') 
            if gender3=='female':
                bodyff=(1.20 * bmi) + (0.23 * age3) - 5.4
                strbf='Your body fat percentage is '+str(bodyff)
                messages.info(request,strbf)
            if gender3=='male':
                bodyff=(1.20 * bmi) + (0.23 * age3) - 16.2 
                strbf='Your body fat percentage is '+str(bodyff)
                messages.info(request,strbf)  
            if request.user.is_authenticated:
                profile = request.user
                user3=bodyf.objects.create(profile=profile,num=str(bodyff))
                user3.save()
                print('Saved') 
        return render(request,'befitapp/cal.html')
    except MultiValueDictKeyError:
        messages.info(request,'You forgot to click on radio buttons .')
        return render(request,'befitapp/cal.html') 
    except ValueError:
        messages.info(request,'Fields cannot be empty.')
        return render(request,'befitapp/cal.html')   

def calo1(request):
    try:
        cw=0.0
        var5=0.0
        if request.method == "POST":
            age1=int(request.POST['age'])
            gender1=request.POST['gender']
            h=float(request.POST['ht'])   
            w=float(request.POST['wt'])
            act=request.POST['act'] 
        if len(str(age1))==0 and  len(str(h))==0 and len(str(w))==0 :
            messages.info(request,'Fields cannot be empty.')
            return render(request,'befitapp/Gainweight.html')  
        h1=round(h/2.54)
        w1=round(w*2.205)
        if gender1=='female':
            var1=w1*4.35
            var2=h1*4.7
            var3=var1+var2
            var4=age1*4.7
            var5=var3-var4+665
            
            if act=='none':
                cw=var5*1.2
            if act=='light':
                cw=var5*1.375   
            if act=='mod':
                cw=var5*1.55  
            if act=='very':
                cw=var5*1.725  
            lc=round(cw+500)
            msg='Your metabolic rate is '+str(var5)+' and you will have to take '+str(lc)+' calories to gain 0.5kg weight in a week'
            print(msg)
            messages.info(request,msg)

        if gender1=='male':
            var1=w1*6.23
            var2=h1*12.7
            var3=var1+var2
            var4=age1*6.8
            var5=var3-var4+665
            if act=='none':
                cw=var5*1.2
            if act=='light':
                cw=var5*1.375   
            if act=='mod':
                cw=var5*1.55  
            if act=='very':
                cw=var5*1.725  
            lc=round(cw+500)
            msg='Your metabolic rate is '+str(var5)+' and you will have to take '+str(lc)+' calories to gain 0.5kg weight in a week'
            print(msg)
            print("weight:",w1) 
            print("Height",h1) 
            messages.info(request,msg)
        if request.user.is_authenticated:
            profile = request.user
            user1=prinfo.objects.create(profile=profile,age=age1,gender=gender1,height=h,weight=w,cal=lc,meta=var5)
            user1.save()
            print('Saved')

        return render(request,'befitapp/Gainweight.html')  
    except MultiValueDictKeyError :
        messages.info(request,'You forgot to click on radio buttons .')
        return render(request,'befitapp/Gainweight.html') 
    except ValueError:
        messages.info(request,'Fields cannot be empty.')
        return render(request,'befitapp/Gainweight.html') 

def calo2(request):
    try:
        cw=0.0
        var5=0.0
        if request.method == "POST":
            age1=int(request.POST['age'])
            gender1=request.POST['gender']
            h=float(request.POST['ht'])   
            w=float(request.POST['wt'])
            act=request.POST['act'] 
        if len(str(age1))==0 and  len(str(h))==0 and len(str(w))==0 :
            messages.info(request,'Fields cannot be empty.')
            return render(request,'befitapp/Looseweight.html')  
        h1=round(h/2.54)
        w1=round(w*2.205)
        if gender1=='female':
            var1=w1*4.35
            var2=h1*4.7
            var3=var1+var2
            var4=age1*4.7
            var5=var3-var4+665
            
            if act=='none':
                cw=var5*1.2
            if act=='light':
                cw=var5*1.375   
            if act=='mod':
                cw=var5*1.55  
            if act=='very':
                cw=var5*1.725  
            lc=round(cw-500)
            msg='Your metabolic rate is '+str(var5)+' and you will have to take '+str(lc)+' calories to loose 0.5kg weight in a week'
            print(msg)
            messages.info(request,msg)

        if gender1=='male':
            var1=w1*6.23
            var2=h1*12.7
            var3=var1+var2
            var4=age1*6.8
            var5=var3-var4+665
            if act=='none':
                cw=var5*1.2
            if act=='light':
                cw=var5*1.375   
            if act=='mod':
                cw=var5*1.55  
            if act=='very':
                cw=var5*1.725  
            lc=round(cw-500)
            msg='Your metabolic rate is '+str(var5)+' and you will have to take '+str(lc)+' calories to loose 0.5kg weight in a week'
            print(msg)
            messages.info(request,msg)
        if request.user.is_authenticated:
            profile = request.user
            user1=prinfo.objects.create(profile=profile,age=age1,gender=gender1,height=h,weight=w,cal=lc,meta=var5)
            user1.save()
            print('Saved')

        return render(request,'befitapp/Looseweight.html')  
    except MultiValueDictKeyError :
        messages.info(request,'You forgot to click on radio buttons .')
        return render(request,'befitapp/Looseweight.html') 
    except ValueError:
        messages.info(request,'Fields cannot be empty.')
        return render(request,'befitapp/Looseweight.html') 

def baddmeal(request):
    if request.method == "POST":
        var1=request.POST['bv1']
        var2=request.POST['bv2']
        var3=request.POST['bv3']
        var4=request.POST['bv4']
        var5=request.POST['bv5']
        var6=request.POST['bv6']  
        var7=request.POST['bbtn'] 
        meal1=Bmeal.objects.all()
        meal2=Lmeal.objects.all()
        meal3=Emeal.objects.all()
        meal4=Dmeal.objects.all()
        cal=prinfo.objects.latest('id')
        cal69=getattr(cal,'cal')
        cala=int(cal69)*20/100
        calb=int(cal69)*20/100
        calc=int(cal69)*15/100
        cald=int(cal69)*20/100
        if request.user.is_authenticated:
            profile = request.user
            user1=pbmeal.objects.create(profile=profile,title=var1,imgurl=var2,cal=var3,carb=var4,protien=var5,ytb=var6)
            user1.save()
            messages.info(request,'Added to profile.')
        if (var7=="gain"):
            return render(request,'befitapp/gainweight.html',{
                'breakf':Bmeal.objects.all(),'lunch':Lmeal.objects.all(),
                'even':Emeal.objects.all(),'dinner':Dmeal.objects.all(),
                'first':cala,'second':calb,'third':calc,'fourth':cald,
                'breakf1':Bmeal.objects.all(),'lunch1':Lmeal.objects.all(),
                'even1':Emeal.objects.all(),'dinner1':Dmeal.objects.all()})
        else:
            return render(request,'befitapp/looseweight.html',{
                'breakf':Bmeal.objects.all(),'lunch':Lmeal.objects.all(),
                'even':Emeal.objects.all(),'dinner':Dmeal.objects.all(),
                'first':cala,'second':calb,'third':calc,'fourth':cald,
                'breakf1':Bmeal.objects.all(),'lunch1':Lmeal.objects.all(),
                'even1':Emeal.objects.all(),'dinner1':Dmeal.objects.all()})

def laddmeal(request):
    if request.method == "POST":
        var1=request.POST['lv1']
        var2=request.POST['lv2']
        var3=request.POST['lv3']
        var4=request.POST['lv4']
        var5=request.POST['lv5']
        var6=request.POST['lv6']   
        var7=request.POST['lbtn']
        meal1=Bmeal.objects.all()
        meal2=Lmeal.objects.all()
        meal3=Emeal.objects.all()
        meal4=Dmeal.objects.all()
        cal=prinfo.objects.latest('id')
        cal69=getattr(cal,'cal')
        cala=int(cal69)*20/100
        calb=int(cal69)*20/100
        calc=int(cal69)*15/100
        cald=int(cal69)*20/100
        if request.user.is_authenticated:
            profile = request.user
            user1=plmeal.objects.create(profile=profile,title=var1,imgurl=var2,cal=var3,carb=var4,protien=var5,ytb=var6)
            user1.save()
            messages.info(request,'Added to profile.')
        if (var7=="gain"):
            return render(request,'befitapp/gainweight.html',{
                'breakf':Bmeal.objects.all(),'lunch':Lmeal.objects.all(),
                'even':Emeal.objects.all(),'dinner':Dmeal.objects.all(),
                'first':cala,'second':calb,'third':calc,'fourth':cald,
                'breakf1':Bmeal.objects.all(),'lunch1':Lmeal.objects.all(),
                'even1':Emeal.objects.all(),'dinner1':Dmeal.objects.all()})
        else:
            return render(request,'befitapp/looseweight.html',{
                'breakf':Bmeal.objects.all(),'lunch':Lmeal.objects.all(),
                'even':Emeal.objects.all(),'dinner':Dmeal.objects.all(),
                'first':cala,'second':calb,'third':calc,'fourth':cald,
                'breakf1':Bmeal.objects.all(),'lunch1':Lmeal.objects.all(),
                'even1':Emeal.objects.all(),'dinner1':Dmeal.objects.all()})

def eaddmeal(request):
    if request.method == "POST":
        var1=request.POST['ev1']
        var2=request.POST['ev2']
        var3=request.POST['ev3']
        var4=request.POST['ev4']
        var5=request.POST['ev5']   
        var7=request.POST['ebtn'] 
        meal1=Bmeal.objects.all()
        meal2=Lmeal.objects.all()
        meal3=Emeal.objects.all()
        meal4=Dmeal.objects.all()
        cal=prinfo.objects.latest('id')
        cal69=getattr(cal,'cal')
        cala=int(cal69)*20/100
        calb=int(cal69)*20/100
        calc=int(cal69)*15/100
        cald=int(cal69)*20/100
        if request.user.is_authenticated:
            profile = request.user
            user1=pemeal.objects.create(profile=profile,title=var1,imgurl=var2,cal=var3,carb=var4,protien=var5)
            user1.save()
            messages.info(request,'Added to profile.')
        if (var7=="gain"):
            return render(request,'befitapp/gainweight.html',{
                'breakf':Bmeal.objects.all(),'lunch':Lmeal.objects.all(),
                'even':Emeal.objects.all(),'dinner':Dmeal.objects.all(),
                'first':cala,'second':calb,'third':calc,'fourth':cald,
                'breakf1':Bmeal.objects.all(),'lunch1':Lmeal.objects.all(),
                'even1':Emeal.objects.all(),'dinner1':Dmeal.objects.all()})
        else:
            return render(request,'befitapp/looseweight.html',{
                'breakf':Bmeal.objects.all(),'lunch':Lmeal.objects.all(),
                'even':Emeal.objects.all(),'dinner':Dmeal.objects.all(),
                'first':cala,'second':calb,'third':calc,'fourth':cald,
                'breakf1':Bmeal.objects.all(),'lunch1':Lmeal.objects.all(),
                'even1':Emeal.objects.all(),'dinner1':Dmeal.objects.all()}) 

def daddmeal(request):
    if request.method == "POST":
        var1=request.POST['dv1']
        var2=request.POST['dv2']
        var3=request.POST['dv3']
        var4=request.POST['dv4']
        var5=request.POST['dv5']
        var6=request.POST['dv6']    
        var7=request.POST['dbtn'] 
        meal1=Bmeal.objects.all()
        meal2=Lmeal.objects.all()
        meal3=Emeal.objects.all()
        meal4=Dmeal.objects.all()
        cal=prinfo.objects.latest('id')
        cal69=getattr(cal,'cal')
        cala=int(cal69)*20/100
        calb=int(cal69)*20/100
        calc=int(cal69)*15/100
        cald=int(cal69)*20/100
        
        if request.user.is_authenticated:
            profile = request.user
            user1=pdmeal.objects.create(profile=profile,title=var1,imgurl=var2,cal=var3,carb=var4,protien=var5,ytb=var6)
            user1.save()        
            messages.info(request,'Added to profile.')
        if (var7=="gain"):
            return render(request,'befitapp/gainweight.html',{
                'breakf':Bmeal.objects.all(),'lunch':Lmeal.objects.all(),
                'even':Emeal.objects.all(),'dinner':Dmeal.objects.all(),
                'first':cala,'second':calb,'third':calc,'fourth':cald,
                'breakf1':Bmeal.objects.all(),'lunch1':Lmeal.objects.all(),
                'even1':Emeal.objects.all(),'dinner1':Dmeal.objects.all()})
        else:
            return render(request,'befitapp/looseweight.html',{
                'breakf':Bmeal.objects.all(),'lunch':Lmeal.objects.all(),
                'even':Emeal.objects.all(),'dinner':Dmeal.objects.all(),
                'first':cala,'second':calb,'third':calc,'fourth':cald,
                'breakf1':Bmeal.objects.all(),'lunch1':Lmeal.objects.all(),
                'even1':Emeal.objects.all(),'dinner1':Dmeal.objects.all()})