:orphan:

Mass evolution of a subhalo
===========================

Example code for tracking the mass evolution of a halo across snapshots.
The most massive halo at :math:`z=0` (by :math:`M_{200c}`) is identified via its
``TrackId``, which remains consistent across all snapshots, allowing the halo
to be located in each earlier catalogue.
Note that if you need to do this for many objects, reading the raw
`HBT-HERONS <../../soap/hbt_merger_trees.html>`__ output files directly may
be more efficient, as those files are sorted by ``TrackId``.

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np
    import swiftsimio as sw

    # ---------------------------------------------------------
    # Find the most massive halo at z=0 and get its TrackId
    # ---------------------------------------------------------
    base_dir = "/cosma8/data/dp004/colibre/Runs/"
    run = "L0100N1504/Thermal"
    snap_nr = 127  # z=0
    soap_filename = f"{base_dir}/{run}/SOAP-HBT/halo_properties_{snap_nr:04}.hdf5"
    soap = sw.load(soap_filename)

    halo_M200c = soap.spherical_overdensity_200_crit.total_mass.to_physical_value("Msun")
    central_idx = np.argmax(halo_M200c)
    track_id = soap.input_halos_hbtplus.track_id[central_idx].value

    print(f"Tracking halo with TrackId={track_id}, M200c={halo_M200c[central_idx]:.2e} Msun")

    # ---------------------------------------------------------
    # Loop over snapshots and record masses
    # ---------------------------------------------------------
    # Dark matter and gas masses are taken within R200c.
    # Stellar mass is taken within a 50 kpc aperture.
    # TrackIds may be absent from early snapshots if the halo had
    # fewer than 20 bound particles, so we skip any missing entries.
    snap_nrs = np.arange(22, 128, 5)
    scale_factors = []
    dm_masses = []
    gas_masses = []
    stellar_masses = []

    for i, snap_nr in enumerate(snap_nrs):
        print(f"Loading snapshot {snap_nr} ({i + 1}/{len(snap_nrs)})")
        soap_filename = f"{base_dir}/{run}/SOAP-HBT/halo_properties_{snap_nr:04}.hdf5"
        soap = sw.load(soap_filename)

        matches = np.where(soap.input_halos_hbtplus.track_id[:].value == track_id)[0]
        if len(matches) == 0:
            print(f"  TrackId={track_id} not found, skipping")
            continue
        idx = matches[0]

        scale_factors.append(soap.metadata.a)
        dm_masses.append(soap.spherical_overdensity_200_crit.dark_matter_mass[idx].to_physical_value("Msun"))
        gas_masses.append(soap.spherical_overdensity_200_crit.gas_mass[idx].to_physical_value("Msun"))
        stellar_masses.append(soap.exclusive_sphere_50kpc.stellar_mass[idx].to_physical_value("Msun"))

    scale_factors = np.array(scale_factors)
    dm_masses = np.array(dm_masses)
    gas_masses = np.array(gas_masses)
    stellar_masses = np.array(stellar_masses)

    # ---------------------------------------------------------
    # Plot
    # ---------------------------------------------------------
    fig, ax = plt.subplots(1)

    ax.plot(scale_factors, dm_masses, label="Dark matter ($R_{200c}$)", color="k")
    ax.plot(scale_factors, gas_masses, label="Gas ($R_{200c}$)", color="tab:green")
    ax.plot(scale_factors, stellar_masses, label="Stars (50 kpc)", color="tab:orange")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Scale factor")
    ax.set_ylabel(r"Mass [$M_\odot$]")
    ax.set_title(f"Mass evolution (TrackId = {track_id})")
    ax.legend()

    plt.savefig("mass_evolution.png", dpi=200)
    plt.close()
