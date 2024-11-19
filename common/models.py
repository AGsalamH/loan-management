'''
Database Models
'''
import uuid
from django.db import models


class BaseModel(models.Model):
    '''Timestamped Base Model for all database models.'''
    id = models.UUIDField(
                            verbose_name='ID',
                            primary_key=True,
                            serialize=False,
                            auto_created=True,
                            default=uuid.uuid4,
                            editable=False
                        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StatusChoices(models.TextChoices):
    AVAILABLE = 'AVAILABLE', 'Available'
    CLOSED = 'CLOSED', 'Closed'
    PENDING = 'PENDING', 'Pending'
    ACTIVE = 'ACTIVE', 'Active'
    COMPLETED = 'COMPLETED', 'Completed'
