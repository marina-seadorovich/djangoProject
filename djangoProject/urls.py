from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path(r'riddles/', include('riddles.urls')),
    path(r'admin/', admin.site.urls),
]
