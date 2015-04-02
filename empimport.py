#!/home/karthik/.virtualenvs/hrms/bin/python
import os
import sys
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hrms.settings")

import django
django.setup()

from api.models import Employee
from django.contrib.auth.models import User

def main(args):
    #print args
    with open(args) as f:
        r = csv.reader(f)
        for data in r:
            print data[4]
            print data[5]
            print data[6]
            print data[7]
            print '#'*60
            #break
            u = User.objects.create_user(data[1], data[24], 'm$Y$'+data[1])
            e = Employee()
            e.user = u

            e.employee_code       = data[1]
            e.name                = data[2]
            e.qualification       = data[3]
            e.year_of_passing     = data[4]
            e.doj                 = data[5] if data[5] else None 
            e.dor                 = data[6] if data[6] else None
            e.designation         = data[7]
            e.client_name         = data[8]
            e.project_name        = data[9]
            e.father              = data[10]
            e.permanent_address   = data[11]
            e.temporary_address   = data[12]
            e.email_id            = data[13]
            e.pan_no              = data[14]
            e.passport_no         = data[15]
            e.dob                 = data[16]
            e.blood_group         = data[17]
            e.emergency_contact   = data[18]
            e.primary_contact     = data[19]
            e.secondary_contact   = data[20]
            e.reference           = data[21]
            e.msys_reference      = data[22]
            e.contact_no          = data[23]
            e.msys_email          = data[24]
            e.acount_no           = data[25]
            e.save()
            del(u)
            del(e)


if __name__ == "__main__":
    main(sys.argv[1])