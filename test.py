#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tools4msp_rba.settings.dev')
django.setup()
from rba.models import CSphase2
from tools4msp.models import Weight
def main():
    """Run administrative tasks."""
    
    p2 = CSphase2.objects.get(pk=1) 
    p2.table2()
    print (p2.table2())
    

if __name__ == '__main__':

    main()
