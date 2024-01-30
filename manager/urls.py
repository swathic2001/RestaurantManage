
from django.urls import path
from .views import *


from manager.views import HomeView


from .views import  CustomerListView



from . import views
from .views import *


 




urlpatterns = [

    path('home/',views.HomeView,name="home"),
    # path('',LoginView.as_view(),name="LoginView"),
   


    path('addcustom',addcustomer.as_view(),name="addcustom"),
    path('CustomerListVieew',CustomerListView.as_view(), name='CustomerListVieew'),
    path('DeleteCustomeer', DeleteCustomer.as_view(), name='DeleteCustomeer'),
    path('editcuste/<int:id>/',EditCustomer.as_view(),name="editcuste"),
    path('updatecuste',UpdateCustomer.as_view(),name="updatecuste"),



    
    path('addorde',addorder.as_view(), name='addorde'),
    path('createorde',createorder.as_view(), name='createorde'),
    path('OrderListViews',OrderListView.as_view(),name='OrderListViews'),
    path('DeleteOrde', DeleteOrder.as_view(), name='DeleteOrde'),
    path('editorde/<int:id>/',EditOrder.as_view(),name="editorde"),
    path('update',UpdateOrder.as_view(),name="update"),
   

 path('update_orderr/<int:order_id>/', views.update_order, name='update_orderr'),


  

    path('changePass',changePassword.as_view(), name='changePass'),
    path('updatePass',updatePassword.as_view(), name='updatePass'),
    path('PaymentListView',PaymentListView.as_view(),name='PaymentListView'),



]

    





   





 
   









