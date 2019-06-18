from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('datingmap/', include('datingmap.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/datingmap/')),
]
