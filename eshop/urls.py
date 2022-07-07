"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from store import views
from store.middleware.middleware import auth_middleware
from . import settings

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage,),
    path('', views.index,name="homepageq"),
    path('signup/',views.signup),
    path('login/',views.login,name='login'),
    path('logout/', views.logout),
    path('cart/', auth_middleware(views.cart),name="cart"),
    path('cart/check-out',views.check_out),
    path('order/',auth_middleware(views.order),name="order"),
    path('profile/',auth_middleware(views.profile),name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

