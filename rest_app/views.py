from django.shortcuts import get_object_or_404, render,redirect
from django.http import JsonResponse
from django.views import View
from rest_app.models import Branch,User,Customer,Restaurant,Category,FoodItem,FoodItemStatus,Order,Register
from django.views.generic import TemplateView,ListView
from rest_framework.views import APIView
from django.shortcuts import render

# Create your views here.




def HomeView(request):
    order_count =Order.objects.count()
    restaurant_count = Restaurant.objects.count()
    branch_count = Branch.objects.count()
    customer_count = Customer.objects.count()
    user_count = User.objects.count()



    context = {
        'order_count': order_count,
        'restaurant_count':  restaurant_count,
        'branch_count':  branch_count,
        'customer_count':  customer_count,
        'user_count':  user_count,

    }
 
    return render(request,'rest_app/index.html', context)




##############Branch
    
class addbranch(TemplateView):
    template_name = "rest_app/addbranch.html"

class createbranch(APIView):
    def post(self, request,*args,**kwargs):
        bname = request.POST.get('bname')
        user=Branch()
        user.bname=bname
    
        user.save()
        return redirect('/BranchListView')

class BranchListView(ListView):
    model = Branch
    template_name ="rest_app/branchlist.html"

class DeleteBranch(View):
    def  get(self, request):
        branchId = request.GET.get('branchId', None)
        Branch.objects.get(branchId=branchId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    



class EditBranch(TemplateView):
    template_name = 'rest_app/editbranch.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['id'] = self.kwargs['id']
            blist = Branch.objects.filter(branchId=context['id'])
        except:
            blist = Branch.objects.filter(branchId=context['id'])
            
        context['blist']= list(blist)
        return context

class UpdateBranch(APIView):
   
    def post(self, request):
       
        bname = request.POST['bname']
       
        branchId = request.POST['branchId']
       
        products=Branch.objects.get(branchId=branchId)
        products.bname=bname
       
        products.save()
        return JsonResponse({'success': True}, status=200)
      


#############Restaurant
class addrestaurant(TemplateView):
    template_name = "rest_app/addrestaurant.html"
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
        return redirect('/RestaurantListVieww')


class RestaurantListView(ListView):
    model = Restaurant
    template_name = "rest_app/restaurantlist.html"

class DeleteRestaurant(View):
    def  get(self, request):
        restaurantId = request.GET.get('restaurantId', None)
        Restaurant.objects.get(restaurantId=restaurantId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class EditRestaurant(TemplateView):
    template_name = 'rest_app/editrestaurant.html'
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
    template_name = 'rest_app/addcategory.html'
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
        return redirect('/CategoryListVieww')


class CategoryListView(ListView):
    model = Category
    template_name ="rest_app/viewcategory.html"

class DeleteCategory(View):
    def  get(self, request):
        categoryId = request.GET.get('categoryId', None)
        Category.objects.get(categoryId=categoryId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class EditCategory(TemplateView):
    template_name = 'rest_app/editcategory.html'
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
    template_name = 'rest_app/addfooditem.html'
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
        return redirect('/FoodItemListVieww')


class FoodItemListView(ListView):
    model = FoodItem
    template_name ="rest_app/viewfooditem.html"

class DeleteFoodItem(View):
    def  get(self, request):
        foodId = request.GET.get('foodId', None)
        FoodItem.objects.get(foodId=foodId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class EditFoodItem(TemplateView):
    template_name = 'rest_app/editfooditem.html'
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
    template_name = 'rest_app/addstatus.html'
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
        return redirect('/StatusListVieww')


class StatusListView(ListView):
    model = FoodItemStatus
    template_name ="rest_app/viewstatus.html"

class DeleteStatus(View):
    def  get(self, request):
        statusId = request.GET.get('statusId', None)
        FoodItemStatus.objects.get(statusId=statusId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)



class EditStatus(TemplateView):
    template_name = 'rest_app/editstatus.html'
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

#########order##################
class addorder(TemplateView):
    template_name = 'rest_app/addorder.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blist=Branch.objects.all()
        rlist=Restaurant.objects.all()
        clist=Category.objects.all()
        flist=FoodItem.objects.all()
        # plist=FoodItem.objects.all()
        custlist=Customer.objects.all()

        context = {'custlist': list(custlist),'flist': list(flist),'clist':list(clist),'rlist':list(rlist),'blist':list(blist)}
        return context




class createorder(APIView):
    def post(self, request, *args, **kwargs):
        customer_id = request.POST.get('customer', '')

        fooditem_id = request.POST.get('food_item', '')
        
        quantity = request.POST.get('quantity', '')

        totalprice=float(request.POST.get('totalprice',0))


        ma=Order()
        ma.customer=Customer.objects.get(cId=customer_id)
        ma.food_item = FoodItem.objects.get(foodId=fooditem_id)
        ma.totalprice= totalprice
        ma.quantity= quantity
        
        ma.save()
        return redirect('/OrderListVieww')


class OrderListView(ListView):
    model = Order
    template_name ="rest_app/vieworder.html"

class DeleteOrder(View):
    def  get(self, request):
        orderId = request.GET.get('orderId', None)
        Order.objects.get(orderId=orderId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class EditOrder(TemplateView):
    template_name = 'rest_app/editorders.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blist = Branch.objects.all()
        rlist=Restaurant.objects.all()
        clist=Category.objects.all()
        flist=FoodItem.objects.all()
        slist =FoodItemStatus.objects.all()
        custlist=Customer.objects.all()


        try:
            olist =Order.objects.filter(orderId=kwargs['id'])
        except:
            olist =Order.objects.filter(orderId=context['id'])
        context = {'olist': list(olist),'custlist': list(custlist),'slist': list(slist),'flist': list(flist),'clist': list(clist),'rlist': list(rlist),'blist':list(blist)}
    
        return context
        

class UpdateOrder(APIView):


    def post(self, request):
       
        order_id = request.POST['orderId']
        food_item_id = request.POST['food_item']
        customer_id=request.POST['customer']
        quantity=request.POST['quantity']
        totalprice=float(request.POST['totalprice'])

        food_instance = get_object_or_404(FoodItem, foodId=food_item_id)
        cust_instance = get_object_or_404(Customer, cId=customer_id)
        
        order_instance = get_object_or_404(Order, orderId=order_id)
        order_instance.quantity=quantity
        order_instance.totalprice=totalprice
        order_instance.customer = cust_instance
        order_instance.food_item = food_instance
        order_instance.save()

        return JsonResponse({'success': True}, status=200)    

class KitchenListView(ListView):
    model = Order
    template_name ="rest_app/viewkitchen.html"


from django.shortcuts import render, redirect
from django.views.generic import ListView
from rest_app.models import Order


from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from rest_app.models import Order  # Import your actual model





from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# from .models import YourOrderModel  # Import your Order model

@csrf_exempt  # This decorator is used to exempt the view from CSRF protection for simplicity. In production, you should handle CSRF properly.
@require_POST
def update_kitchen_status(request):
    # Retrieve data from the POST request
    order_id = request.POST.get('orderId')
    kitchen_status = request.POST.get('kitchen_status')

    try:
        # Retrieve the order instance
        order = Order.objects.get(pk=order_id)

        # Update the payment status
        order.kitchen_status = kitchen_status
        order.save()

        # You can return additional data if needed
        response_data = {'success': True, 'message': 'Kitchen status updated successfully'}
    except Order.DoesNotExist:
        response_data = {'success': False, 'message': 'Order not found'}
    except Exception as e:
        response_data = {'success': False, 'message': str(e)}

    return JsonResponse(response_data)

from django.shortcuts import render, redirect
from rest_app.models import Order
from django.shortcuts import render, get_object_or_404, redirect
from rest_app.models import Order

def update_order(request, order_id):
    order = get_object_or_404(Order, orderId=order_id)
    if request.method == 'POST':
        order.payment_status = request.POST['payment_status']
        order.totalprice = request.POST['totalprice']
        order.save()
        return redirect('/PayListVieww')
    return render(request, 'rest_app/update_order.html', {'order': order})


def update_kitchen(request, order_id):
    orderr = get_object_or_404(Order, orderId=order_id)
    if request.method == 'POST':
        orderr.kitchen_status = request.POST['kitchen_status']

        orderr.save()
        return redirect('/KitchenListVieww')
    return render(request, 'rest_app/update_kitchen.html', {'orderr': orderr})
class addkitchen(APIView):
    def post(self, request,*args,**kwargs):
        kitchen_status = request.POST.get('kitchen_status')
        user=Order()
        user.kitchen_status=kitchen_status
    
        user.save()
        return redirect('/KitchenListVieww')
#########PAYMENT############
    # views.py

from django.shortcuts import render, redirect
from django.views.generic import ListView
from rest_app.models import Order


from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from rest_app.models import Order  # Import your actual model


class PaymentListView(ListView):
    model = Order
    template_name ="rest_app/viewpay.html"
#########PAYMENT############

class addpay(TemplateView):
    template_name = 'rest_app/addpay.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blist=Branch.objects.all()
        rlist=Restaurant.objects.all()
        clist=Category.objects.all()
        flist=FoodItem.objects.all()
        # olist=Order.objects.all()

        context = {'flist': list(flist),'clist':list(clist),'rlist':list(rlist),'blist':list(blist)}
        return context


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# from .models import YourOrderModel  # Import your Order model

@csrf_exempt  # This decorator is used to exempt the view from CSRF protection for simplicity. In production, you should handle CSRF properly.
@require_POST
def update_payment_status(request):
    # Retrieve data from the POST request
    order_id = request.POST.get('orderId')
    payment_status = request.POST.get('paymentStatus')

    try:
        # Retrieve the order instance
        order = Order.objects.get(pk=order_id)

        # Update the payment status
        order.payment_status = payment_status
        order.save()

        # You can return additional data if needed
        response_data = {'success': True, 'message': 'Payment status updated successfully'}
    except Order.DoesNotExist:
        response_data = {'success': False, 'message': 'Order not found'}
    except Exception as e:
        response_data = {'success': False, 'message': str(e)}

    return JsonResponse(response_data)



class PayListView(ListView):
    model =Order
    template_name ="rest_app/viewpay.html"
    context_object_name = 'orders'

# Customer###################
class addcustomer(TemplateView,APIView):
    template_name = "rest_app/addcustomer.html"
    def post(self, request):
        cId=request.POST.get('cId')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phnumber= request.POST.get('phnumber')


        if cId=="" or  name=="" or email=="":
            return JsonResponse({'status': "fail", 'reason': 'Name is mandatory'})
        else:
            user=Customer()
            user.cId=cId
            user.name=name
            user.email=email
            user.phnumber=phnumber
            user.save()
            return JsonResponse({'status': "Success"})


class CustomerListView(ListView):
    model = Customer
    template_name ="rest_app/customerlist.html"

class DeleteCustomer(View):
    def  get(self, request):
        cId = request.GET.get('cId', None)
        Customer.objects.get(cId=cId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    

class EditCustomer(TemplateView):
    template_name = 'rest_app/editcust.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['id'] = self.kwargs['id']
            custlist =Customer.objects.filter(cId=context['id'])
        except:
            custlist = Customer.objects.filter(cId=context['id'])
            
        context['custlist']= list(custlist)
        return context

class UpdateCustomer(APIView):
   
    def post(self, request):
    
        name = request.POST['name']
        email=request.POST['email']
        phnumber = request.POST['phnumber']
        
        cId = request.POST['cId']
       
        products=Customer.objects.get(cId=cId)
        products.name=name
        products.email=email
        products.phnumber=phnumber

       
        products.save()
        return JsonResponse({'success': True}, status=200)


#############################User
class adduser(TemplateView,APIView):
    template_name = "rest_app/adduser.html"
    def post(self, request):
        userId=request.POST.get('userId')
        uname = request.POST.get('name')
        email = request.POST.get('email')
        password=request.POST.get('password')
        contact_number= request.POST.get('contact_number')
        role= request.POST.get('role')
        if role=="" or  uname=="" or email=="" or password=="":
            return JsonResponse({'status': "fail", 'reason': 'Name is mandatory'})
        else:
            user=User()
            user.userId=userId
            user.name=uname
            user.email=email
            user.password=password
            user.contact_number=contact_number
            user.role=role
            user.save()
            return JsonResponse({'status': "Success"})
        
class UserListView(ListView):
    model = User
    template_name ="rest_app/userlist.html"

class DeleteUser(View):
    def  get(self, request):
        userId = request.GET.get('userId', None)
        User.objects.get(userId=userId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
class EditUser(TemplateView):
    template_name = 'rest_app/editusers.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['id'] = self.kwargs['id']
            ulist =User.objects.filter(userId=context['id'])
        except:
            ulist = User.objects.filter(userId=context['id'])
            
        context['ulist']= list(ulist)
        return context

class UpdateUser(APIView):
   
    def post(self, request):
     
   

        name = request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        contact_number = request.POST['contact_number']
        role=request.POST['role']
        
        
        userId = request.POST['userId']
       
        products=User.objects.get(userId=userId)
        products.name=name
        products.email=email
        products.password=password
        products.role=role
        products.contact_number=contact_number

       
        products.save()
        return JsonResponse({'success': True}, status=200)
    


class login_check(APIView,TemplateView):
    template_name = "login.html"

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)
        print(password)
        try:
            user = Register.objects.get(email=email, password=password)
            role = user.role
            print(role)

            if role in ['superadmin', 'admin', 'manager','restaurant','customer','kitchen']:
                request.session['user'] = email
                request.session['type'] = role

                return JsonResponse({'usertype': role, 'userdetails': email})
            else:
                request.session['user'] = "default"
                request.session['type'] = "default"

                return JsonResponse({'usertype': "default", 'userdetails': email})
        
        except Register.DoesNotExist:
            request.session['user'] = "default"
            request.session['type'] = "default"

            return JsonResponse({'usertype': "default", 'userdetails': {}})
        except Exception as e:
            print(e)  
            return JsonResponse({'usertype': "default", 'userdetails': {}})



class add(APIView,TemplateView):
    template_name="login.html"

    def post(self , request):
     
       
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        if email == '' or password == '':
            return JsonResponse({'status':"fail","reason":"email and pass mandatory"})
        else:
            user = Register()
         
            user.password = password
            user.email = email
            user.role = role
            user.save()
            return JsonResponse({'status':"Success"})

class viewusers(APIView):
    def post(self, request):
       
        print("im here")
        print(Register.objects.values())
        reglist = list(Register.objects.values())
        return JsonResponse({"reglist":reglist})



class SignInView(TemplateView):
    template_name = "login.html"

class SignUpView(APIView):
    def post(self, request):
        role = request.POST.get('role')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if role == "" or email == "" or password == "":
            return JsonResponse({'status': "fail", 'reason': 'Role, email, and password are mandatory'})

        if password != confirm_password:
            return JsonResponse({'status': "fail", 'reason': 'Password and confirm password must be the same'})
        else:

            user = Register()
            user.email = email
            user.password = password
            user.confirm_password = confirm_password
            user.role = role
            user.save()

            return JsonResponse({'status': "Success"})
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login_check')  


from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.http import JsonResponse

def forgot_password(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        email = request.POST.get('email')

        # Validate the email (you may add more validation)
        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=email)
        except user_model.DoesNotExist:
            return JsonResponse({'error': 'User with this email does not exist'}, status=404)

        # Generate a token for the password reset link
        token_generator = default_token_generator
        token = token_generator.make_token(user)

        # Send the password reset email
        reset_url = reverse('password_reset_confirm', args=[user.id, token])
        reset_url = request.build_absolute_uri(reset_url)

        subject = 'Password Reset'
        message = f'Click the following link to reset your password: {reset_url}'
        from_email = 'swathic6361@gmail.com'  # Update with your Gmail email
        to_email = [email]

        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return JsonResponse({'message': 'Password reset email sent successfully'})

    return render(request, 'login.html')



class changePassword(TemplateView):
    """
    Render feature map template
    """
    template_name = 'rest_app/changepassword.html'
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
