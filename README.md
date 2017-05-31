# geocoder

Code for using [geocode farm](http://geocode.farm) to locate addresses in NSW, Australia.

## requirements

Requires [geopy](https://github.com/geopy/geopy).

## usage
Set your API key in the environment variable GOOGLE_API_KEY, either run `export GOOGLE_API_KEY=yourkey` or create a file named `.env` that contains a line `GOOGLE_API_KEY=yourkey`

and then call the script, passing in input files as command line parameters: `
python geopy_geocodefarm_batch.py input.csv
`
