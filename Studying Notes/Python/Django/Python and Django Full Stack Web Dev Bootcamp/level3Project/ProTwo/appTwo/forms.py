from django import forms
from appTwo.models import UserSignup

class SignupForm(forms.ModelForm):

    class Meta:
        model = UserSignup
        fields = ['username', 'userpass', 'useremail']
        labels = {
            'username':'Username:',
            'userpass':'Password:',
            'useremail':'Email Address:'
        }