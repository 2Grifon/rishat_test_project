from django.urls import path

from apps.shop.views import BuyItemView

urlpatterns = [
    path("buy/<int:pk>/", BuyItemView.as_view(), name="buy-item"),
]
