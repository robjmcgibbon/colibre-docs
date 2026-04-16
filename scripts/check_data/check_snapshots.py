#!/bin/env python
#
# Check what snapshots exist for each run
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

        dirname = name.replace("σ", "sigma").replace("*","star")
        print(dirname)

        try:
            snapshots_dir = root[f"{box}/{dirname}/snapshots"]
        except KeyError:
            print("  Directory not found")
            continue

        # Check which snapshots we have
        snaps_present = []
        for snap_nr in range(nr_snaps):
            filename = f"flamingo_{snap_nr:04d}/flamingo_{snap_nr:04d}.0.hdf5"
            try:
                snap_file = snapshots_dir[filename]
            except KeyError:
                pass
            else:
                snaps_present.append(snap_nr)

        snaps_found = np.sort(np.asarray(snaps_present))
        if (len(snaps_found) == len(all_snaps)) and np.all(snaps_found==all_snaps):
            print("  All snapshots present")
        elif (len(snaps_found) == len(expected_snaps)) and np.all(snaps_found==expected_snaps):
            print("  Expected subset of snapshots present")
        else:
            missing = 0
            for sn in expected_snaps:
                if sn not in snaps_found:
                    missing += 1
            if missing == 0:
                print("  Have extra snapshots")
            else:
                print("  MISSING SNAPSHOTS")
