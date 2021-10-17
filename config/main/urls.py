from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="restaurant-list"),
    path('add_restaurant_record', add_restaurant_record, name="add_restaurant_record"),
    path('update_item/<int:contact_id>/', update_item, name="update_item")
]
