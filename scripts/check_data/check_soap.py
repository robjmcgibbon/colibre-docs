#!/bin/env python
#
# Check what soap catalogues exist for each run
#

import numpy as np
import hdfstream
import simulation_list as sl

root = hdfstream.open("flamingo", "/FLAMINGO/")

for check in sl.sim_params:

    box = check["box"]
    names = check["names"]
    nr_snaps = check["nr_snaps"]
    all_snaps = np.arange(nr_snaps, dtype=int)
    expected_snaps = np.sort(np.asarray(list(check["expected_snaps"].keys()), dtype=int))

    for name in names:

        # Get directory name for this run
        dirname = name.replace("σ", "sigma").replace("*","star")
        print(dirname)

        # Try top open the SOAP dir
        nr_soaps = 0
        try:
            soap_dir = root[f"{box}/{dirname}/SOAP-HBT"]
        except KeyError:
            print(f"ALL MISSING")
        else:
            # Loop over snapshots
            for snap_nr in all_snaps:
                filename = f"halo_properties_{snap_nr:04d}.hdf5"
                if filename in soap_dir:
                    nr_soaps += 1
            if nr_soaps == nr_snaps:
                print(f"  Ok")
            else:
                print(f"  MISSING {nr_snaps-nr_soaps} SOAP outputs")
