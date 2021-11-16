from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index, name='index')
# ]

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('full_width', views.about, name='full_width'),
    path('contact', views.about, name='contact'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]
