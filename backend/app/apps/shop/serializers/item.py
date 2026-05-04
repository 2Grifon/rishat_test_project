from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.shop.models.item import Item
from apps.shop.services.api_managers import stripe_api_manager


class BuyItemSerializer(ModelSerializer):
    session_id = SerializerMethodField()

    class Meta:
        model = Item
        fields = ("session_id",)

    def get_session_id(self, obj: Item) -> str:
        return stripe_api_manager.create_session(self.context["request"], obj)
