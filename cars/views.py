from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CarBrandForm,CarModelForm,SignUpForm
from .models import CarBrand,CarModel
from .import forms


# Create your views here.
def homePage(request,brand_slug=None):
    data = CarModel.objects.all()
    if brand_slug is not None:
        brand = CarBrand.objects.get(slug = brand_slug)
        data = CarModel.objects.filter(car_model=brand)
    carbrands = CarBrand.objects.all()
    
    return render(request,'home.html',{'data' : data,'carbrands' : carbrands})

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['type'] = 'SignUp'
        return context
    
class LoginUserView(LoginView):
    template_name = 'signup.html'
    next_page = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home')
    

class DetailsPostView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'view_detail.html'
    

class CommentsPostView(DetailsPostView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'view_detail.html'
    
    def post(self,request,*args,**kwargs):
        carModel = self.get_object()
        comment_form = forms.CommentForm(data=self.request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.carModel= carModel
            new_comment.save()
        return self.get(request,*args,**kwargs)
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        carModel = self.object
        comments = carModel.comments.all
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
        
        
@login_required
def profile(request,id):
    data = CarModel.objects.filter(id = id)
    return render(request,'profile.html',{'data' : data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request,'profile.html',{'form' : profile_form})

def buy_car(request,id,profile_id):
    car = CarModel.objects.get(id=id)
    # print("faa = ",car)
    # print(id,profile_id)
    
    if car.car_quantity > 0:
        car.car_quantity -= 1
        car.save()
        return redirect('profile',id)
        
    

    

