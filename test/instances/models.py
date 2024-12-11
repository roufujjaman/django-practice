from django.db import models


PROFESSION = {
    "ARC": "Architect",
    "ENG": "Engineer",
    "ART": "Artist",
    "LAW": "Lawyer",
    "DOC": "Doctor",
    "TCH": "Teacher"
}

class TestInstance(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    profession = models.CharField(max_length=3, choices=PROFESSION)
    
