from django.shortcuts import render, redirect
from .models import Comment, Product

def add_comment(request):
    if request.method == "POST":
        name = request.POST.get("name", "Anonymous")
        avatar = request.POST.get("avatar", "")
        text = request.POST.get("text")

        if text:
            Comment.objects.create(
                name=name,
                avatar=avatar,
                text=text
            )

        return redirect('home')

    return render(request, 'comment/add_comment.html')


def view_comments(request):
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'comment/view_comments.html', {
        'comments': comments
    })

def home(request):
    products = Product.objects.all()
    comments = Comment.objects.all().order_by('-created_at')

    context = {
        "products": products,
        "comments": comments
    }

    return render(request, "core/home.html", context)