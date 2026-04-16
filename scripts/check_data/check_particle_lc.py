#!/bin/env python
#
# Check what particle lightcone outputs exist for each run
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

        # Open the particle lightcone directory, if there is one
        try:
            lc_dir = root[f"{box}/{dirname}/particle_lightcones"]
        except KeyError:
            print(f"  Directory particle_lightcones not found")
            continue

        # Check how many lightcones we have
        nr_lightcones = 0
        for basename in lc_dir.directories:
            if basename.startswith("lightcone"):
                nr_lightcones += 1

        # For each lightcone, check what particle types we have
        particle_types = {}
        for lightcone_nr in range(8):
            particle_types[lightcone_nr] = []
            filename = f"lightcone{lightcone_nr}_particles/lightcone{lightcone_nr}_0000.0.hdf5"
            if filename in lc_dir:
                lc_file = lc_dir[filename]
                for name in lc_file["Cells"]:
                    particle_types[lightcone_nr].append(name)
                print(f"  {lightcone_nr} : ", particle_types[lightcone_nr])
