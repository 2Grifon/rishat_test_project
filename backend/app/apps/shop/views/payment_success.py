from django.views.generic.base import TemplateView


class PaymentSuccessView(TemplateView):
    """HTML страница с сообщением об успешной оплате"""

    template_name = "shop/payment_success.html"
