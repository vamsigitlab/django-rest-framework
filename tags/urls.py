from django.urls import path, include
from tags.views import CreateTagView, DetailTagView, ListTagView, DetailTagV2View, ListTagV2View, DeleteTagView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create_tag'),
    path('detail/<str:slug>/', DetailTagView.as_view(), name='detail_tag'),
    path('list/', ListTagView.as_view(), name='list_tag'),
    path('detail/v2/<str:slug>/', DetailTagV2View.as_view(), name='detail_tag'),
    path('list/v2/', ListTagV2View.as_view(), name='list_tag'),
    path('delete/<str:slug>/', DeleteTagView.as_view(), name='delete_tag'),

]
