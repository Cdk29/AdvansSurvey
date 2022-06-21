import datetime

from django.db import models
from django.utils import timezone


class CVE(models.Model):
    CRITICITY_CODE = (
        ('F', 'Faible'),
        ('M', 'Moyen'),
        ('U', 'Urgent'),
    )
    STATUS_CODE = (
        ('N', 'Nouveau'),
        ('A', 'Archivé'),
    )
    cve_name = models.CharField(max_length=20)
    cve_summary = models.TextField(default="...")
    pub_date = models.DateTimeField('date published')
    cve_criticity = models.CharField(max_length=1, choices=CRITICITY_CODE)
    cve_status = models.CharField(max_length=1, choices=STATUS_CODE)

    def __str__(self):
        return self.cve_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
