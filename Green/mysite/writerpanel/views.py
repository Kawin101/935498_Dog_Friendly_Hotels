from django.shortcuts import render
from blogs.models import Blogs
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="member")
def panel(request):
    writer = "jojo"
    blogs = Blogs.objects.filter(writer=writer)
    blogCount = blogs.count()
    total = Blogs.objects.filter(writer=writer).aggregate(Sum("views"))

    return render(request, "backend/index.html", {
        "blogs":blogs,
        "writer":writer,
        "blogCount":blogCount,
        "total":total,
    })
