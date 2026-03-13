from django.shortcuts import render
from .models import Product
from apps.comment.models import Comment


def home(request):

    products = Product.objects.all()[:4]

    comments = Comment.objects.all().order_by("-created_at")[:4]

    context = {
        "products": products,
        "comments": comments
    }

    return render(request, "core/home.html", context)