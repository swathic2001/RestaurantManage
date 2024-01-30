from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render,redirect
from django.http import JsonResponse
from django.views import View
from rest_app.models import Branch,Customer,Restaurant,Category,FoodItem,FoodItemStatus,Order,Register
from django.views.generic import TemplateView,ListView
from rest_framework.views import APIView
from django.shortcuts import render

# Create your views here.







def HomeView(request):
    order_count =Order.objects.count()
    # restaurant_count = Restaurant.objects.count()
    # branch_count = Branch.objects.count()
    customer_count = Customer.objects.count()
    category_count =Category.objects.count()



    context = {
        'order_count': order_count,
       
        'customer_count':  customer_count,
        'category_count':  category_count,

    }
 
    return render(request,'restaurant/home.html', context)

#############Restaurant
class addrestaurant(TemplateView):
    template_name = "restaurant/addrestaurant.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        blist = Branch.objects.all()
        context={'blist':list(blist)}
        return context

class createrestaurant(APIView):
    def post(self, request, *args, **kwargs):
    
       
        rname = request.POST.get('rname','')
        branch_id = request.POST.get('branch','') 
        user = Restaurant()
        user.rname = rname
        user.branch =Branch.objects.get(branchId=branch_id)
        user.save()
        return redirect('/restaurant/RestaurantListVieew')


class RestaurantListView(ListView):
    model = Restaurant
    template_name = "restaurant/restaurantlist.html"

class DeleteRestaurant(View):
    def  get(self, request):
        restaurantId = request.GET.get('restaurantId', None)
        Restaurant.objects.get(restaurantId=restaurantId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class EditRestaurant(TemplateView):
    template_name = 'restaurant/editrestaurant.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blist = Branch.objects.all()

        try:
            rlist = Restaurant.objects.filter(restaurantId=kwargs['id'])
        except:
            rlist = Restaurant.objects.filter(restaurantId=context['id'])
        context = {'rlist': list(rlist),'blist':list(blist)}
    
        return context
        

class UpdateRestaurant(APIView):
   
    def post(self, request):
        rname = request.POST['rname']
        restaurant_id = request.POST['restaurantId']
        branch_id = request.POST['branch']

        # Assuming branch is a ForeignKey field in Restaurant model
        branch_instance = get_object_or_404(Branch, branchId=branch_id)

        restaurant_instance = get_object_or_404(Restaurant, restaurantId=restaurant_id)
        restaurant_instance.rname = rname
        restaurant_instance.branch = branch_instance
        restaurant_instance.save()

        return JsonResponse({'success': True}, status=200)


        
#############Category#############
class addcategory(TemplateView):
    template_name = 'restaurant/addcategory.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rlist=Restaurant.objects.all()
        blist=Branch.objects.all()
      
        context = {'rlist': list(rlist),'blist':blist}
        return context



class createcategory(APIView):
    def post(self, request, *args, **kwargs):
        cname = request.POST.get('cname', '')
        restaurant_id = request.POST.get('restaurant','')
        ma=Category()
        ma.restaurant = Restaurant.objects.get(restaurantId=restaurant_id)
        ma.cname = cname
        ma.save()
        return redirect('restaurant/CategoryListVieew')


class CategoryListView(ListView):
    model = Category
    template_name ="restaurant/viewcategory.html"

class DeleteCategory(View):
    def  get(self, request):
        categoryId = request.GET.get('categoryId', None)
        Category.objects.get(categoryId=categoryId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class EditCategory(TemplateView):
    template_name = 'restaurant/editcategory.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blist = Branch.objects.all()
        rlist=Restaurant.objects.all()

        try:
            clist =Category.objects.filter(categoryId=kwargs['id'])
        except:
            clist = Category.objects.filter(categoryId=context['id'])
        context = {'clist': list(clist),'rlist': list(rlist),'blist':list(blist)}
    
        return context
        

class UpdateCategory(APIView):
   
    def post(self, request):
        cname = request.POST['cname']
        category_id = request.POST['categoryId']
        restaurant_id = request.POST['restaurant']

        restaurant_instance = get_object_or_404(Restaurant, restaurantId=restaurant_id)

        category_instance = get_object_or_404(Category, categoryId=category_id)
        category_instance.cname = cname
        category_instance.restaurant = restaurant_instance
        category_instance.save()

        return JsonResponse({'success': True}, status=200)


###############Food -----Item###########
class addfooditem(TemplateView):
    template_name = 'restaurant/addfooditem.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blist=Branch.objects.all()
        rlist=Restaurant.objects.all()
        clist=Category.objects.all()
        context = {'clist': list(clist),'rlist':rlist,'blist':blist}
        return context

class createfooditem(APIView):
    def post(self, request, *args, **kwargs):
        fname = request.POST.get('fname', '')
        description = request.POST.get('description', '')
        price = request.POST.get('price', '')
        category_id = request.POST.get('category', '')
        ma=FoodItem()
        ma.category = Category.objects.get(categoryId=category_id)
        ma.fname = fname
        ma.description = description
        ma.price = price
        ma.save()
        return redirect('/restaurant/FoodItemListVieew')


class FoodItemListView(ListView):
    model = FoodItem
    template_name ="restaurant/viewfooditem.html"

class DeleteFoodItem(View):
    def  get(self, request):
        foodId = request.GET.get('foodId', None)
        FoodItem.objects.get(foodId=foodId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class EditFoodItem(TemplateView):
    template_name = 'restaurant/editfooditem.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blist = Branch.objects.all()
        rlist=Restaurant.objects.all()
        clist=Category.objects.all()

        try:
            flist =FoodItem.objects.filter(foodId=kwargs['id'])
        except:
            flist = FoodItem.objects.filter(foodId=context['id'])
        context = {'flist': list(flist),'clist': list(clist),'rlist': list(rlist),'blist':list(blist)}
    
        return context
        

class UpdateFoodItem(APIView):
   
    def post(self, request):
        fname = request.POST['fname']
        food_id = request.POST['foodId']
        description= request.POST['description']
        price = request.POST['price']

        category_id = request.POST['category']

        category_instance = get_object_or_404(Category, categoryId=category_id)

        fooditem_instance = get_object_or_404(FoodItem, foodId=food_id)
        fooditem_instance.fname = fname
        fooditem_instance.description = description

        fooditem_instance.price = price

        fooditem_instance.category = category_instance
        fooditem_instance.save()

        return JsonResponse({'success': True}, status=200)

#########food----------status######
class addstatus(TemplateView):
    template_name = 'restaurant/addstatus.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blist=Branch.objects.all()
        rlist=Restaurant.objects.all()
        clist=Category.objects.all()
        flist=FoodItem.objects.all()

        context = {'flist': list(flist),'clist':list(clist),'rlist':list(rlist),'blist':list(blist)}
        return context




class createstatus(APIView):
    def post(self, request, *args, **kwargs):
        status_name = request.POST.get('status_name', '')
        fooditem_id = request.POST.get('fooditem', '')
        ma=FoodItemStatus()
        ma.fooditem = FoodItem.objects.get(foodId=fooditem_id)
        ma.status_name = status_name
      
        ma.save()
        return redirect('/restaurant/StatusListVieew')


class StatusListView(ListView):
    model = FoodItemStatus
    template_name ="restaurant/viewstatus.html"

class DeleteStatus(View):
    def  get(self, request):
        statusId = request.GET.get('statusId', None)
        FoodItemStatus.objects.get(statusId=statusId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)



class EditStatus(TemplateView):
    template_name = 'restaurant/editstatus.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blist = Branch.objects.all()
        rlist=Restaurant.objects.all()
        clist=Category.objects.all()
        flist=FoodItem.objects.all()

        try:
            slist =FoodItemStatus.objects.filter(statusId=kwargs['id'])
        except:
            slist = FoodItemStatus.objects.filter(statusId=context['id'])
        context = {'slist': list(slist),'flist': list(flist),'clist': list(clist),'rlist': list(rlist),'blist':list(blist)}
    
        return context
        

class UpdateStatus(APIView):


    def post(self, request):
        status_name = request.POST['status_name']
        status_id = request.POST['statusId']
      

        fooditem_id = request.POST['fooditem']

        food_instance = get_object_or_404(FoodItem, foodId=fooditem_id)

        status_instance = get_object_or_404(FoodItemStatus, statusId=status_id)
        status_instance.status_name=status_name
        status_instance.fooditem = food_instance
        status_instance.save()

        return JsonResponse({'success': True}, status=200)
class changePassword(TemplateView):
    """
    Render feature map template
    """
    template_name = 'restaurant/changepassword.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reglist = Register.objects.all()
        context = {'reglist': list(reglist)}
        return context

class updatePassword(APIView):
    """
        ESearch
    """

    def post(self, request):
        """
            Post Request
        :param request:
        :return:
        """
        #print(request.POST)
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        email = request.POST['email']
        Register.objects.filter(email=email).update(password=password,confirm_password=confirm_password)
        return redirect("/login_check")
