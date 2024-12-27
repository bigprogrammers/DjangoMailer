from django.contrib import admin
from.models import EmailList, Subscriber,EmailCampaign

admin.site.register(EmailList)
admin.site.register(Subscriber)
admin.site.register(EmailCampaign)