from django.shortcuts import render, redirect
from .models import Comment


def add_comment(request):

    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")
        avatar = request.POST.get("avatar")

        Comment.objects.create(
            name=name,
            text=text,
            avatar=avatar
        )

        return redirect("/")

    return render(request, "comment/add_comment.html")


def feedback(request):

    comments = Comment.objects.all().order_by("-created_at")

    return render(request, "comment/feedback.html", {
        "comments": comments
    })