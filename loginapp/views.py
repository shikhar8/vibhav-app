from django.shortcuts import render
from .models import signupp
from .models import eventlist
from .models import eventpass
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
def signuppg(request):
    return render(request,'loginapp/singuppage.html',{})
def registerr(request):
    a=request.POST.get('username')
    b=request.POST.get('password')
    c=request.POST.get('phone_num')
    d = request.POST.get('name')
    #from twilio.rest import Client
    #import random
    #r = str(random.randint(1000, 10000))
    #request.session['r'] = r
    request.session['a'] = a
    request.session['b'] = b
    request.session['c'] = c

    # Your Account SID from twilio.com/console
    """account_sid = "AC58067786c0f209e190314833afee3941"
    # Your Auth Token from twilio.com/console
    auth_token = "72388e654dbf18b6070454972cf2b306"

    client = Client(account_sid, auth_token)
#(863) 532-7522
    #+18635327522
    message = client.messages.create(
        to='+918544235460',
        status_callback='http://postb.in/b/1234abcd',
        from_='+18635327522',
        body=r)

    print(message.sid)
    """
    """""
    import os
    from twilio.rest import Client

    account_sid = os.environ.get('AC58067786c0f209e190314833afee3941')
    auth_token = os.environ.get('72388e654dbf18b6070454972cf2b306')

    client = Client(account_sid, auth_token)

    client.messages.create(from_=os.environ.get('+18635327522'),
                           to=os.environ.get(c),
                           body='You just sent an SMS from Python using Twilio!')
"""
    #return HttpResponse(a)
    cc = eventlist.objects.create(username=a)
    cc.register_u()
    from random import randint
    a1=randint(100, 999)
    a2 = randint(100, 999)
    a3 = randint(100, 999)
    a4 = randint(100, 999)
    a5 = randint(100, 999)
    cc = eventpass.objects.create(username=a,pass1=a1,pass2=a2,pass3=a3,pass4=a4,pass5=a5)
    cc.register_u()
    cc=signupp.objects.create(username=a,phone=c,name=d)
    cc.register_u()
    from django.contrib.auth.models import User
    user = User.objects.create_user(username=a, password=b, email="sample@gmail.com")
    user.save()
    return render(request, 'loginapp/home.html', {})

    #if loginpage.objects.filter(username=a).exists():
    #    return HttpResponse('created')
    #else:
    #    return HttpResponse('not created')
    #return render(request,'loginapp/aut.html',{'c':c})
""""def confirmm(request):
    r= request.session.get('r')
    a = request.session.get('a')
    b = request.session.get('b')
    c = request.session.get('c')
    #return  HttpResponse(b)
    #c= request.POST.get('phone')
    #return HttpResponse(c)
    #us=loginpage.objects.filter(phone=c)
    otp=str(request.POST.get('otp'))
    if otp=="1234" or otp==r:
    #if otp=="1234":
        #fin=signupp.objects.get(phone=c)
        #fin.auth=1
        #fin.register_u()
      cc = signupp.objects.create(username=a, phone=c)
      cc.register_u()
      from django.contrib.auth.models import User
      user = User.objects.create_user(username=a , password=b , email="sample@gmail.com")
      user.save()

    #return HttpResponse(user.email)
        #return render(request, 'loginapp/cc.html', {})
    else:
        return render(request,'loginapp/sf.html',{})
    #x=1
    #return render(request, 'loginapp/home.html', {'x':x})
    return render(request, 'loginapp/ss.html', {})
"""
#def loginn(request):
#    return render(request,'loginapp/loginpage.html',{})
"""def check(request):
    a=request.POST.get('phone')
    b=request.POST.get('password')
    if signupp.objects.filter(phone=a,password=b,auth=1).exists():
        return  HttpResponse('logged in')
    else:
        return  HttpResponse('not logged in')
    from django.contrib.auth import login
    """
from django.contrib.auth.decorators import login_required
@login_required
def vote(request):
    return render(request,'loginapp/vote.html',{})
@login_required
def votecol(request):
    from django.contrib.auth.signals import user_logged_in, user_logged_out
    x=request.user
    a=signupp.objects.get(username=x.username)
    a.vote=request.POST.get('voteb')
    a.register_u()
    return render(request, 'loginapp/vs.html', {})
def home(request):
    return render(request,'loginapp/home.html',{})
def votepre(request):
    from django.http import HttpResponseRedirect
    if not request.user.is_authenticated():
        return HttpResponseRedirect('login')
    else:
        return HttpResponseRedirect('vote')
@login_required
def e1(request):
    info=[]
    a = request.user.username
    b=eventlist.objects.get(username=a)
    c=str(b.event1)
    d=eventpass.objects.get(username=a)
    if str(d.pass1)=='0':
        e='0'
    else:
        e='1'
    info.append(c)
    info.append(e)
    return render(request, 'loginapp/e1.html', {'c':c,'e':e})
def r1(request):
    a=request.user.username
    b=eventlist.objects.get(username=a)
    if b.event1 =='0':
     b.event1=str(a)
     b.save()
     d = signupp.objects.get(username=a)
     d.provision_bucks = str(int(d.provision_bucks) + 100)
     d.save()
     return HttpResponse('registration successfull..!!')
    return HttpResponse('already registered..!!')
def o1(request):
    a=request.user.username
    b = request.POST.get('password')
    c=eventpass.objects.get(username=a)
    if str(c.pass1)== str(b) and c.pass1 != 0:
        d=signupp.objects.get(username=a)
        d.provision_bucks=str(int(d.provision_bucks)-100)
        d.confirm_bucks=str(int(d.confirm_bucks)+100)
        d.save()
        c.pass1=0
        c.save()
        return HttpResponse('right passcode..!!')
    return HttpResponse('wrong passcode..!!')
@login_required
def e2(request):
    info=[]
    a = request.user.username
    b=eventlist.objects.get(username=a)
    c=str(b.event2)
    d=eventpass.objects.get(username=a)
    if str(d.pass2)=='0':
        e='0'
    else:
        e='1'
    info.append(c)
    info.append(e)
    return render(request, 'loginapp/e2.html', {'c':c,'e':e})
def r2(request):
    a=request.user.username
    b=eventlist.objects.get(username=a)
    if b.event2 =='0':
     b.event2=str(a)
     b.save()
     d = signupp.objects.get(username=a)
     d.provision_bucks = str(int(d.provision_bucks) + 100)
     d.save()
     return HttpResponse('registration successfull..!!')
    return HttpResponse('already registered..!!')
def o2(request):
    a=request.user.username
    b = request.POST.get('password')
    c=eventpass.objects.get(username=a)
    if str(c.pass2)== str(b) and c.pass2 != 0:
        d=signupp.objects.get(username=a)
        d.provision_bucks=str(int(d.provision_bucks)-100)
        d.confirm_bucks=str(int(d.confirm_bucks)+100)
        d.save()
        c.pass2=0
        c.save()
        return HttpResponse('right passcode..!!')
    return HttpResponse('wrong passcode..!!')
@login_required
def e3(request):
    info=[]
    a = request.user.username
    b=eventlist.objects.get(username=a)
    c=str(b.event3)
    d=eventpass.objects.get(username=a)
    if str(d.pass3)=='0':
        e='0'
    else:
        e='1'
    info.append(c)
    info.append(e)
    return render(request, 'loginapp/e3.html', {'c':c,'e':e})
def r3(request):
    a=request.user.username
    b=eventlist.objects.get(username=a)
    if b.event3 =='0':
     b.event3=str(a)
     b.save()
     d = signupp.objects.get(username=a)
     d.provision_bucks = str(int(d.provision_bucks) + 100)
     d.save()
     return HttpResponse('registration successfull..!!')
    return HttpResponse('already registered..!!')
def o3(request):
    a=request.user.username
    b = request.POST.get('password')
    c=eventpass.objects.get(username=a)
    if str(c.pass3)== str(b) and c.pass3 != 0:
        d=signupp.objects.get(username=a)
        d.provision_bucks=str(int(d.provision_bucks)-100)
        d.confirm_bucks=str(int(d.confirm_bucks)+100)
        d.save()
        c.pass3=0
        c.save()
        return HttpResponse('right passcode..!!')
    return HttpResponse('wrong passcode..!!')
@login_required
def e4(request):
    info=[]
    a = request.user.username
    b=eventlist.objects.get(username=a)
    c=str(b.event4)
    d=eventpass.objects.get(username=a)
    if str(d.pass4)=='0':
        e='0'
    else:
        e='1'
    info.append(c)
    info.append(e)
    return render(request, 'loginapp/e4.html', {'c':c,'e':e})
def r4(request):
    a=request.user.username
    b=eventlist.objects.get(username=a)
    if b.event4 =='0':
     b.event4=str(a)
     b.save()
     d = signupp.objects.get(username=a)
     d.provision_bucks = str(int(d.provision_bucks) + 100)
     d.save()
     return HttpResponse('registration successfull..!!')
    return HttpResponse('already registered..!!')
def o4(request):
    a=request.user.username
    b = request.POST.get('password')
    c=eventpass.objects.get(username=a)
    if str(c.pass4)== str(b) and c.pass4 != 0:
        d=signupp.objects.get(username=a)
        d.provision_bucks=str(int(d.provision_bucks)-100)
        d.confirm_bucks=str(int(d.confirm_bucks)+100)
        d.save()
        c.pass4=0
        c.save()
        return HttpResponse('right passcode..!!')
    return HttpResponse('wrong passcode..!!')
@login_required
def e5(request):
    info=[]
    a = request.user.username
    b=eventlist.objects.get(username=a)
    c=str(b.event5)
    d=eventpass.objects.get(username=a)
    if str(d.pass5)=='0':
        e='0'
    else:
        e='1'
    info.append(c)
    info.append(e)
    return render(request, 'loginapp/e5.html', {'c':c,'e':e})
def r5(request):
    a=request.user.username
    b=eventlist.objects.get(username=a)
    if b.event5 =='0':
     b.event5=str(a)
     b.save()
     d = signupp.objects.get(username=a)
     d.provision_bucks = str(int(d.provision_bucks) + 100)
     d.save()
     return HttpResponse('registration successfull..!!')
    return HttpResponse('already registered..!!')
def o5(request):
    a=request.user.username
    b = request.POST.get('password')
    c=eventpass.objects.get(username=a)
    if str(c.pass5)== str(b) and c.pass5 != 0:
        d=signupp.objects.get(username=a)
        d.provision_bucks=str(int(d.provision_bucks)-100)
        d.confirm_bucks=str(int(d.confirm_bucks)+100)
        d.save()
        c.pass5=0
        c.save()
        return HttpResponse('right passcode..!!')
    return HttpResponse('wrong passcode..!!')

def profile(request):
    a=request.user.username
    b=signupp.objects.get(username=a)
    c=eventlist.objects.get(username=a)
    return render(request, 'loginapp/profile.html', {'b': b, 'c': c})