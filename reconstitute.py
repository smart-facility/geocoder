#!/usr/bin/env python3

import sys, csv

geocoded = csv.reader(open(sys.argv[2],'r'),delimiter='\t',quotechar='"')
original = csv.reader(open(sys.argv[1],'r'),delimiter='\t',quotechar='"')

lookup = dict()

for row in geocoded:
    lookup[row[0]] = row

for row in original:
    try:
        output = lookup[row[0]]
        for item in output:
            print(item,end='\t')
        print()
    except KeyError:
        print("address not found error", file=sys.stderr)
