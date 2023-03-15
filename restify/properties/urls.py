from django.urls import path
from .views import CreatePropertyView, UpdatePropertyView, DeletePropertyView, PropertyListView

app_name = "properties"

urlpatterns = [
    path('create/', CreatePropertyView.as_view(), name="create"),
    path('update/<int:pk>', UpdatePropertyView.as_view(), name="update"),
    path('delete/<int:pk>', DeletePropertyView.as_view(), name="delete"),
    path('view/', PropertyListView.as_view(), name='list'),
]