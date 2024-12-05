from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('item/', views.ItemClassView.as_view() , name= 'item'),
    path('<int:pk>/', views.ItemDetails.as_view(), name = "details"),
    path('add_items/', views.AddItemView.as_view(), name="add_items"),
    path('update_items/<int:item_id>/', views.update_items, name="update_items"),
    path('delete_item/<int:id>/', views.delete_items, name='delete_item'),  # Ensure the name is 'delete_item'
]