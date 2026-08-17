"""
定义 details_page 的 URL 模式
"""

from django.urls import path

from . import views

app_name = 'details_page'
urlpatterns = [
    #主页
    path('', views.index, name='index'),
]