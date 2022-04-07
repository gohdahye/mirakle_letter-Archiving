

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import OrderForm
from .models import Order, OrderPayment


def home(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            payment = OrderPayment.from_order(order)

            return HttpResponseRedirect(reverse('payment:pay', args=[payment.pk]))
    else:
        form = OrderForm(initial={
            'name': '공원용 대관람차(배송비별도)',
            'amount': '100',
            'buyer': '고길동',
            'email': 'alchole@to.me',
            'tel': '1588-1588'
        })

    return render(request, 'home.html', {'form': form})


def retry_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    payment = OrderPayment.from_order(order)

    return HttpResponseRedirect(reverse('payment:pay', args=[payment.pk]))
