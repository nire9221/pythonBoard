from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('itBoardApp/', include('itBoardApp.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
