from django.urls import path
from .import views

urlpatterns = [
    path('',views.homePage,name='home'),
    path('brand/<slug:brand_slug>/', views.homePage, name='brand_wise_post'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('login/',views.LoginUserView.as_view(),name='login'),
    path('logout/',views.LogoutUserView.as_view(),name='logout'),
    path('detail/<int:id>/', views.DetailsPostView.as_view(),name='detail'),
    path('details/<int:id>/', views.CommentsPostView.as_view(),name='detail_post'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('profile/edit',views.edit_profile,name='edit_profile'),
    path('buy/<int:id>/<int:profile_id>/',views.buy_car,name='buy_car')
]