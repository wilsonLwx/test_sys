"""test_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from inter_faces.views import InterfaceListViewSet

# 实例化router类
router = DefaultRouter()

router.register(r'interfaces', InterfaceListViewSet)

urlpatterns = [
    # 路由router下的url
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    # path('docs/', include_docs_urls(title='测试系统'))
]
