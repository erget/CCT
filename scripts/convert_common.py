#!/usr/bin/env python

import sys
import string
import csv
import re
import os


dirname = sys.argv[1]
for infilename in os.listdir(dirname):
    if infilename.endswith(".txt") and infilename.startswith("Common"):
        outfilename=infilename[7:10]+'.csv'
        with open(dirname + '/' + infilename, encoding = 'utf-8') as csvFile:
            csvReader = csv.reader(csvFile, delimiter = ',', quotechar='"')
            outfile = open(outfilename, 'w', encoding='utf-8', newline='')
            outfilewriter = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

            for row in csvReader:
                outfilewriter.writerow(row[1:])

            outfile.close()
