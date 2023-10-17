from django.shortcuts import render
from blogs.models import Blogs

# Create your views here.
def panel(request):
    writer = "jojo"
    blogs = Blogs.objects.filter(writer=writer)
    return render(request, "backend/index.html", {
        "blogs":blogs,
        "writer":writer,
    })
