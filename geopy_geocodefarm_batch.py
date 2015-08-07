#!/usr/bin/env python

# Addresses with ranges, like 202-207 Princes Hwy, are unsupported. 
# Keep only the first number in the range when preparing input.

import csv, time, sys
from geopy.geocoders import GeocodeFarm
#from getpass import getpass

#user = input("Enter uow proxy usename: ")
#pw = getpass('Enter uow proxy password: ')
api_key = sys.argv[1]

#intialize geocoder to geocode addresses in only NSW, Australia (addresses will be interpolated to add NSW, Australia)
gc = GeocodeFarm(api_key,"%s, NSW, Australia",1)#,proxies={"http": "http://username:password@proxy.domain:8080"})

outstring = ""

for addressfile in sys.argv[2:]:
    with open(addressfile, "r") as f:
        reader = csv.reader(f)
        with open(addressfile[:-4]+"_output.csv", "w") as output:
            for row in reader:
                address = ",".join(row)
                print (address)
                outstring = outstring + address
                try:
                    place, (lat, lng) = gc.geocode(address)
                    outstring = outstring + "\t" + str(lat) + "\t" + str(lng) + "\n"
                    output.write(outstring)
                    print (place,lat,lng)
                except:
                    outstring = outstring + "\t" + "address couldn't be geolocated" + "\n"
                    output.write(outstring)
                    print ("address couldn't be geolocaed")

                #set outstring to empty
                outstring = ""
                time.sleep(1/6.94) # rate limit
        output.close()
        f.close()

print (" ")
print (" ")
print ("********************************")
print ("********************************")
print ("        job completed!")
print ("********************************")
print ("********************************")
print (" ")
