"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Files.views import files_view
from Users.views import profile_view, pin_item_view, delete_pin_view, home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('files/', files_view, name='files'),
    path('pins/', profile_view, name='pins'),
    path('pin-item/<int:id>/', pin_item_view, name='pin-item'),
    path('pin-delete/<int:id>/', delete_pin_view, name='pin-delete'),
    path('', home_view, name='home'),
    path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
