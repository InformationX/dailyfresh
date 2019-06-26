from django.shortcuts import render

# Create your views here.
from df_carts.models import CartInfo
from df_user import user_decorator


@user_decorator.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title':'购物车',
        'page_name':1,
        'carts':carts,
    }


    return render(request, 'df_carts/cart.html', context)