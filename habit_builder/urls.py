"""habit_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

from fcm_django.api.rest_framework import FCMDeviceViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'devices', FCMDeviceViewSet)


urlpatterns = [
    path('', RedirectView.as_view(url='habit-app/home/')),
    path('habit-app/admin/', admin.site.urls),
    path('habit-app/', include('dashboard.urls')),
    path('habit-app/habit/', include('habit.urls')),
    path('firebase-messaging-sw.js',(TemplateView.as_view(
        template_name="firebase-messaging-sw.js",
        content_type='application/javascript',
    )), name='firebase-messaging-sw.js'),
    path('habit-app/api/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
