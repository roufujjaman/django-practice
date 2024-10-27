from django.db import models

PROJECT_CURRENT_STATUS = [
    ("IP", "In Progress"),
    ("OH", "On Hold"),
    ("HC", "Hold By Client"),
    ("HO", "Hold By Office"),
    ("BI", "Billing Issue")
]
# Create your models here.
class Projects(models.Model):
    # client 
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    current_phase = models.CharField(max_length=100) # foreign key later
    current_sub_phase = models.CharField(max_length=100) # foreign key later
    current_status = models.CharField(max_length=2, choices=PROJECT_CURRENT_STATUS)


class Phases(models.Model):
    title = models.CharField(max_length=50)

# idea 
# flags for all services for example fire drawing, plumbing, structure
# the flag will represent whether currrent phase requires above consultant and it it updated and chekek by them