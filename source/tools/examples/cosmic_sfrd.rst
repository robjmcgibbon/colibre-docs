:orphan:

Cosmic star formation rate density
===================================

SWIFT produces several plain-text log files alongside the snapshot output
which record global properties of the simulation at every timestep.
These are much smaller than the snapshots and convenient for tracking the
overall evolution of a run without opening HDF5 files.
The files available for COLIBRE simulations are:

* ``statistics.txt`` — global mass budgets (gas, dark matter, stars, black holes, dust,
  H, H₂, HI, He), energy budgets (kinetic, thermal, potential, radiated), BH accretion
  rate, bolometric luminosity, and jet power.
* ``SFR.txt`` — instantaneous star formation rate of all particles at every timestep.
* ``SNIa.txt`` — number and rate of SNIa events and total injected energy, per timestep.
* ``SNII.txt`` — same quantities for SNII events.

The example below uses ``SFR.txt`` to produce a plot of the
cosmic star formation rate density (SFRD) as a function of redshift.
Because SWIFT writes one row per timestep and there are hundreds of thousands
of timesteps in a full run, the raw values are binned in log scale factor before
plotting. The x-axis is also in log scale factor, relabelled with the
corresponding redshift values, which gives a more uniform spacing in cosmic
time than plotting against redshift directly.

.. code-block:: python

    import h5py
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.patheffects as pe
    from scipy.stats import binned_statistic

    COSMA_DIR = "/cosma8/data/dp004/colibre/Runs"
    SNAP_NR = 127  # z=0

    simulations = [
        ("L0400N3008/Thermal", "L400m7", "m7"),
        ("L0200N3008/Thermal", "L200m6", "m6"),
        ("L0025N0752/Thermal", "L25m5",  "m5"),
    ]

    COLIBRE_COLORS = {"m5": "#C4E8FF", "m6": "#FF9F6E", "m7": "#D12424"}
    PATH_EFFECTS = [pe.Stroke(linewidth=5, foreground="k"), pe.Normal()]
    LINE_WIDTH = 3.5
    SFR_TO_MSUN_PER_YR = 1.022690e-02

    fig, ax = plt.subplots(1)

    for run, label, resolution in simulations:
        sim_dir = f"{COSMA_DIR}/{run}"

        # Read the comoving box side length from the snapshot header
        snap = f"{sim_dir}/snapshots/colibre_{SNAP_NR:04d}/colibre_{SNAP_NR:04d}.0.hdf5"
        with h5py.File(snap, "r") as f:
            box_size_mpc = f["Header"].attrs["BoxSize"][0]  # comoving Mpc

        box_volume_mpc3 = box_size_mpc ** 3

        # Load the SFR file.
        # Column 3: redshift
        # Column 7: total SFR of all particles (internal units)
        # The conversion factor to Msun/yr is given in the file header.
        data = np.loadtxt(f"{sim_dir}/SFR.txt", comments="#")
        redshift = data[:, 3]
        sfrd = data[:, 7] * SFR_TO_MSUN_PER_YR / box_volume_mpc3  # Msun/yr/cMpc^3

        # Convert to log scale factor for the x-axis. Plotting in log(a) gives a
        # more uniform spacing in cosmic time than plotting in redshift directly.
        log_a = np.log10(1.0 / (1.0 + redshift))

        # Bin the SFRD in log scale factor to smooth over per-timestep noise.
        log_a_bins = np.linspace(-1.3, 0, 300)
        sfrd_binned, edges, _ = binned_statistic(
            log_a, sfrd, statistic="mean", bins=log_a_bins
        )
        log_a_centres = 0.5 * (edges[:-1] + edges[1:])
        mask = sfrd_binned > 0

        ax.semilogy(
            log_a_centres[mask],
            sfrd_binned[mask],
            color=COLIBRE_COLORS[resolution],
            lw=LINE_WIDTH,
            path_effects=PATH_EFFECTS,
            label=label,
        )

    # Place x-axis ticks at positions corresponding to round redshift values
    z_ticks = [0, 0.5, 1, 2, 3, 5, 7, 10]
    ax.set_xticks(np.log10(1.0 / (1.0 + np.array(z_ticks))))
    ax.set_xticklabels(z_ticks)
    ax.set_xlabel("Redshift $z$")
    ax.set_ylabel(r"SFR density [$\mathrm{M_\odot \, yr^{-1} \, cMpc^{-3}}$]")
    ax.set_xlim(0, -1.3)
    ax.set_ylim(bottom=1e-4)
    ax.legend()
    plt.tight_layout()
    plt.savefig("cosmic_sfrd.png", dpi=200)
    plt.close()
