from django.db import models

# Email list Model 
class EmailList(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Subscriber(models.Model):
    email_list=models.ForeignKey(EmailList,related_name='subscribers',on_delete=models.CASCADE)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

class EmailCampaign(models.Model):
    subject=models.CharField(max_length=255)
    content=models.TextField()
    email_list=models.ForeignKey(EmailList,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.subject