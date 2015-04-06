from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Employee(models.Model):
   
    user                = models.OneToOneField(User)
    employee_code       = models.CharField(max_length=20)
    name                = models.CharField(max_length=100)
    qualification       = models.CharField(max_length=20)
    year_of_passing     = models.CharField(max_length=10, default='')
    doj                 = models.DateField(blank=True, null=True)
    dor                 = models.DateField(blank=True, null=True)
    designation         = models.CharField(max_length=100)
    client_name         = models.CharField(max_length=100)
    project_name        = models.CharField(max_length=100)
    father              = models.CharField(max_length=100)
    permanent_address   = models.CharField(max_length=1024)
    temporary_address   = models.CharField(max_length=1024)
    email_id            = models.EmailField()
    pan_no              = models.CharField(max_length=20)
    passport_no         = models.CharField(max_length=50)
    dob                 = models.DateField(blank=True, null=True)
    blood_group         = models.CharField(max_length=20)
    emergency_contact   = models.CharField(max_length=100)
    primary_contact     = models.CharField(max_length=100)
    secondary_contact   = models.CharField(max_length=100)
    reference           = models.CharField(max_length=100)
    msys_reference      = models.CharField(max_length=100)
    contact_no          = models.CharField(max_length=20)
    msys_email          = models.EmailField()
    employees_number    = models.CharField(max_length=20)
    emails              = models.EmailField()
    acount_no           = models.CharField(max_length=20)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = u'employee'

class Leave(models.Model):
    id              = models.BigIntegerField(primary_key=True)
    code            = models.CharField(max_length=20)
    name            = models.CharField(max_length=100)
    no_of_days      = models.IntegerField()
    ts              = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = u'leave'

class LeaveLedger(models.Model):
    id                  = models.BigIntegerField(primary_key=True)
    emp_code            = models.CharField(max_length=20)
    leave_code          = models.CharField(max_length=20)
    leave_summary       = models.TextField()
    from_date           = models.DateTimeField()
    to_date             = models.DateTimeField()
    status              = models.CharField(max_length=100)
    status_by           = models.CharField(max_length=100)
    status_remark       = models.TextField(max_length=100)
    ts                  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = u'leave_ledger'