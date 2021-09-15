from django.shortcuts import render, redirect
from .models import us_data, userfile
import pandas as pd
from pathlib import Path
import csv
import os
import pickle
from sklearn.model_selection import train_test_split
from django.core.mail import send_mail
from django.conf import settings
import socket

# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.
def user_login(request):
    return render(request, 'us_design/log_in.html')


def user_registration(request):
    return render(request, 'us_design/register.html')


def user_home(request):
    return render(request, 'us_design/home.html')


def registration(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        pas = request.POST.get('pass')
        email = request.POST.get('email')
        ag = request.POST.get('age')
        gent = request.POST.get('gend')
        dob = request.POST.get('dateofbir')
        stat = request.POST.get('state')
        coun = request.POST.get('country')
        cardno = request.POST.get('cardno')
        exp_mon = request.POST.get('exp_month')
        exp_year = request.POST.get('exp_year')
        cvv = request.POST.get('cvv')
        if nam == "":
            return redirect('user_reg')
        elif pas == "":
            return redirect('user_reg')
        elif email == "":
            return redirect('user_reg')
        elif ag == "":
            return redirect('user_reg')
        elif gent == "":
            return redirect('user_reg')
        elif stat == "":
            return redirect('user_reg')
        elif coun == "":
            return redirect('user_reg')

        elif cardno == "":
            return redirect('user_reg')
        elif exp_mon == "":
            return redirect('user_reg')
        elif exp_year == "":
            return redirect('user_reg')
        elif cvv == "":
            return redirect('user_reg')
        else:
            user=us_data.objects.create(name=nam, password=pas,email=email,
                                   age=ag, gentder=gent,
                                   dob=dob, state=stat,
                                   country=coun, cardno=cardno, exp_month=exp_mon, exp_year=exp_year, cvv=cvv)
        # return redirect('user_log')

    else:
        return redirect('user_reg')
    return render(request,"us_design/input.html",{'user':user})


def login(request):
    output = ""
    output1 = ""
    if request.method == "POST":
        nam = request.POST.get('user_nam')
        pas = request.POST.get('user_pass')
        if nam == "":
            return redirect('user_log')
        elif pas == "":
            return redirect('user_log')
        else:
            if us_data.objects.filter(name=nam, password=pas).exists():
                return redirect('user_home')
            else:
                return redirect('user_log')
        


def credit_data_submit(request):
    output = ""
    output1 = ""
    username = request.POST.get('username')
    print(username)
    month = request.POST.get('month')
    print(month)
    year = request.POST.get('year')
    print(year)
    cvv = request.POST.get('cvv')
    print(cvv)
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("Hostname :  ",host_name)
    print("IP : ",host_ip)
    if us_data.objects.filter(name=username, cvv=cvv, exp_month=month, exp_year=year).exists():
        user = us_data.objects.get(name=username)
        data = userfile.objects.filter(owner=user)
        df = pd.DataFrame(userfile.objects.filter(owner=user).values())
        # print(df)
        pa1 = os.path.join(BASE_DIR, 'media/csvfile/customer.csv')
        df.to_csv(pa1)
        df_test = pd.read_csv('media/csvfile/customer.csv')
        print(df_test)
        df_test = df_test.set_index(['Unnamed: 0', 'id', 'owner_id'])
        print(df_test)
        # df_test=pd.read_csv('media/csvfile/data/test.csv')
        filename = 'media/savfile/finalized_model.sav'  # random forest
        loaded_model = pickle.load(open(filename, 'rb'))
        print(loaded_model.predict(df_test))
        out = loaded_model.predict(df_test)
        if out == 0:
            data = us_data.objects.filter(name=username)
            for i in data:
                request.session['email'] = i.email
                subject = 'success'
                massage = 'success'
                email_from = settings.EMAIL_HOST_USER
                to = [i.email]
                send_mail(subject, massage, email_from, to)
            output = "user is not fraud"
            output1 = ""
        else:

            hostname = socket.gethostname()
            ## getting the IP address using socket.gethostbyname() method
            ip_address = socket.gethostbyname(hostname)
            ## printing the hostname and ip_address
            print(f"Hostname: {hostname}")
            print(f"IP Address: {ip_address}")

            data = us_data.objects.filter(name=username)
            for i in data:
                request.session['email'] = i.email
                subject = 'your account needs to be verified'
                a = 'CLINT IP :', ip_address,'   HOST NAME  :',hostname, 'some one has using your credit card'
                b = " "
                b = b.join(a)
                message = b
                email_from = settings.EMAIL_HOST_USER
                to = [i.email]
                send_mail(subject, message, email_from, to)
            output1 = "user is fraud"
            output = ""
    return render(request, 'us_design/home.html', {'output': output, 'output1': output1})


def inputvalues(request,userid):
    v1 = request.POST.get('v1')
    v2 = request.POST.get('v2')
    v3 = request.POST.get('v3')
    v4 = request.POST.get('v4')
    v5 = request.POST.get('v5')
    v6 = request.POST.get('v6')
    v7 = request.POST.get('v7')
    v8 = request.POST.get('v8')
    v8 = request.POST.get('v8')
    v9 = request.POST.get('v9')
    v10 = request.POST.get('v10')
    v11 = request.POST.get('v11')
    v12 = request.POST.get('v12')
    v13 = request.POST.get('v13')
    v14 = request.POST.get('v14')
    v15 = request.POST.get('v15')
    v16 = request.POST.get('v16')
    v17 = request.POST.get('v17')
    v18 = request.POST.get('v18')
    v19 = request.POST.get('v19')
    v20 = request.POST.get('v20')
    v21 = request.POST.get('v21')
    v22 = request.POST.get('v22')
    v23 = request.POST.get('v23')
    v24 = request.POST.get('v24')
    v25 = request.POST.get('v25')
    v26 = request.POST.get('v26')
    v27 = request.POST.get('v27')
    v28 = request.POST.get('v28')
    user = us_data.objects.get(id=userid)
    userfile.objects.create(owner=user,v1=v1,v2=v2,v3=v3,v4=v4,v5=v5,v6=v6,v7=v7,v8=v8,v9=v9,v10=v10,v11=v11,v12=v12,v13=v13,v14=v14,v15=v15,v16=v16,v17=v17,v18=v18,v19=v19,v20=v20,v21=v21,v22=v22,v23=v23,v24=v24,v25=v25,v26=v26,v27=v27,v28=v28)
    return redirect('user_log')