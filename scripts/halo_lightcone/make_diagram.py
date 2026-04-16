#!/bin/env python

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

snapshot_redshifts = {
    57 : 1.00,
    58 : 0.95,
    59 : 0.90,
    60 : 0.85,
    61 : 0.80,
    62 : 0.75,
    63 : 0.70,
    64 : 0.65,
    65 : 0.60,
    66 : 0.55,
    67 : 0.50,
    68 : 0.45,
    69 : 0.40,
    70 : 0.35,
    71 : 0.30,
    72 : 0.25,
    73 : 0.20,
    74 : 0.15,
    75 : 0.10,
    76 : 0.05,
    77 : 0.00,
}

# Snapshot file used to get cosmology info (temp. value for running on Hamilton)
import swiftsimio
snap_file = "/nobackup/dph1jch/COLIBRE/test_run/colibre_0127.hdf5"
snap = swiftsimio.load(snap_file)
cosmo = snap.metadata.cosmology

plt.figure(figsize=(8,5))
ax = plt.gca()
#ax.axis("off")
#ax.get_xaxis().set_visible(False)

colours = ("lightsteelblue", "lavender")

snapnums = range(64, 78)

# Draw wedges
rmax = 0
for snap_nr in list(snapnums) + [min(snapnums)-1,]:

    colour = colours[snap_nr % len(colours)]
    
    # Inner (later time) edge of the shell
    if snap_nr < 77:
        z1 = snapshot_redshifts[snap_nr+1]
        z2 = snapshot_redshifts[snap_nr]
        z_inner = 0.5*(z1+z2)
    else:
        z_inner = snapshot_redshifts[snap_nr]
    r_inner = cosmo.comoving_distance(z_inner).value
        
    # Outer (earlier time) edge of the shell
    z1 = snapshot_redshifts[snap_nr]
    z2 = snapshot_redshifts[snap_nr-1]
    z_outer = 0.5*(z1+z2)
    r_outer = cosmo.comoving_distance(z_outer).value
    rmax = max(rmax, r_outer)
    
    slice_patch = Wedge((0,0), r_outer, -90, 90, width=r_outer-r_inner, fc=colour)
    ax.add_patch(slice_patch)
    
# Add a horizontal line at z=0
ax.hlines(0, 0, rmax, color="black")

# Label the snapshot redshifts
r_label = [cosmo.comoving_distance(snapshot_redshifts[i]).value for i in snapnums]
ax.scatter(r_label, [0]*len(r_label), color="black", label="Shell midpoint")
ax.scatter(0, 0, color="red", label="Observer")

# Redshift labels
labels = [f"{snapshot_redshifts[i]:.2f}" for i in snapnums]
for r, l in zip(r_label, labels):
    if r > 0:
        ax.text(r, -100.0, l, ha="center", va="center")
ax.text(rmax/2, -200, "Redshift", ha="center", va="center")

# Snapnum labels
labels = [f"{i}" for i in snapnums]
for r, l in zip(r_label, labels):
    if r > 0:
        ax.text(r, 100.0, l, ha="center", va="center")
ax.text(rmax/2, 200, "Snapshot number", ha="center", va="center")


ax.set_xlim(   0, 2500)
ax.set_ylim(-800, 800)
ax.set_aspect('equal')
plt.ylabel("y [comoving Mpc]")
plt.xlabel("x [comoving Mpc]")
plt.legend(loc="upper right")
plt.title(r"Halo lightcone shells in $\mathtt{L1\_m9}$")
plt.tight_layout()
plt.savefig("lightcone_shells.png")
