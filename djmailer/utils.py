from django.core.mail import send_mass_mail


def send_email(campaign):
    messages = []
    for subscriber in campaign.email_list.subscribers.all():
        message = (campaign.subject, campaign.content, 'your_email@example.com', [subscriber.email])
        messages.append(message)
    send_mass_mail(messages, fail_silently=False)