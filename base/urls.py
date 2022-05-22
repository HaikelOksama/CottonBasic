
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path("logout/", views.logoutUser, name="logout"),
    path("profile/<str:user>/", views.profileView, name="profile"),
    
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),

    path('cart/<str:pk>/', views.cart, name='cart'),

    path('product/', views.productView, name='product'),
    path('product/<str:pk>/', views.detail, name='detail'),
    path('remove/<str:pk>/', views.remove, name='remove'),
    # path('add/<str:pk>', views.add, name='add'),
    
    path('testimoni/', views.testimoniView, name='testimoni'),
    path('about/', views.aboutView, name='about'),
    path('contact/', views.contactView, name='contact'),
]
