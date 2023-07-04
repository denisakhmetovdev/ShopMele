from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    Отправка уведомления по электронной почте
    при успешном создании заказа.
    :param order_id: id заказа
    :return: send_mail object
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order.id}'
    message = f'Уважаемый {order.first_name},\n\n Ваш заказ успешно размещён. Номер Вашего заказа - {order.id}'
    mail_sent = send_mail(subject, message, 'admin@myshop.kz', [order.email])
    return mail_sent
