"""
URL configuration for config project.

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
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from review.views import toggle_like
from django.conf import settings
from django.conf.urls.static import static

import notifications.urls

schema_view = get_schema_view(
    openapi.Info(
        title="Python 23 API",
        description="makers bootcamp",
        default_version="v1",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui("swagger")),
    path('api/v1/', include("account.urls")),
    path('api/v1/', include("review.urls")),
    path('api/v1/', include("post.urls")),
    path('', include('chat.urls')),
    re_path('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]