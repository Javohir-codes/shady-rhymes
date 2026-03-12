from django.shortcuts import render
from apps.comment.models import Comment

def home(request):
    comments = Comment.objects.all().order_by("-created_at")

    return render(request, "core/home.html", {
        "comments": comments
    })