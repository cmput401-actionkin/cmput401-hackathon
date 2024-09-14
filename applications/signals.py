# signals.py
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from notifications.models import Notifications
from applications.models import Applications

@receiver(pre_save, sender=Applications)
def create_notification_if_status_changed(sender, instance, **kwargs):
    if kwargs.get('created', False):
        # Skip creation if this is a new instance
        return

 
    # Check if the status has changed
    old_instance = Applications.objects.get(pk=instance.pk)
    print(old_instance.status)
    print(instance.status)
    if old_instance.status != instance.status:
        # Create a notification
        Notifications.objects.create(
            companyname = old_instance.companyname,
            position = old_instance.position,
            date_applied = old_instance.date_applied,
            status = instance.status,
            message=f'{instance.companyname} Application Status changed to {instance.status}'
        )

