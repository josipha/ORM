from django.db import models
from django.contrib import admin
class loan (models.Model):
    loan_id=models.IntegerField(primary_key=True)
    loan_type=models.CharField(max_length=30)
    loan_amnt=models.FloatField()
    customer_acntno=models.IntegerField()
    cust_name=models.CharField(max_length=50)
 
class loanADMIN(admin.ModelAdmin):
    list_display=('loan_id','loan_type','loan_amnt','customer_acntno','cust_name')
# Create your models here.
