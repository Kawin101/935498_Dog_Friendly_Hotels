from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import Blogs
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def index(request):
    categories = Category.objects.all()
    blogs = Blogs.objects.all()
    # if .order_by('pk') = 1,2,3,4
    # '-pk' = 4,3,2,1
    # [:2] แสดง 2 บทความล่าสุด
    latest = Blogs.objects.all().order_by('-pk')[:4]

    # บทความยอดนิยม
    # 'views' = 1,2,3,4
    # '-views' = 4,3,2,1
    # [:3] แสดง 3 ตัวแรก
    popular = Blogs.objects.all().order_by('-views')[:3]

    # บทความแนะนำ
    suggestion = Blogs.objects.all().order_by('views')[:3]

    # Pagination
    paginator = Paginator(blogs,4)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    
    try:
        blogPerpage = paginator.page(page)
    except (EmptyPage, InvalidPage):
        blogPerpage = paginator.page(paginator.num_pages)

    return render(request, "frontend/index.html", {
        'categories': categories,
        'blogs': blogPerpage,
        'latest': latest,
        'popular': popular,
        'suggestion': suggestion,
        })

def blogDetail(request, id):
    categories = Category.objects.all()
    # บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    # บทความแนะนำ
    suggestion = Blogs.objects.all().order_by('views')[:3]

    singleBlog = Blogs.objects.get(id = id)
    singleBlog.views = singleBlog.views+1
    singleBlog.save()
    return render(request, "frontend/blogDetail.html", {
        "blog":singleBlog,
        'categories': categories,
        'popular': popular,
        'suggestion': suggestion,
        })

def searchCategory(request, cat_id):
    blogs = Blogs.objects.filter(category_id = cat_id)
    # บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    # บทความแนะนำ
    suggestion = Blogs.objects.all().order_by('views')[:3]
    categoryName = Category.objects.get(id=cat_id)
    categories = Category.objects.all()
    return render(request, "frontend/searchCategory.html", {
        "blogs": blogs,
        'categories': categories,
        'popular': popular,
        'suggestion': suggestion,
        'categoryName': categoryName,
        })

def searchWriter(request, writer):
    blogs = Blogs.objects.filter(writer = writer)
    categories = Category.objects.all()
    suggestion = Blogs.objects.all().order_by('views')[:3]
    popular = Blogs.objects.all().order_by('-views')[:3]

    return render(request,"frontend/searchWriter.html", {
        "blogs": blogs,
        'categories': categories,
        'popular': popular,
        'suggestion': suggestion,
        'writer': writer,
    })

def searchAddress(request):
    return render(request,"frontend\searchAddress.html")

def googleMap(request):
    return render(request,"frontend\googleMap.html")

def webScraping(request):
    return render(request,"frontend\webScraping.html")