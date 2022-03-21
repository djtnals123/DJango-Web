from apps.account.models import MyUser
from apps.board.validators import max_file_size
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class Board(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='writer')
    attachment = models.FileField(validators=[max_file_size], null=True, blank=True)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


@receiver(post_delete, sender=Board)
def file_delete_action(sender, instance, **kwargs):
    instance.attachment.delete(False)


@receiver(pre_save, sender=Board)
def pre_save_attachment(sender, instance, *args, **kwargs):
    """ instance old attachment file will delete from os """
    try:
        old_attachment = instance.__class__.objects.get(id=instance.id).attachment.path
        try:
            new_attachment = instance.attachment.path
        except:
            new_attachment = None
        if new_attachment != old_attachment:
            import os
            if os.path.exists(old_attachment):
                os.remove(old_attachment)
    except:
        pass
