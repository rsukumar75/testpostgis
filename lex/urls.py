from django.urls import path
from . import views

urlpatterns = [ path('signup/', views.signup, name='signup'),
                path('recommendations/<str:n>/', views.recommendations, name='recommendations'),]
