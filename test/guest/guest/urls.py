from django.conf.urls import url
from django.contrib import admin
from sign import views       # 导入sign应用views文件

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/%S', views.index),   # 添加index/路径配置
]