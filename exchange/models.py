from django.db import models
from django.utils.timezone import now

from user.models import User


class Document(models.Model):
    REQUESTED = 'requested'
    NOTIFIED = 'notified'
    SENDING = 'sending'
    COMPLETED = 'completed'

    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, to_field='user_id', related_name='receiver', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, to_field='user_id', related_name='sender', on_delete=models.CASCADE)
    doc = models.FileField(upload_to='docs', null=False, blank=False)
    sig_sender = models.CharField(max_length=100, null=False, blank=False)
    sig_receiver = models.CharField(max_length=100, null=True, blank=False)
    session_id = models.CharField(max_length=100, null=True, blank=False)
    date_created = models.DateTimeField(default=now)

    status = models.CharField(max_length=100, choices=[
        (REQUESTED, 'Requested'),
        (NOTIFIED, 'Notified'),
        (SENDING, 'Sending'),
        (COMPLETED, 'Completed'),
    ], default=REQUESTED)

    class Meta:
        db_table = 'ttp_document'
        indexes = [
            models.Index(fields=['session_id']),
        ]
