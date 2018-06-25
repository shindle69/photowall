from django.urls import path
from . import views

app_name ='blog'

urlpatterns = [   
   path('',views.index, name='index'),
   path('post_list/',views.post_list, name='post_list'),
   #path('','django.views.generic.simple.direct_to_template',{'template':'layout.html'},name='layout'),
   path('post_detail<int:pk>/',views.post_detail, name ="post_detail"),
  # path('',views.main, name='main'),
]
