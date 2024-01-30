
from django.urls import path
from .views import *


from rest_app.views import HomeView


from rest_app.views import   CategoryListView , BranchListView,CustomerListView,UserListView,DeleteRestaurant,DeleteBranch,DeleteUser,DeleteStatus



from . import views
from rest_app.views import *


 




urlpatterns = [

    path('homee/',views.HomeView,name="homee"),
    # path('',LoginView.as_view(),name="LoginView"),
   

    path('login_check/',login_check.as_view(),name="login_check"),
    path('addd',add.as_view(),name="addd"),
    
    


    path('addpay',addpay.as_view(), name='addpay'),
    path('changePassword',changePassword.as_view(), name='changePassword'),
    path('updatePassword',updatePassword.as_view(), name='updatePassword'),

    
    

    path('updatePaymentStatus/',views.update_payment_status, name='updatePaymentStatus'),

  
    path('PayListView',PaymentListView.as_view(),name='PayListView'),
    
    path('addkitchen',addkitchen.as_view(), name='addkitchen'),
    path('updateKitchenStatus/',views.update_kitchen_status, name='updateKitchenStatus'),
   path('update_order/<int:order_id>/', views.update_order, name='update_order'),
    path('update_kitchen/<int:order_id>/', views.update_kitchen, name='update_kitchen'),

  
    path('KitchenListVieww',KitchenListView.as_view(),name='KitchenListVieww'),

    path('signin/',SignInView.as_view(),name="signin"),
    path('signup/',SignUpView.as_view(),name="signup"),
  

    path('logout/', logout_view, name='logout'),
 
    
    path('addbranch',addbranch.as_view(),name="addbranch"),
    path('createbranch',createbranch.as_view(),name="createbranch"),
    path('editbranch/<int:id>/',EditBranch.as_view(),name="editbranch"),
    path('updatebranch',UpdateBranch.as_view(),name="updatebranch"),




    path('BranchListView',BranchListView.as_view(),name='BranchListView'),
    path('DeleteBranch', DeleteBranch.as_view(), name='DeleteBranch'),



    path('addcustomerr',addcustomer.as_view(),name="addcustomerr"),
    path('CustomerListVieww',CustomerListView.as_view(), name='CustomerListVieww'),
    path('DeleteCustomerr', DeleteCustomer.as_view(), name='DeleteCustomerr'),
    path('editcustt/<int:id>/',EditCustomer.as_view(),name="editcustt"),
    path('updatecustt',UpdateCustomer.as_view(),name="updatecustt"),


    path('adduserr',adduser.as_view(),name="adduserr"),
    path('UserListVieww',UserListView.as_view(), name='UserListVieww'),
    path('DeleteUserr', DeleteUser.as_view(), name='DeleteUserr'),
    path('edituserr/<int:id>/',EditUser.as_view(),name="edituserr"),
    path('updateuserr',UpdateUser.as_view(),name="updateuserr"),

    
    path('addrestaurantt',addrestaurant.as_view(),name="addrestaurantt"),
    path('createrestaurantt',createrestaurant.as_view(),name="createrestaurantt"),
    path('editrestaurantt/<int:id>/',EditRestaurant.as_view(),name="editrestaurantt"),
    path('updaterestaurantt',UpdateRestaurant.as_view(),name="updaterestaurantt"),
    path('RestaurantListVieww',RestaurantListView.as_view(), name='RestaurantListVieww'),
    path('DeleteRestaurantt', DeleteRestaurant.as_view(), name='DeleteRestaurantt'),

    
    path('addcategoryy',addcategory.as_view(), name='addcategoryy'),
    path('createcategoryy',createcategory.as_view(), name='createcategoryy'),
    path('CategoryListVieww',CategoryListView.as_view(),name='CategoryListVieww'),
    path('DeleteCategoryy', DeleteCategory.as_view(), name='DeleteCategoryy'),
    path('editcategoryy/<int:id>/',EditCategory.as_view(),name="editcategoryy"),
    path('updatecategoryy',UpdateCategory.as_view(),name="updatecategoryy"),

    path('addfooditemm',addfooditem.as_view(), name='addfooditemm'),
    path('createfooditemm',createfooditem.as_view(), name='createfooditemm'),
    path('FoodItemListVieww',FoodItemListView.as_view(),name='FoodItemListVieww'),
    path('DeleteFoodItemm', DeleteFoodItem.as_view(), name='DeleteFoodItemm'),
    path('editfooditemm/<int:id>/',EditFoodItem.as_view(),name="editfooditemm"),
    path('updatefooditemm',UpdateFoodItem.as_view(),name="updatefooditemm"),

    path('addstatuss',addstatus.as_view(), name='addstatuss'),
    path('createstatuss',createstatus.as_view(), name='createstatuss'),
    path('StatusListVieww',StatusListView.as_view(),name='StatusListVieww'),
    path('DeleteStatuss', DeleteStatus.as_view(), name='DeleteStatuss'),
    path('editstatuss/<int:id>/',EditStatus.as_view(),name="editstatuss"),
    path('updatestatuss',UpdateStatus.as_view(),name="updatestatuss"),

    
    path('addorderr',addorder.as_view(), name='addorderr'),
    path('createorderr',createorder.as_view(), name='createorderr'),
    path('OrderListVieww',OrderListView.as_view(),name='OrderListVieww'),
    path('DeleteOrderr', DeleteOrder.as_view(), name='DeleteOrderr'),
    path('editorderr/<int:id>/',EditOrder.as_view(),name="editorderr"),
    path('updateorderr',UpdateOrder.as_view(),name="updateorderr"),

    path('KitchenListVieww',KitchenListView.as_view(),name='KitchenListVieww'),


    # path('addpay',addpay.as_view(), name='addpay'),
  
    path('PayListVieww',PayListView.as_view(),name='PayListVieww'),
]

    





   





 
   









