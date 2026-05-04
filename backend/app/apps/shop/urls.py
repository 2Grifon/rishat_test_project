from django.urls import path

from apps.shop.views import BuyItemView, ItemDetailView, PaymentSuccessView

urlpatterns = [
    path("buy/<int:pk>/", BuyItemView.as_view(), name="buy-item"),
    path("item/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("success/", PaymentSuccessView.as_view(), name="payment-success"),
]
