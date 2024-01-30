
from django.urls import path
from .views import *


from restaurant.views import HomeView


from restaurant.views import   CategoryListView ,DeleteRestaurant,DeleteStatus



from . import views
from restaurant.views import *


 




urlpatterns = [
    
       
    path('index/',views.HomeView,name="index"),
   

    
    path('addrestaurannt',addrestaurant.as_view(),name="addrestaurannt"),
    path('createrestaurannt',createrestaurant.as_view(),name="createrestaurannt"),
    path('editrestaurannt/<int:id>/',EditRestaurant.as_view(),name="editrestaurannt"),
    path('updaterestaurannt',UpdateRestaurant.as_view(),name="updaterestaurannt"),
    path('RestaurantListVieew',RestaurantListView.as_view(), name='RestaurantListVieew'),
    path('DeleteRestaurannt', DeleteRestaurant.as_view(), name='DeleteRestaurannt'),

    
    path('addcategoryy',addcategory.as_view(), name='addcategoryy'),
    path('createcategoryy',createcategory.as_view(), name='createcategoryy'),
    path('CategoryListVieew',CategoryListView.as_view(),name='CategoryListVieew'),
    path('DeleteCategoryy', DeleteCategory.as_view(), name='DeleteCategoryy'),
    path('editcategoryy/<int:id>/',EditCategory.as_view(),name="editcategoryy"),
    path('updatecategoryy',UpdateCategory.as_view(),name="updatecategoryy"),

    path('addfooditeem',addfooditem.as_view(), name='addfooditeem'),
    path('createfooditeem',createfooditem.as_view(), name='createfooditeem'),
    path('FoodItemListVieew',FoodItemListView.as_view(),name='FoodItemListVieew'),
    path('DeleteFoodIteem', DeleteFoodItem.as_view(), name='DeleteFoodIteem'),
    path('editfooditeem/<int:id>/',EditFoodItem.as_view(),name="editfooditeem"),
    path('updatefooditeem',UpdateFoodItem.as_view(),name="updatefooditeem"),

    path('addstatuus',addstatus.as_view(), name='addstatuus'),
    path('createstatuus',createstatus.as_view(), name='createstatuus'),
    path('StatusListVieew',StatusListView.as_view(),name='StatusListVieew'),
    path('DeleteStatuus', DeleteStatus.as_view(), name='DeleteStatuus'),
    path('editstatuus/<int:id>/',EditStatus.as_view(),name="editstatuus"),
    path('updatestatuus',UpdateStatus.as_view(),name="updatestatuus"),

    path('changePasswor',changePassword.as_view(), name='changePasswor'),
    path('updatePasswor',updatePassword.as_view(), name='updatePasswor'),
   
]

    





   





 
   









