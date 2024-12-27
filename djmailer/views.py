from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomAuthenticationForm,CustomUserCreationForm,EmailListForm,SubscriberForm,EmailCampaignForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import EmailList,EmailCampaign
from django.contrib.auth.decorators import login_required
from .utils import send_email

# Create your views here.
def index(request):
    return render(request,'djmailer/index.html')

# Login View 
def user_login(request):
    if request.method == 'POST':
        form=CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.error(request,'Invalid username or password')
        else:
            messages.error(request,'Invalid username or password')
    else:
        form=CustomAuthenticationForm()
    return render(request,'djmailer/login.html',{'form':form})


# Register View

def register(request):
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
           form.save()
           username=form.cleaned_data.get('username')
           password=form.cleaned_data.get('password1')
           messages.success(request,f'Account created for {username}')
           return redirect('login')
    else:
        form=CustomUserCreationForm()
    return render(request,'djmailer/register.html',{'form':form})
        
# Email List 
@login_required
def email_list(request):
    email_list=EmailList.objects.all()
    return render(request,'djmailer/email_list.html',{'email_list':email_list})

# Add Email List View 

@login_required
def create_email_list(request):
    if request.method == 'POST':
        form = EmailListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('email_list')
    else:
        form = EmailListForm()
    return render(request, 'djmailer/create_email_list.html', {'form': form})


# Add Subscriber View 
@login_required
def add_subscriber(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('email_list')
    else:
        form = SubscriberForm()
    return render(request, 'djmailer/add_subscriber.html', {'form': form})
    
    

# EmailCampaign view 
@login_required
def campaign_list(request):
    campaign_list=EmailCampaign.objects.all()
    return render(request,'djmailer/campaign_list.html',{'campaign_list':campaign_list})


#  EmailCampaign Detail 

@login_required
def campaign_detail(request,campaign_id):
    campaign=get_object_or_404(EmailCampaign,id=campaign_id)
    return render(request,'djmailer/campaign_detail.html',{'campaign':campaign})


# Add EmailCampaign

@login_required
def create_campaign(request):
    if request.method=='POST':
        form=EmailCampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campaign_list')
    else:
        form=EmailCampaignForm()
    return render(request,'djmailer/create_campaign.html',{'form':form})



# Send Email 
@login_required
def send_campaign(request,campaign_id):
    campaign=get_object_or_404(EmailCampaign,id=campaign_id)
    send_email(campaign)
    context={
        'campaign':campaign
    }
    return render (request,'djmailer/done.html',context)