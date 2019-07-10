from django.urls import path, re_path, include
from .views import RegisterUser


urlpatterns = [

 path('', include('django.contrib.auth.urls')),
 path('signup/', RegisterUser.as_view(), name='signup'),
 re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]