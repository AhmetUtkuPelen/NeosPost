from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.forms import widgets
from django.contrib.auth.models import User


# ! modeli miras alıp içine tanımlama atıyorum ! #

class UyeGirisForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields["username"].widget.attrs['class'] = 'form-control w-50 '
        self.fields["password"].widget = widgets.PasswordInput(attrs={'class':'form-control w-50'})
        
        
class UyeKayıt(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields["username"].widget = widgets.TextInput(attrs={'class':'form-control w-50'})
        self.fields["first_name"].widget = widgets.TextInput(attrs={'class':'form-control w-50'})
        self.fields["last_name"].widget = widgets.TextInput(attrs={'class':'form-control w-50'})
        self.fields["email"].widget = widgets.EmailInput(attrs={'class':'form-control w-50'})
        self.fields["password1"].widget = widgets.PasswordInput(attrs={'class':'form-control w-50'})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={'class':'form-control w-50'})
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            self.add_error('email','This E-Mail Address Is Already In Use')
        return email
    
    
class sifreDegistir(PasswordChangeForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class':'form-control'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class':'form-control'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class':'form-control'})