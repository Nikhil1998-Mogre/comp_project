from django.db import models
import pandas as pd

# Create your models here.


# # # Create your models here.
class Job(models.Model):
    Company = models.TextField(max_length=500, null = True)
    Location = models.TextField(max_length=500, null =True)
    JD = models.TextField(max_length=20000, null = True)
    posted = models.TextField(max_length=500, null = True)
    job_role = models.TextField(max_length=500, null = True)

    # link = models.TextField(max_length=10000, null = True)


   