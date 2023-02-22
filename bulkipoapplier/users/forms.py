from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # email must be unique
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        


        #make widgets for the fields
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',
        'placeholder':'Username',
        'required':'true',
        'pattern':'[a-zA-Z0-9_-]*',
        })
        self.fields['email'].widget.attrs.update({'class': 'form-control',
        'placeholder':'Email',
        'required':'true',
        'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$',
        })
        self.fields['password1'].widget.attrs.update({'class': 'form-control',
        'placeholder':'Password',
        'required':'true',
        
        })
        self.fields['password2'].widget.attrs.update({'class': 'form-control',
        'placeholder':'Confirm Password',
        'required':'true',
        
        })

      