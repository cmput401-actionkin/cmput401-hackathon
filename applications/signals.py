# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from applications.models import Applications

@receiver(post_save, sender=Applications)
def create_notification_if_status_changed(sender, instance, **kwargs):
    print(55)
    if kwargs.get('created', False):
        # Skip creation if this is a new instance
        return

    # Check if the status has changed
    old_instance = Applications.objects.get(pk=instance.pk)
    if old_instance.status != instance.status:
        # Create a notification
        Notifications.objects.create(
            message=f'{instance.companyname} Application Status changed to {instance.status}'
        )
