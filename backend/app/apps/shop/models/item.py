from django.db.models import Model, CharField, PositiveIntegerField, TextField


class Item(Model):
    name = CharField(max_length=255)
    description = TextField()
    price = PositiveIntegerField(
        help_text="Цена в наименьших единицах валюты (копейки, центы и т.д.)"
    )
    currency = CharField(max_length=3, default="usd")  # Сделать через choices?

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
