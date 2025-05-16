from django.urls import path
from . import views
from .test import first
urlpatterns = [
    # path('admin/', admin.site.urls),
     path('',views.index,name='index'),
     # path('play/', first.render,name='render'),
     path('html2/',views.htmlpage, name='htmlpage'),

]