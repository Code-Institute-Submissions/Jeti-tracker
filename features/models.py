from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Feature(models.Model):

    WAITING = 'Waiting'
    INPROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    STATUS_CHOICES = ((WAITING, 'Waiting'),
                      (INPROGRESS, 'In Progress'), (COMPLETED, 'Completed'))

    name = models.CharField(max_length=50, blank=False)
    details = models.TextField(blank=False)
    username = models.ForeignKey(User, default=None)
    created_date = models.DateTimeField(blank=True, default=None, null=True)
    waiting_date = models.DateTimeField(blank=True, default=None, null=True)
    in_progress_date = models.DateTimeField(
        blank=True, default=None, null=True)
    completion_date = models.DateTimeField(blank=True, default=None, null=True)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    status = models.CharField(
        max_length=40, choices=STATUS_CHOICES, default=WAITING)

    def __str__(self):
        return self.name

class UpvoteFeature(models.Model):
    upvoted_feature = models.ForeignKey(Feature, default=None)
    user = models.ForeignKey(User, default=None)

    def __str__(self):
        return str(self.user)