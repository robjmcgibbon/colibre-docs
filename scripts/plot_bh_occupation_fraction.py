import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import swiftsimio as sw
from scipy.stats import binned_statistic

# ---------------------------------------------------------
# Simulations to compare
# ---------------------------------------------------------
base_dir = "/cosma8/data/dp004/colibre/Runs/"
snap_nr = 127  # z=0

simulations = [
    ("L0400N3008/Thermal", "L400m7", "m7"),
    ("L0200N3008/Thermal", "L200m6", "m6"),
    ("L0025N0752/Thermal", "L025m5", "m5"),
]

COLIBRE_COLORS = {"m5": "#C4E8FF", "m6": "#FF9F6E", "m7": "#D12424"}
PATH_EFFECTS = [pe.Stroke(linewidth=3, foreground="k"), pe.Normal()]
LINE_WIDTH = 1.75

log_mass_bins = np.linspace(6, 12, 25)
log_mass_centres = 0.5 * (log_mass_bins[:-1] + log_mass_bins[1:])

fig, ax = plt.subplots(1)

for run, label, resolution in simulations:
    soap_filename = f"{base_dir}/{run}/SOAP-HBT/halo_properties_{snap_nr:04}.hdf5"
    print(f"Loading {label} ({run})...")
    soap = sw.load(soap_filename)

    stellar_mass = soap.exclusive_sphere_50kpc.stellar_mass.to_physical_value("Msun")
    bh_mass = soap.bound_subhalo.black_holes_subgrid_mass.to_physical_value("Msun")
    is_central = soap.input_halos.is_central[:].value == 1

    # host_halo_index maps each subhalo to the SOAP index of its host central
    # (a central maps to itself). M200c is only computed for centrals, so
    # indexing it by host_halo_index gives every subhalo its host's M200c.
    host_halo_index = soap.soap.host_halo_index[:].value
    M200c = soap.spherical_overdensity_200_crit.total_mass.to_physical_value("Msun")
    host_M200c = M200c[host_halo_index]

    has_bh = bh_mass > 0
    has_stars = stellar_mass > 0
    log_stellar_mass = np.log10(stellar_mass, where=has_stars, out=np.full_like(stellar_mass, np.nan))

    color = COLIBRE_COLORS[resolution]

    is_massive_host_sat = ~is_central & (host_M200c > 1e14)

    for sat_mask, linestyle in [
        (~is_central, "--"),
        (is_central, "-"),
        (is_massive_host_sat, ":"),
    ]:
        mask = has_stars & sat_mask
        if not np.any(mask):
            print(f"  No halos for {label} with linestyle {linestyle!r}, skipping")
            continue
        occupation_fraction, _, _ = binned_statistic(
            log_stellar_mass[mask],
            has_bh[mask].astype(float),
            statistic="mean",
            bins=log_mass_bins,
        )
        ax.plot(
            10**log_mass_centres,
            occupation_fraction,
            color=color,
            linestyle=linestyle,
            lw=LINE_WIDTH,
            path_effects=PATH_EFFECTS,
        )

# ---------------------------------------------------------
# Two legends stacked bottom right: simulation colour above line style
# ---------------------------------------------------------
style_handles = [
    plt.Line2D([0], [0], color="k", lw=LINE_WIDTH, linestyle="-", label="Central"),
    plt.Line2D([0], [0], color="k", lw=LINE_WIDTH, linestyle="--", label="Satellite"),
    plt.Line2D([0], [0], color="k", lw=LINE_WIDTH, linestyle=":", label=r"Satellite (host $M_{200c} > 10^{14}\,\mathrm{M}_\odot$)"),
]
style_legend = ax.legend(handles=style_handles, loc="lower right")
ax.add_artist(style_legend)

sim_handles = [
    plt.Line2D([0], [0], color=COLIBRE_COLORS[res], lw=LINE_WIDTH, path_effects=PATH_EFFECTS, label=label)
    for _, label, res in simulations
]
ax.legend(handles=sim_handles, loc="lower right", bbox_to_anchor=(1, 0.20))

ax.set_xscale("log")
ax.set_xlabel(r"Exclusive Sphere (50 kpc) $M_*$ [$M_\odot$]")
ax.set_ylabel("Black hole occupation fraction")
ax.set_ylim(0, 1.05)

plt.tight_layout()
plt.savefig("bh_occupation_fraction.png", dpi=200)
plt.close()

print("Saved bh_occupation_fraction.png")
