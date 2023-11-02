from django.db import models
from Registration_Login.models import LogRegister_Details

# Create your models here.
class candidateDetails(models.Model):
    email= models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    Mobile_no=models.CharField(max_length=10)
    qualification=models.CharField(max_length=100)
    passout_year=models.CharField(max_length=10)
    college_name=models.CharField(max_length=100)
    location=models.CharField(max_length=300)
    expereince=models.CharField(max_length=15)
    previous_designation=models.CharField(max_length=255,null=True)
    previous_company=models.CharField(max_length=255,null=True)
    reason_for_registration=models.CharField(max_length=300)
    status=models.CharField(max_length=100)
    response=models.CharField(max_length=500,null=True)
    reason =models.CharField(max_length=500,null=True)
    data_added_date=models.DateField(auto_now_add=True,null=True)
    hr_id=models.ForeignKey(LogRegister_Details,on_delete=models.CASCADE,null=True)