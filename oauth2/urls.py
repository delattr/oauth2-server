from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('accounts/', include('users.urls')),
    re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
