#!/bin/env python

import os.path
import numpy as np
from table import rst_grid_table

simdir = "/cosma8/data/dp004/flamingo/Runs/L1000N1800/HYDRO_PLANCK/"
#simdir = "/cosma8/data/dp004/flamingo/Runs/L1000N3600/HYDRO_FIDUCIAL/"

columns =("Snapshot number", "Redshift", "Available for all models")

# Read snapshot redshifts
with open(f"{simdir}/output_list.txt","r") as infile:
    zlist = [float(line) for line in infile.readlines() if not line.startswith("#")]

# Write the table
rows = []
for i, z in enumerate(zlist):

    snapdir = f"{simdir}/snapshots/flamingo_{i:04d}"
    if os.path.isdir(snapdir):
        available = "Y"
    else:
        available = ""
    rows.append([f"{i}", f"{z:.2f}", available])

print(rst_grid_table(columns, rows))
