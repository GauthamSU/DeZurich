"""
URL configuration for lounge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("select2/", include("django_select2.urls")),
    # path('accounts/', include('allauth.urls')),
    path('', include('lounge_app_services.homepage.urls')),
    path('internal/', include('lounge_app_services.authentication.urls')),
    path('internal/', include('lounge_app_services.employee.urls')),
    path('internal/menu/', include('lounge_app_services.menu.urls')),
    path('internal/order/', include('lounge_app_services.create_track_orders.urls')),
    path('internal/workspace/', include('lounge_app_services.workspace.urls')),
    path('internal/management/', include('lounge_app_services.management_decisions.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)