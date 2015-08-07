# geocoder

Code for using [geocode farm](http://geocode.farm) to locate addresses in NSW, Australia.

## requirements

Requires [geopy](https://github.com/geopy/geopy).

## usage
Set your API key in the environment variable GEOCODEFARM_API_KEY, and then call the script, passing in input files as command line parameters:
```shell
export GEOCODEFARM_API_KEY=yourkey
python geopy_geocodefarm_batch.py input.csv
```
