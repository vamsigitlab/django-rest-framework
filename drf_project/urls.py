from django.urls import path, include
from django.contrib import admin
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tags/', include('tags.urls')),
    path('authentication/', include('authentication.urls')),
]
