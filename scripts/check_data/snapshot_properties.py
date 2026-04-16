#!/bin/env python
#
# Make rst tables of particle properties
#

import h5py
from table import rst_grid_table


# Table column names
columns = ("Name", "Type", "Dimensions", "Description")

# Open a snapshot file
filename = "/cosma8/data/dp004/flamingo/Runs/L1000N1800/HYDRO_FIDUCIAL/snapshots/flamingo_0077/flamingo_0077.0.hdf5"
snap = h5py.File(filename, "r")

# Loop over particle types
for ptype in (0, 1, 4, 5, 6):

    # Open the group for this type
    group = snap[f"PartType{ptype}"]

    # List of table rows
    rows = []

    # Generate table rows
    for name in group:
        dset = group[name]
        rows.append([
            name,
            str(dset.dtype),
            ",".join(["N",]+[str(s) for s in dset.shape[1:]]),
            dset.attrs["Description"].decode()
        ])

    print(rst_grid_table(columns, rows))
