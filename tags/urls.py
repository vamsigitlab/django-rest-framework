from django.urls import path, include
from tags.views import CreateTagView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create_tag'),
]
