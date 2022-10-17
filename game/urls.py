from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name='home' ) , 
    path('game' , views.game , name='game' ) , 
    path('instructions' , views.instructions , name='instructions' ) , 
]
