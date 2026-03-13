from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from apps.core.models import Product


def create_order(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")

        Order.objects.create(
            product=product,
            name=name,
            phone=phone
        )

        return redirect("/")

    return render(request, "orders/order.html", {"product": product})