#!/bin/env python
#
# Check that postprocessed maps are present
#

import sys
import os.path
import yaml
import numpy as np
import h5py

yaml_config = sys.argv[1]
sim_dir = os.path.dirname(yaml_config)

# Read the yaml config
with open(yaml_config, "r") as f:
    data = yaml.safe_load(f)

nr_shells = {}
nr_lightcones = 0
while True:
    name = f"Lightcone{nr_lightcones}"
    if name not in data:
        break
    if "radius_file" in data[name]:
        with open(sim_dir+"/"+data[name]["radius_file"],"r") as f:
            cols = np.loadtxt(f, skiprows=1, delimiter=",")
            nr_shells[nr_lightcones] = cols.shape[0]
    nr_lightcones += 1

for map_name in ("neutrino_corrected_maps", "neutrino_corrected_maps_downsampled_4096"):
    print(f"check {map_name}")
    for lightcone_nr in range(nr_lightcones):
        for shell_nr in range(nr_shells[lightcone_nr]):
            filename = f"{sim_dir}/{map_name}/lightcone{lightcone_nr}_shells/shell_{shell_nr}/lightcone{lightcone_nr}.shell_{shell_nr}.0.hdf5"
            if not os.path.exists(filename):
                raise RuntimeError("Missing file!")
            try:
                with h5py.File(filename, "r") as f:
                    nr_files_per_shell = f["Shell"].attrs["nr_files_per_shell"][0]
                    assert nr_files_per_shell == 1
            except Exception:
                raise RuntimeError("Unreadable file!")

        print(f"  lightcone {lightcone_nr} ok with {nr_shells[lightcone_nr]} shells")

print()
print("Safe to delete:")
print()
for lightcone_nr in range(nr_lightcones):
    print(f"{sim_dir}/lightcones-do-not-use/lightcone{lightcone_nr}_shells")
