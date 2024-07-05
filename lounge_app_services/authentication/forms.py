from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class NewUserForm(UserCreationForm):
	
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm Password'})
        self.fields['username'].widget.attrs.update({'placeholder':self.fields['username'].help_text})
        self.fields['email'].required =True
        self.fields['email'].widget.attrs.update({'placeholder':'email@domain.com'})
        
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")





class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'placeholder':'Enter your Password'})
        self.fields['username'].widget.attrs.update({'placeholder':self.fields['username'].help_text})

    class Meta:
        model = User
        fields = ("username", "password")
        