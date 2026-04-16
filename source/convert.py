#!/bin/env python

import sys
import pandoc

infile = sys.argv[1]
outfile = sys.argv[2]

doc = pandoc.read(infile)
pandoc.write(doc, outfile)
