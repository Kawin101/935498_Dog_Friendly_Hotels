from django.urls import path
from .views import index, blogDetail, searchCategory, searchWriter, searchAddress, googleMap, webScraping

urlpatterns = [
    path('', index),
    path('blog/<int:id>', blogDetail, name="blogDetail"),
    path('blog/category/<int:cat_id>', searchCategory, name="searchCategory"),
    path('blog/writer/<str:writer>', searchWriter, name="searchWriter"),
    path('searchAddress', searchAddress, name="searchAddress"),
    path('googleMap', googleMap, name="googleMap"),
    path('webScraping', webScraping, name="webScraping"),

]