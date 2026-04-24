Matching halos across simulations
=================================

Matching catalogues are provided to link halos containing the same particles across different simulations.
For each halo in the first simulation we take the IDs of all the particles bound and determine which halo in the second output contains the largest number of these IDs. This matching process is then repeated in the opposite direction and we check for cases where we have consistent matches in both directions. Matching is not carried out for satellite subhalos.

Each hydrodynamical simulation is matched to its corresponding DMO run at the same resolution.
Therefore, if you wish to match halos between the Thermal and Hybrid AGN feedback variations runs, you should do this via the DMO run.
There are currently no matching catalogues across resolutions.

The output is a HDF5 file with the following datasets:

    * ``MatchIndex1to2`` - for each subhalo in the first soap catalogue, index of the matching halo in the second.
    * ``MatchCount1to2`` - how many of the particles from the halo in the first catalogue are in the matched halo in the second.
    * ``Consistent1to2`` - whether the match from first to second catalogue is consistent with second to first (1) or not (0).

There are corresponding datasets with 1 and 2 reversed (e.g. ``MatchIndex2to1``) with information about matching in the opposite direction.

Matching catalogues can be found in ``/cosma8/data/dp004/dc-mcgi1/COLIBRE/matching/``.
Please contact Rob McGibbon if you require them for other simulations/snapshots.

Matching example
----------------

.. code-block:: python

    import h5py
    import matplotlib.pyplot as plt
    import numpy as np
    import swiftsimio as sw

    # Simulations to match between
    sim1 = "L0100N1504/DMO"
    sim2 = "L0100N1504/Thermal"
    nr_part = -1  # -1 indicates all particles were used to do the matching
    snap_nr = 127

    # Load SOAP catalogues
    base_dir = "/cosma8/data/dp004/colibre/Runs"
    soap1 = sw.load(f"{base_dir}/{sim1}/SOAP-HBT/halo_properties_{snap_nr:04}.hdf5")
    soap2 = sw.load(f"{base_dir}/{sim2}/SOAP-HBT/halo_properties_{snap_nr:04}.hdf5")

    # Load matching file
    sim1 = sim1.replace('/', '_')
    sim2 = sim2.replace('/', '_')
    match_dir = f"/cosma8/data/dp004/dc-mcgi1/COLIBRE/matching/"
    match_filename = f"{match_dir}/match_{sim1}_{sim2}_{snap_nr:04}.{nr_part}.hdf5"
    with h5py.File(match_filename, "r") as file:
        match_index = file["MatchIndex1to2"][:]
        consistent = file["Consistent1to2"][:] == 1

    # Load the bound mass of the matched halos
    fig, ax = plt.subplots(1)
    bound_mass_1 = soap1.bound_subhalo.total_mass[consistent]
    bound_mass_2 = soap2.bound_subhalo.total_mass[match_index[consistent]]

    # Plot
    bins = 10 ** np.linspace(9, 14, 50)
    ax.hist2d(bound_mass_1.to('Msun').value, bound_mass_2.to('Msun').value, bins=bins, norm="log")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(f"Mass in {sim1} [$M_\\odot$]")
    ax.set_ylabel(f"Mass in {sim2} [$M_\\odot$]")
    plt.savefig(f"compare_mbound_{sim1}_{sim2}.png", dpi=200)
    plt.close()

