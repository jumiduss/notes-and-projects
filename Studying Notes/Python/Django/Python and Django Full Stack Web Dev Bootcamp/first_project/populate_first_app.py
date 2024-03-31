import os
#Import the project settings before writing scripts
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
#Import django to initialize settings
django.setup()

from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        
        fake_lname = fakegen.last_name()
        fake_fname = fakegen.first_name()
        fake_email = fakegen.email()
        # create new webpage entry
        userRecord = User.objects.get_or_create(lname=fake_lname,fname=fake_fname,email=fake_email)[0]
        userRecord.save()
        
if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("population complete!")
