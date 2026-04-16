#!/bin/env python

import h5py
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import LogNorm
from matplotlib import cm


def make_map_image(input_filename, map_name, output_filename):

    # Read in the map
    with h5py.File(input_filename, "r") as infile:
        nside = infile[map_name].attrs["nside"][0]
        map_data = infile[map_name][...]

    # Plot the map
    hp.mollview(map_data, norm="log", min=5e-10, max=5e-6, title="Compton Y at z < 0.05", cmap="inferno")

    # Save
    plt.savefig(output_filename)


if __name__ == "__main__":

    basedir="/cosma8/data/dp004/flamingo/Runs/L1000N3600/HYDRO_FIDUCIAL/neutrino_corrected_maps_downsampled_4096/lightcone0_shells/"
    shell_nr = 0
    make_map_image(f"{basedir}/shell_{shell_nr}/lightcone0.shell_{shell_nr}.0.hdf5", "ComptonY", "comptony_z0.05.png")
