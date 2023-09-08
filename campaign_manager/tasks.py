from celery import shared_task
from django.core.mail import send_mail
from email_campaign_manager import settings
from .models import Subscribers, Campaigns
from django.template.loader import render_to_string
from datetime import date

@shared_task(bind=True)
def send_ad_mails(self):
  # Fetch the campaign based on campaign_id
  campaign = Campaigns.objects.filter(published_date=date.today()).first()

  if not campaign:
    print('No campaign found for today.')
    return

  # Fetch the list of subscribers for this campaign
  subscribers = Subscribers.objects.filter(is_active=True)

  # Render the base email template with campaign data
  email_content = render_to_string('base_template.html', {
      'subject': campaign.Subject,
      'preview_text': campaign.preview_text,
      'article_url': campaign.article_url,
      'content': campaign.html_content, 
      'published_date': campaign.published_date,
  })


  # Send the email to each subscriber
  for subscriber in subscribers:
      send_mail(
          subject=campaign.Subject,
          message=campaign.plain_text_content,
          from_email=settings.EMAIL_HOST_USER,
          recipient_list=[subscriber.email],
          html_message=email_content,
      )