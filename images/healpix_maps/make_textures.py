#!/bin/env python

import h5py
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import LogNorm
from matplotlib import cm


def make_textures(input_filename, output_filename):

    # Read in the map
    with h5py.File(input_filename, "r") as infile:
        nside = infile["SmoothedGasMass"].attrs["nside"][0]
        map_data = infile["SmoothedGasMass"][...]

    # Get cartesian projection
    nx = 2048
    proj = hp.projector.CartesianProj(xsize=nx, ysize=nx // 2, lonra=[0, 360], latra=[-90, 90])
    vec2pix = lambda x, y, z : hp.pixelfunc.vec2pix(nside, x, y, z)
    map_2d = proj.projmap(map_data, vec2pix)

    vmin = np.mean(map_2d) / 3.
    vmax = np.mean(map_2d) * 4.

    # Convert the array to a colour image
    norm = LogNorm(vmin=vmin, vmax=vmax)
    cmap = matplotlib.colormaps["viridis"]
    rgba = cmap(norm(map_2d))
    img = (rgba * 255).astype(np.uint8)

    # Save
    plt.imsave(output_filename, img)


if __name__ == "__main__":

    basedir="/cosma8/data/dp004/flamingo/Runs/L1000N3600/HYDRO_FIDUCIAL/neutrino_corrected_maps_downsampled_4096/lightcone0_shells/"

    for shell_nr in range(10):
        input_filename = f"{basedir}/shell_{shell_nr}/lightcone0.shell_{shell_nr}.0.hdf5"
        output_filename = f"./images/shell_{shell_nr}.png"
        make_textures(input_filename, output_filename)
