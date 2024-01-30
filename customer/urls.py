
from django.urls import path
from .views import *


from customer.views import HomeView


from .views import  CustomerListView



from . import views
from customer.views import *


 




urlpatterns = [

    path('house/',views.HomeView,name="house"),
    # path('',LoginView.as_view(),name="LoginView"),
   

   
   
   

    path('addcustome',addcustomer.as_view(),name="addcustome"),
    path('CustomerListViews',CustomerListView.as_view(), name='CustomerListViews'),
    path('DeleteCustomer', DeleteCustomer.as_view(), name='DeleteCustomer'),
    path('editcus/<int:id>/',EditCustomer.as_view(),name="editcus"),
    path('updatecus',UpdateCustomer.as_view(),name="updatecus"),


   
   
    path('addord',addorder.as_view(), name='addord'),
    path('createord',createorder.as_view(), name='createord'),
    path('OrderListVi',OrderListView.as_view(),name='OrderListVi'),
    path('DeleteOrder', DeleteOrder.as_view(), name='DeleteOrder'),
    path('editord/<int:id>/',EditOrder.as_view(),name="editord"),
    path('updateord',UpdateOrder.as_view(),name="updateord"),

  
]

    





   





 
   









