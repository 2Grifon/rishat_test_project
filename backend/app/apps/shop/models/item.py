from django.db.models import Model, CharField, PositiveIntegerField, TextChoices, TextField


class Item(Model):
    class CurrencyChoices(TextChoices):
        USD = "usd", "USD"
        RUB = "rub", "RUB"

    name = CharField(max_length=255)
    description = TextField()
    price = PositiveIntegerField(
        help_text="Цена в наименьших единицах валюты (копейки, центы и т.д.)"
    )
    currency = CharField(choices=CurrencyChoices.choices, max_length=3, default="usd")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
