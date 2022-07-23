from secrets import choice
from django import forms
from matplotlib.pyplot import title
from .models import Movies, User
from django.forms  import ValidationError
# class SignUpForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ['first_name','gender']


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movies
        fields = ['title','actors','release_date','description','movie_poster','url']

    

class RegistrationForm(forms.ModelForm):
    GENDER  = (
        ('Male','Male'),
        ('Female','Female')
    )
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    age = forms.IntegerField()
    image = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username','image','email','first_name','last_name','age','gender')
    def clean(self):
        errors=[]
        first_name = self.cleaned_data['first_name']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if(password != confirm_password):
            errors.append("Password doesn't match")
        
        if(len(first_name)< 6):
            errors.append("Fistname is too short")
        if(len(username)< 6):
            errors.append("Username is too short")

        if(len(errors) > 0):
            raise ValidationError(errors)

    
    def save(self):
        user  = User(username = self.cleaned_data['username'],gender = self.cleaned_data['gender'],first_name = self.cleaned_data['first_name'],last_name= self.cleaned_data['last_name'],age=self.cleaned_data['age'],email=self.cleaned_data['email'],image= self.cleaned_data['image'])
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
