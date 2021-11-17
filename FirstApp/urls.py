from django.urls import  path
from .views import *

urlpatterns = [
    path('home/', homeview, name='home'),
    path('retrieve/', retrieveview, name='retrieve'),
    path('update/<int:oid>/', updateview, name='update'),
    path('delete/<int:id>/', deleteview, name='delete'),
]