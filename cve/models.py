import datetime

from django.db import models
from django.utils import timezone
from djongo import models


class CVE(models.Model):

    cve_name = models.CharField(max_length=20)
    summary = models.TextField(default="...")
    pub_date = models.DateTimeField('date published')
    cvss = models.TextField(default="...")
    # cve_criticity = models.CharField(max_length=1, choices=CRITICITY_CODE)
    cve_status = models.TextField(default="...")
    _id = models.TextField(default="...") #https://stackoverflow.com/questions/66085516/pymongo-errors-duplicatekeyerror-e11000-duplicate-key-error-collection
    
    def __str__(self):
        return self.cve_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
