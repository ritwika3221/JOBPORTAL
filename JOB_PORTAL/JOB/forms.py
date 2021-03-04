from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import gettext,gettext_lazy as _

class SignUpForm(UserCreationForm):
    # mobile=forms.CharField(label='Mobile',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    # # image=forms.FileField(null=True)
    # gender=forms.CharField(label='Gender',max_length=10)
    password1=forms.CharField(label='Password', max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'ENTER PASSWORD'}))
    password2=forms.CharField(label='Confirm_Password', max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'RE-ENTER PASSWORD'}))
    username=forms.CharField( max_length=15,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','password1','password2']

class SignUpForm2(forms.ModelForm):
    first_name = forms.CharField(label="First Name",required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'Ritwika'}))
    last_name = forms.CharField(label="Last Name",required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'Ghosh'}))
    mobile=forms.CharField(label='Mobile',max_length=12,widget=forms.TextInput(attrs={'class':'form-control'}))
    gender=forms.CharField(label='Gender',max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(label='Email',max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    image=forms.ImageField(label='Image',widget=forms.FileInput(attrs={'class':'form-control'}))
    role=forms.CharField(label="Role",initial="student",widget=forms.TextInput(attrs={'class':'form-control'}))
    upload_resume=forms.FileField(label="Resume",widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model=studentuser
        fields=['first_name','last_name','mobile','email','gender','image','role','upload_resume']

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class ReqruiterSignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password', max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'ENTER PASSWORD'}))
    password2=forms.CharField(label='Confirm_Password', max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'RE-ENTER PASSWORD'}))
    username=forms.CharField( max_length=15,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','password1','password2']

class ReqruiterSignUpForm2(forms.ModelForm):
    first_name = forms.CharField(label="First Name",required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'Ritwika'}))
    last_name = forms.CharField(label="Last Name",required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'Ghosh'}))
    mobile=forms.CharField(label='Mobile',max_length=12,widget=forms.TextInput(attrs={'class':'form-control'}))
    gender=forms.CharField(label='Gender',max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(label='Email',max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    company=forms.CharField(label='Company',max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    image=forms.ImageField(label='Image',widget=forms.FileInput(attrs={'class':'form-control'}))
    role=forms.CharField(initial="reqruiter",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=reqruiteruser
        fields=['first_name','last_name','mobile','email','gender','company','image','role']

class LoginForm2(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class AddJobForm(forms.ModelForm):
    # startdate = forms.DateField(label="Start Date",required=True, widget=forms.SelectDateWidget(attrs={'class': "form-control",}))
    # enddate = forms.DateField(label="End Date",required=True, widget=forms.SelectDateWidget(attrs={'class': "form-control"}))
    title=forms.CharField(label='Title',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    salary=forms.CharField(label='Salary',max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    description=forms.CharField(label='Description',max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    expirence=forms.CharField(label='Expirence',max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    location=forms.CharField(label='Location',widget=forms.TextInput(attrs={'class':'form-control'}))
    skills=forms.CharField(label='Skills',max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    # creationdate=forms.DateField(label='Creation Date',widget=forms.SelectDateWidget(attrs={'class':'form-control'}))
    class Meta:
        model=job
        fields=['title','salary','description','expirence','location','skills']
class contactshows(forms.ModelForm):
    phone= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': '7987643221'}))
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'ritwi3221@gmail.com'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'SUBJECT'}))
    message = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'message'}))
    
    class Meta:
        model=contactmodel
        fields='__all__'
