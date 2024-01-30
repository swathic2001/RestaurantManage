from django.shortcuts import get_object_or_404, render,redirect
from django.http import JsonResponse
from django.views import View
from rest_app.models import Order
from rest_app.models import Branch,User,Customer,Restaurant,Category,FoodItem,FoodItemStatus,Order,Register

from django.views.generic import TemplateView,ListView
from rest_framework.views import APIView
from django.shortcuts import render

# Create your views here.



def HomeView(request):
    order_count =Order.objects.count()
  

 




    context = {
        'order_count': order_count,
       
        

    }
 
    return render(request,'kitchen_app/index.html', context)
class KitchenListView(ListView):
    model = Order
    template_name ="kitchen_app/viewkitchen.html"

from django.shortcuts import render, redirect
from django.views.generic import ListView
from rest_app.models import Order


from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from rest_app.models import Order  # Import your actual model




class addkitchen(TemplateView):
    template_name = 'kitchen_app/addkitchen.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blist=Branch.objects.all()
        rlist=Restaurant.objects.all()
        clist=Category.objects.all()
        flist=FoodItem.objects.all()
        # olist=Order.objects.all()

        context = {'flist': list(flist),'clist':list(clist),'rlist':list(rlist),'blist':list(blist)}
        return context



from django.shortcuts import render, redirect
from rest_app.models import Order
from django.shortcuts import render, get_object_or_404, redirect
from rest_app.models import Order



def update_kitchenn(request, order_id):
    orderr = get_object_or_404(Order, orderId=order_id)
    if request.method == 'POST':
        orderr.kitchen_status = request.POST['kitchen_status']

        orderr.save()
        return redirect('KitchenListView')
    return render(request, 'kitchen_app/update_kitchen.html', {'orderr': orderr})
class addkitchen(APIView):
    def post(self, request,*args,**kwargs):
        kitchen_status = request.POST.get('kitchen_status')
        user=Order()
        user.kitchen_status=kitchen_status
    
        user.save()
        return redirect('KitchenListView')

def update_kitchen_status(request, order_id):
    orderr = get_object_or_404(Order, orderId=order_id)
    if request.method == 'POST':
        orderr.kitchen_status = request.POST['kitchen_status']

        orderr.save()
        return redirect('KitchenListView')
    return render(request, 'kitchen_app/update_kitchen.html', {'orderr': orderr})
class changePassword(TemplateView):
    """
    Render feature map template
    """
    template_name = 'kitchen_app/changepassword.html'
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