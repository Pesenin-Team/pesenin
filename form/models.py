from django.db import models

# Create your models here.

class FeedbackForm(models.Model):
    
    CATEGORY = [
        ['FASILKOM', 'FASILKOM'],
        ['FK', 'FK'],
        ['FKG', 'FKG'],
        ['FT', 'FT'],
        ['FKM', 'FKM'],
        ['FARMASI', 'FARMASI'],
        ['FIK', 'FIK'],
        ['FMIPA', 'FMIPA'],
        ['FIB', 'FIB'],
        ['FISIP', 'FISIP'],
        ['FIA', 'FIA'],
        ['FEB', 'FEB'],
        ['FH', 'FH'],
        ['PSIKOLOGI', 'PSIKOLOGI'],
        ['VOKASI', 'VOKASI'],
    ]
    Faculty = models.CharField(
        max_length = 500,
        choices = CATEGORY)
    
    Satisfaction = models.IntegerField()

    Comment = models.CharField(max_length = 1000)

    def __str__(self):
        return ("{}.{}".format(self.id, self.Faculty))
