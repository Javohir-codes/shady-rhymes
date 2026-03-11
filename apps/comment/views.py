from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from apps.core.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(user=request.user, product=product, content=content)
        return redirect('product_detail', slug=product.slug)
    
    context = {
        'product': product
    }
    return render(request, 'comment/add_comment.html', context)


def product_comments(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = Comment.objects.filter(product=product, is_active=True)
    
    context = {
        'product': product,
        'comments': comments
    }
    return render(request, 'comment/product_comments.html', context)