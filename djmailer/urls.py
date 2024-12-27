from django.urls import path,include
from . import views as view

urlpatterns = [
   path('',view.index,name='index'),
   path ('login/',view.user_login,name='login'),
   path('register/',view.register,name='register'),
   path('email_lists/',view.email_list,name='email_list'),
   path('create-email-list/',view.create_email_list,name='create_email_list'),
   path('add_subscriber/',view.add_subscriber,name='add_subscriber'),
   path('campaign_list/',view.campaign_list,name='campaign_list'),
   path('create-campaign/',view.create_campaign,name='create_campaign'),
   path('campaigns/<int:campaign_id>/', view.campaign_detail, name='campaign_detail'),
   path('send-campaign/<int:campaign_id>/', view.send_campaign, name='send_campaign'),
]
