import stripe


class StripeApiManager:  # TODO: взять базовый класс синглтона из проекта DFA и наследовать его
    def create_session(self, item) -> str:
        """
        Создаёт сессию Stripe Session и возвращает её id
        https://docs.stripe.com/api/checkout/sessions/create?architecture-style=resources
        """
        line_items: list[dict] = [self._create_line_item(item)]

        session = stripe.checkout.Session.create(
            line_items=line_items,
            mode="payment",
            success_url="http://localhost:3000/success",  # TODO: использовать рабочий URL
        )

        return session.id

    def _create_line_item(self, item) -> dict:
        """Создаёт словарь line item для Stripe Session на основе объекта Item"""
        return {
            "price_data": {
                "currency": item.currency.lower(),
                "unit_amount": item.price,
                "product_data": {
                    "name": item.name,
                    "description": item.description,
                },
            },
            "quantity": 1,
        }


stripe_api_manager = (
    StripeApiManager()
)  # REVIEW: Не уверен что это лучшее решение, но пусть пока будет так
