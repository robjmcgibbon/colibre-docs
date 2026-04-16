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

        # Check for virtual snapshot with membership
        found = []
        for snap_nr in all_snaps:
            filename = f"{box}/{dirname}/SOAP-HBT/flamingo_{snap_nr:04d}.hdf5"
            try:
                snap = root[filename]
            except KeyError:
                pass
            else:
                found.append(snap_nr)

        missing = 0
        for snap_nr in expected_snaps:
            if snap_nr not in found:
                missing += 1
        print(f"  Virtual snaps total: {len(found)}, missing: {missing}")

        # Check for membership data files
        found = []
        for snap_nr in all_snaps:
            filename = f"{box}/{dirname}/SOAP-HBT/membership_{snap_nr:04d}/membership_{snap_nr:04d}.0.hdf5"
            try:
                snap = root[filename]
            except KeyError:
                pass
            else:
                found.append(snap_nr)
        missing = 0
        for snap_nr in expected_snaps:
            if snap_nr not in found:
                missing += 1
        print(f"  Membership snaps total: {len(found)}, missing: {missing}")
