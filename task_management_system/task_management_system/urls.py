from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_api_auth(request):
    return redirect('/api-auth/login/?next=/api/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', redirect_to_api_auth),


]
