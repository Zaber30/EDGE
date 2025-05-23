from django.urls import path
from . import views
from .test import first
urlpatterns = [
    # path('admin/', admin.site.urls),
    #  path('',views.index,name='index'),
    #  path('play/', first.play,name='play'),
     path('bootstrap/',views.bootstrap,name='bootstrap'),
]