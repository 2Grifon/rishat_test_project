from django.conf import settings
from django.db.models import QuerySet
from django.views.generic.detail import DetailView
from rest_framework.generics import RetrieveAPIView, get_object_or_404

from apps.shop.models import Item
from apps.shop.serializers.item import BuyItemSerializer


class BuyItemView(RetrieveAPIView):
    """Позволяет купить товар, создавая сессию Stripe Session и возвращая её id"""

    serializer_class = BuyItemSerializer

    def get_queryset(self) -> QuerySet[Item]:
        return Item.objects.all()

    def get_object(self) -> Item:
        return get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])


class ItemDetailView(DetailView):
    """Рендерит HTML страницу с деталями товара и кнопкой для оплаты"""

    model = Item
    template_name = "shop/item_detail.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["publishable_key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context
