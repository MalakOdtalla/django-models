from django.urls import path

from .views import Home, SnacksListView, SnacksDetailView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('list/', SnacksListView.as_view(), name="Snack_list"),
    path('detail/<int:pk>/', SnacksDetailView.as_view(), name='Snack_detail')
]