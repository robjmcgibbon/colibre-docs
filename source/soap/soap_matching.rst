Matching halos across simulations
=================================

Matching catalogues are provided to link halos containing the same particles across different simulations.
For each halo in the first simulation we take the IDs of all the particles bound and determine which halo in the second output contains the largest number of these IDs. This matching process is then repeated in the opposite direction and we check for cases where we have consistent matches in both directions. Matching is not carried out for satellite subhalos.

Each hydrodynamical simulation is matched to its corresponding DMO run at the same resolution.
Therefore, if you wish to match halos across the :math:`1 \; \rm{Gpc}` feedback variations runs, you should do this via ``L1_m9_DMO``.
Additionally, all the :math:`1 \; \rm{Gpc}` DMO cosmology variations are matched to the ``L1_m9_DMO``
There are currently no matching catalogues across resolutions.

The output is a HDF5 file with the following datasets:

    * ``MatchIndex1to2`` - for each subhalo in the first soap catalogue, index of the matching halo in the second.
    * ``MatchCount1to2`` - how many of the particles from the halo in the first catalogue are in the matched halo in the second.
    * ``Consistent1to2`` - whether the match from first to second catalogue is consistent with second to first (1) or not (0).

There are corresponding datasets with 1 and 2 reversed (e.g. ``MatchIndex2to1``) with information about matching in the opposite direction.

TODO: Test this script works once the matching files are available

Matching example
----------------

.. code-block:: python

    import hdfstream
    import matplotlib.pyplot as plt
    import numpy as np
    import swiftsimio as sw

    # Connect to the hdfstream service and open the root directory
    root_dir = hdfstream.open("cosma", "/")

    # Simulations to match between
    sim1 = "L1_m9_DMO"
    sim2 = "L1_m9"
    snap_nr = 77

    # Load SOAP catalogues
    soap1 = sw.load(root_dir[f"FLAMINGO/L1_m9/{sim1}/SOAP-HBT/halo_properties_{snap_nr:04}.hdf5"])
    soap2 = sw.load(root_dir[f"FLAMINGO/L1_m9/{sim2}/SOAP-HBT/halo_properties_{snap_nr:04}.hdf5"])

    # Load matching file
    match_filename = f"FLAMINGO/L1_m9/{sim2}/SOAP-HBT/match_{sim1}_{sim2}_{snap_nr:04}.hdf5"
    with hdfstream.open('cosma', match_filename) as file:
        match_index = file["MatchIndex1to2"][:]
        consistent = file["Consistent1to2"][:] == 1

    # Load the mass of the matched halos
    mass_1 = soap1.spherical_overdensity_200_crit.total_mass[consistent]
    mass_2 = soap2.spherical_overdensity_200_crit.total_mass[match_index[consistent]]

    # Plot
    fig, ax = plt.subplots(figsize=(7, 6))
    bins = np.logspace(8, 15, 100)

    h = ax.hist2d(
        mass_1.to_physical_value('Msun'),
        mass_2.to_physical_value('Msun'),
        bins=bins,
        norm="log",
    )
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(f"M200c in {sim1} [$M_\\odot$]")
    ax.set_ylabel(f"M200c in {sim2} [$M_\\odot$]")

    cbar = fig.colorbar(h[3], ax=ax)
    cbar.set_label('N_halo')

    plt.savefig(f"compare_mbound_{sim1}_{sim2}.png", dpi=200)
    plt.close()

