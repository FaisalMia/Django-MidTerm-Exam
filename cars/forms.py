from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import CarBrand,CarModel,Comment


class CarBrandForm(ModelForm):
    class Meta:
        model = CarBrand
        fields = '__all__'
        
        
class CarModelForm(ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
        
        
class SignUpForm(UserCreationForm):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    
class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
    

    