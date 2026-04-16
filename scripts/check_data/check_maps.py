#!/bin/env python
#
# Check what healpix maps exist for each run
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

        # Loop over expected healpix map dirs
        for map_dir_name in ("healpix_maps/nside_16384",
                             "healpix_maps/nside_4096"):

            # Check the directory exists
            try:
                map_dir = root[f"{box}/{dirname}/{map_dir_name}"]
            except KeyError:
                print(f"  Directory {map_dir_name} not found")
                continue

            # Check how many lightcones we have
            nr_lightcones = 0
            nr_shells = []
            for basename in map_dir.directories:
                if basename.startswith("lightcone"):
                    # Count shells in this lightcone
                    nr_shells = len(map_dir[basename].files)
                    print(f"  {map_dir_name}: {basename} has {nr_shells} shells")
                    nr_lightcones += 1
