#!/usr/bin/env python

# Addresses with ranges, like 202-207 Princes Hwy, are unsupported.
# Keep only the first number in the range when preparing input.

import csv, time, sys, os
from geopy.geocoders import GeocodeFarm
#from getpass import getpass
import datetime

#user = input("Enter uow proxy usename: ")
#pw = getpass('Enter uow proxy password: ')
api_key = os.environ['GEOCODEFARM_API_KEY']

#intialize geocoder to geocode addresses in only NSW, Australia (addresses will be interpolated to add NSW, Australia)
gc = GeocodeFarm(api_key,"%s, NSW, Australia",1)#,proxies={"http": "http://username:password@proxy.domain:8080"})

outstring = ""

for addressfile in sys.argv[1:]:
    with open(addressfile, "r") as inputfile:
        with open(addressfile[:-4]+"_output.csv", "w") as outputfile:
            for address in inputfile:
                outstring = address.rstrip()
                print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                try:
                    location = gc.geocode(address)
                    outstring = outstring + "\t" + str(location.latitude) + "\t" + str(location.longitude) + "\t" + location.raw["accuracy"] + "\n"
                    outputfile.write(outstring)
                except:
                    outstring = outstring + "\t" + "address couldn't be geolocated" + "\n"
                    outputfile.write(outstring)
                    print ("address couldn't be geolocated")
                print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                time.sleep(0.3)
                print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
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
