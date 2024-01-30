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
  
    customer_count = Customer.objects.count()
    category_count = Category.objects.count()
    fooditem_count = FoodItem.objects.count()




    context = {
        'order_count': order_count,
       
        'customer_count':  customer_count,
        # 'user_count':  user_count,

    }
 
    return render(request,'manager/index.html', context)


class addorder(TemplateView):
    template_name = 'manager/addorder.html'
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
        return redirect('OrderListViews')


class OrderListView(ListView):
    model = Order
    template_name ="manager/vieworder.html"

    

class DeleteOrder(View):
    def  get(self, request):
        orderId = request.GET.get('orderId', None)
        Order.objects.get(orderId=orderId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class EditOrder(TemplateView):
    template_name = 'manager/editorders.html'
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





class PaymentListView(ListView):
    model = Order
    template_name ="manager/viewpay.html"
#########PAYMENT############

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
        return redirect('PaymentListView')
    return render(request, 'manager/update_order.html', {'order': order})










# Customer###################
class addcustomer(TemplateView,APIView):
    template_name = "manager/addcustomer.html"
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
    template_name ="manager/customerlist.html"

class DeleteCustomer(View):
    def  get(self, request):
        cId = request.GET.get('cId', None)
        Customer.objects.get(cId=cId).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    

class EditCustomer(TemplateView):
    template_name = 'manager/editcust.html'
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




class changePassword(TemplateView):
    """
    Render feature map template
    """
    template_name = 'manager/changepassword.html'
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






