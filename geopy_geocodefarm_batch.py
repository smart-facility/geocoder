#!/usr/bin/env python

# Addresses with ranges, like 202-207 Princes Hwy, are unsupported.
# Keep only the first number in the range when preparing input.

import csv, time, sys, os
from geopy.geocoders import GoogleV3
#from getpass import getpass
from datetime import datetime

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_key = os.environ['GOOGLE_API_KEY']

#intialize geocoder to geocode addresses in only NSW, Australia (addresses will be interpolated to add NSW, Australia)
gc = GoogleV3(api_key)#,proxies={"http": "http://username:password@proxy.domain:8080"})

outstring = ""

for addressfile in sys.argv[1:]:
    with open(addressfile, "r") as inputfile:
        with open(addressfile[:-4]+"_output.csv", "w") as outputfile:
            for address in inputfile:
                outstring = address.rstrip()
                print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
                try:
                    location = gc.geocode(address+", NSW, Australia")
                    outstring = outstring + "\t" + str(location.latitude) + "\t" + str(location.longitude) + "\n"
                    outputfile.write(outstring)
                except:
                    print()
                    outstring = outstring + "\t" + "address couldn't be geolocated" + "\n"
                    outputfile.write(outstring)
                    print ("address couldn't be geolocated")
                print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
                #time.sleep(0.6)
                print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
                #set outstring to empty
                outstring = ""

        outputfile.close()
        inputfile.close()

print (" ")
print (" ")
print ("********************************")
print ("********************************")
print ("        job completed!")
print ("********************************")
print ("********************************")
print (" ")
