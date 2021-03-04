from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.utils import timezone
from pip._internal.utils import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None :
                    try:
                        if user.studentuser.role=="student":
                            login(request,user)
                            messages.success(request,'LOGGED IN SUCCESSFULLY')
                            return HttpResponseRedirect('/dashboard/')
                    except:
                        return HttpResponseRedirect('/reqruiter_login/')
        else:            
            form=LoginForm()
    else:
        return HttpResponseRedirect('/user_login/')
    return render(request,'user_login.html',{'form':form})
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user_login/')
def reqruiter_logout(request):
    logout(request)
    return HttpResponseRedirect('/reqruiter_login/')
def dashboard(request):
    return render(request,'dashboard.html')
def add_job(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/reqruiter_login/')
    if request.method=="POST":
        form=AddJobForm(request.POST)
        if form.is_valid():
            # sd=request.POST['startdate']
            # ed=request.POST['enddate']
            t=request.POST['title']
            s=request.POST['salary']
            d=request.POST['description']
            e=request.POST['expirence']
            l=request.POST['location']
            sk=request.POST['skills']
            # c=request.POST['creationdate']
            us=request.user.reqruiteruser
            ins=job(reqruiteruser=us,title=t,salary=s,description=d,expirence=e,location=l,skills=sk)
            ins.save()
            return HttpResponseRedirect('/job_list/')
    else:
        form=AddJobForm()            
    return render(request,'add_job.html',{'form':form})
def job_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/reqruiter_login/')
    us=request.user.reqruiteruser
    x=us.id
    # print(x)
    jobs = job.objects.filter(reqruiteruser=us)
    d={'jobs':jobs,'x':x}
    return render(request,'job_list.html',d)            
def edit_job(request,pid):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/reqruiter_login/')
    # jobs=job.objects.get(id=pid)
    js=job.objects.get(pk=pid)
    if request.method=="POST":
        form=AddJobForm(request.POST,instance=js)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/job_list/')
    else:
        pi=job.objects.get(pk=pid)
        form=AddJobForm(instance=pi)         
    return render(request,'edit_job.html',{'form':form})
def edit_studentprofile(request,pid):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/user_login/')
    # jobs=job.objects.get(id=pid)
    js=studentuser.objects.get(pk=pid)
    if request.method=="POST":
        form=SignUpForm2(request.POST,instance=js)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        pi=studentuser.objects.get(pk=pid)
        form=SignUpForm2(instance=pi)         
    return render(request,'update_student.html',{'form':form})
def edit_reqruiterprofile(request,pid):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/reqruiter_login/')
    # jobs=job.objects.get(id=pid)
    js=reqruiteruser.objects.get(pk=pid)
    if request.method=="POST":
        form=ReqruiterSignUpForm2(request.POST,instance=js)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Rdashboard/')
    else:
        pi=reqruiteruser.objects.get(pk=pid)
        form=ReqruiterSignUpForm2(instance=pi)         
    return render(request,'update_reqruiter.html',{'form':form})
def delete_job(request,pid):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/reqruiter_login/')
    js=job.objects.get(pk=pid)
    js.delete()
    form=job.objects.all()
    messages.success(request,"successfully deleted")
def delete_candidate(request,pid):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/reqruiter_login/')
    js=jobapplied.objects.get(pk=pid)
    js.delete()
    form=jobapplied.objects.all()
    messages.success(request,"successfully deleted")
    return HttpResponseRedirect("/candidate_apply/")
def delete_myjob(request,pid):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/user_login/')
    p=request.user.studentuser
    js=jobapplied.objects.get(studentuser=p,jobid=pid)
    js.delete()
    messages.success(request,"successfully deleted")
    return HttpResponseRedirect("/latest_job/")
def Rdashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/reqruiter_login/')
    # us=request.user.reqruiteruser
    # x=us.id
    # # print(x)
    # reqruiter =reqruiteruser.objects.filter(reqruiteruser=us)
    # d={'reqruiter':reqruiter,'x':x}
    return render(request,'Rdashboard.html')
def user_signup(request):
    if request.method=="POST":
       
        form=SignUpForm(request.POST)
        formnew=SignUpForm2(request.POST,request.FILES)
        if form.is_valid() and formnew.is_valid():
            user=form.save()
            formx=formnew.save(commit=False)
            formx.user=user
            formx.save()
            messages.success(request,"CONGRATS!!!!! YOU HAVE SUCEESFULLY CREATED ACCOUNT")
            return HttpResponseRedirect('/user_login/')
    else:
        form=SignUpForm()
        formnew=SignUpForm2()

    return render(request,'user_signup.html',{'form':form,'formnew':formnew})

def reqruiter_signup(request):
    if request.method=="POST":
        form=ReqruiterSignUpForm(request.POST)
        formnew=ReqruiterSignUpForm2(request.POST,request.FILES)
        if form.is_valid() and formnew.is_valid():
            user=form.save()
            formx=formnew.save(commit=False)
            formx.user=user
            formx.save()
            messages.success(request,"CONGRATS!!!!! YOU HAVE SUCEESFULLY CREATED ACCOUNT")
            return HttpResponseRedirect('/reqruiter_login/')
    else:
        form=ReqruiterSignUpForm()
        formnew=ReqruiterSignUpForm2()

    return render(request,'reqruiter_signup.html',{'form':form,'formnew':formnew})
def reqruiter_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm2(request=request,data=request.POST)
            # formnew=LoginForm2(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                # rtyp=formnew.cleaned_data['type']               
                user=authenticate(username=uname,password=upass)               
                if user is not None : 
                    try:
                        if user.reqruiteruser.role=="reqruiter":   
                            login(request,user)
                            messages.success(request,'LOGGED IN SUCCESSFULLY')
                            return HttpResponseRedirect('/Rdashboard/')
                    except:
                        return HttpResponseRedirect('/user_login/')    
                else:
                    return HttpResponseRedirect('/reqruiter_login/')
        else:            
            form=LoginForm2()
    else:
        return HttpResponseRedirect('/Rdashboard/')
    return render(request,'reqruiter_login.html',{'form':form})
def change_password(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/user_login/')
    error=""
    if request.method=="POST":
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'change_password.html',d)
def change_password2(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/reqruiter_login/')
    error=""
    if request.method=="POST":
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'change_password2.html',d)
def latest_job(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/user_login/')
    form=job.objects.all().order_by('-date')
    return render(request,'latest_job.html',{'form':form})
def apply(request,pid):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/user_login/')
    p=request.user.studentuser
    z=jobapplied(studentuser=p,jobid=pid)
    zz=jobapplied.objects.filter(studentuser=p,jobid=pid)
    if len(zz)==0:
        z.save()
    else:
        messages.warning(request,'Already Applied')
        return HttpResponseRedirect('/latest_job/')
    return HttpResponseRedirect('/dashboard/')
def view_job(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/user_login/')
    us=request.user.studentuser
    # print(x)
    jobs = jobapplied.objects.filter(studentuser=us)
    a=[]
    for fm in jobs:
        if fm.jobid not in a:
            a.append(fm.jobid)
    f=job.objects.filter(pk__in=a)
    d={'f':f,'a':a}
    return render(request,'view_job.html',d)  
def candidate_apply(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/user_login/')
    us=request.user.reqruiteruser
    jobs = job.objects.filter(reqruiteruser=us)
    a=[]
    for fm in jobs:
        a.append(fm.id)
    z=jobapplied.objects.filter(jobid__in=a)
    b=[]
    for fm in z:
        zz=fm.jobid
        pp=job.objects.get(pk=zz)
        # ppp=pp.title
        b.append(pp)
    mylist = zip(z, b)
    d={'mylist':mylist}
    return render(request,'candidate_apply.html',d)
def contact(request):
    if request.method=="POST":
        form=contactshows(request.POST)
        if form.is_valid():
            messages.success(request,"Thank You For Your Feedback")
            form.save()
            return HttpResponseRedirect('/contact/')
    else:
        form=contactshows()
    return render(request,'contact.html',{'form':form})
def searchk(request):
    if request.method=="POST":
            form1=request.POST["search"]
            obj=job.objects.filter(location__icontains=form1)
            if obj:
                if not request.user.is_authenticated:
                    return HttpResponseRedirect('/user_login/')
                return render(request,'search_page.html',{'obj':obj})
            else:
                messages.success(request,"No result Found")
                return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


    
