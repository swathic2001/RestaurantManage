
from django.urls import path
from .views import *


from kitchen_app.views import HomeView






from . import views
from kitchen_app.views import *


 




urlpatterns = [

    path('housee/',views.HomeView,name="housee"),
    # path('',LoginView.as_view(),name="LoginView"),
   

      
    path('addkitchen',addkitchen.as_view(), name='addkitchen'),
    path('updateKitchenStatus/',views.update_kitchen_status, name='updateKitchenStatus'),



    path('update_kitchenn/<int:order_id>/', views.update_kitchenn, name='update_kitchenn'),
    path('addkitchen',addkitchen.as_view(), name='addkitchen'),
 
    path('KitchenListView',KitchenListView.as_view(),name='KitchenListView'),

    path('changePasswo',changePassword.as_view(), name='changePasswo'),
    path('updatePasswo',updatePassword.as_view(), name='updatePasswo'),

  
]

    





   





 
   









