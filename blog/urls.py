from django.urls import include, path
from . import views

#Always assigning app_name for scalability, keeping it clean and avoiding miss-referencing
app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]