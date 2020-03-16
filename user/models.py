from django.db import models
from django.utils.timezone import now


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, unique=True, null=True, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    public_key = models.CharField(max_length=100, null=False, blank=False)
    date_created = models.DateTimeField(default=now)

    class Meta:
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['name'])
        ]
        db_table = 'ttp_users'

