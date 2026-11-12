:orphan:

Mass evolution of a subhalo
===========================

These examples show how to follow subhalos back in time along their main
progenitor branch, and extract their properties from the SOAP catalogues
at earlier snapshots. There are two ways to link subhalos between snapshots:

* ``SOAP/ProgenitorIndex`` gives the index of the main progenitor of each subhalo
  in the SOAP catalogue of the previous snapshot. It only links neighbouring snapshots,
  so the catalogue for every snapshot must be loaded.
* ``InputHalos/HBTplus/TrackId`` is the same for a subhalo at all snapshots, so it can
  be used to find a subhalo in any catalogue, without loading the snapshots in between.

Both methods follow the same main progenitor branch, since ``SOAP/ProgenitorIndex``
points to the subhalo with the same ``TrackId`` in the previous snapshot.
The first example uses ``SOAP/ProgenitorIndex`` to follow a single subhalo, which
shows how the index works. The second example uses ``TrackId`` to follow
many subhalos at once.

.. note::

   The ``SOAP/ProgenitorIndex`` in the current SOAP catalogues is incorrect for a small number of
   subhalos (see :ref:`issues_progenitor_descendant_index_order`), so the first example reads it from the
   :ref:`SOAP-DescendantInfo <soap_descendant_info>` catalogues, which have the same ordering as the
   SOAP catalogues.

.. note::

   SOAP catalogues only contain resolved subhalos. A subhalo can drop below the resolution limit
   of HBT-HERONS and become resolved again at a later snapshot. In this case
   ``SOAP/ProgenitorIndex`` is -1 at the snapshot where the subhalo becomes resolved again,
   so following the progenitor index stops there. Matching by ``TrackId`` finds the subhalo
   at all the snapshots where it is resolved, leaving gaps where it is not.

Following a single subhalo with ProgenitorIndex
-----------------------------------------------

This example finds the most massive halo at :math:`z=0` (by :math:`M_{200c}`), and follows
``SOAP/ProgenitorIndex`` back one snapshot at a time until it reaches -1, which means that
the subhalo was not resolved in the previous snapshot.

.. warning::

   This example is written to show how ``SOAP/ProgenitorIndex`` works, not to be fast.
   ``swiftsimio`` reads the whole of a dataset (i.e. the value for every subhalo)
   the first time it is accessed, even though we only need the value for one subhalo.
   Doing this for every snapshot of L100m6 is slow. If you need to
   follow a single subhalo quickly then read individual elements using ``h5py``,
   and if you need to follow many subhalos then use the
   :ref:`vectorised example <mass_evolution_vectorised>` below.

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np
    import swiftsimio as sw

    base_dir = "/cosma8/data/dp004/colibre/Runs"
    descendant_info_dir = "/cosma8/data/dp004/dc-mcgi1/COLIBRE"
    run = "L0100N1504/Thermal"
    final_snap_nr = 127  # z=0
    soap_basename = f"{base_dir}/{run}/SOAP-HBT/halo_properties_{{snap_nr:04}}.hdf5"
    descendant_info_basename = (
        f"{descendant_info_dir}/{run}/SOAP-DescendantInfo/descendant_info_{{snap_nr:04}}.hdf5"
    )

    # ---------------------------------------------------------
    # Find the most massive halo at z=0
    # ---------------------------------------------------------
    soap = sw.load(soap_basename.format(snap_nr=final_snap_nr))
    halo_M200c = soap.spherical_overdensity_200_crit.total_mass.to_physical_value("Msun")
    idx = np.argmax(halo_M200c)
    track_id = soap.input_halos_hbtplus.track_id[idx].value
    print(f"Tracking halo with TrackId={track_id}, M200c={halo_M200c[idx]:.2e} Msun")

    # ---------------------------------------------------------
    # Follow the progenitor index back in time
    # ---------------------------------------------------------
    # Dark matter and gas masses are taken within R200c.
    # Stellar mass is taken within a 50 kpc aperture.
    # Note that spherical overdensity properties are only computed for
    # central subhalos, so the R200c masses will be zero at any snapshot
    # where the main progenitor was a satellite.
    scale_factors = []
    dm_masses = []
    gas_masses = []
    stellar_masses = []

    snap_nr = final_snap_nr
    while idx != -1:
        print(f"Snapshot {snap_nr}: index {idx}")
        soap = sw.load(soap_basename.format(snap_nr=snap_nr))
        scale_factors.append(soap.metadata.a)
        dm_masses.append(soap.spherical_overdensity_200_crit.dark_matter_mass[idx].to_physical_value("Msun"))
        gas_masses.append(soap.spherical_overdensity_200_crit.gas_mass[idx].to_physical_value("Msun"))
        stellar_masses.append(soap.exclusive_sphere_50kpc.stellar_mass[idx].to_physical_value("Msun"))

        # Move to the main progenitor in the previous snapshot. This is -1 if the
        # subhalo was not resolved in the previous snapshot (or this is snapshot 0)
        descendant_info = sw.load(descendant_info_basename.format(snap_nr=snap_nr))
        idx = descendant_info.soap.progenitor_index[idx].value
        snap_nr -= 1

    print(f"Main progenitor branch starts at snapshot {snap_nr + 1}")

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

.. _mass_evolution_vectorised:

Following many subhalos with TrackId
------------------------------------

This example selects all central subhalos with :math:`M_{200c} > 10^{13} \, M_\odot` at :math:`z=0`,
and finds them in the SOAP catalogues for a selection of earlier snapshots by matching their ``TrackId``.
All of the subhalos are matched at once, so each catalogue only needs to be read once.
The median mass evolution of the sample is then plotted.

Bound subhalo masses are used rather than :math:`M_{200c}`, since spherical overdensity
properties are only computed for central subhalos, and some of the main progenitors
will have been satellites at earlier times.

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np
    import swiftsimio as sw

    base_dir = "/cosma8/data/dp004/colibre/Runs"
    run = "L0100N1504/Thermal"
    final_snap_nr = 127  # z=0
    soap_basename = f"{base_dir}/{run}/SOAP-HBT/halo_properties_{{snap_nr:04}}.hdf5"

    # ---------------------------------------------------------
    # Select the sample at z=0
    # ---------------------------------------------------------
    soap = sw.load(soap_basename.format(snap_nr=final_snap_nr))
    halo_M200c = soap.spherical_overdensity_200_crit.total_mass.to_physical_value("Msun")
    is_central = soap.input_halos.is_central.value == 1
    mask = is_central & (halo_M200c > 1e13)
    track_ids = soap.input_halos_hbtplus.track_id.value[mask]
    n_halo = track_ids.shape[0]
    print(f"Selected {n_halo} halos")

    # ---------------------------------------------------------
    # Match the TrackIds in each snapshot
    # ---------------------------------------------------------
    # Subhalos which are not resolved in a snapshot are left as NaN
    snap_nrs = np.arange(22, final_snap_nr + 1, 5)
    scale_factors = np.zeros(snap_nrs.shape[0])
    bound_masses = np.full((n_halo, snap_nrs.shape[0]), np.nan)
    stellar_masses = np.full((n_halo, snap_nrs.shape[0]), np.nan)

    for j, snap_nr in enumerate(snap_nrs):
        print(f"Loading snapshot {snap_nr} ({j + 1}/{len(snap_nrs)})")
        soap = sw.load(soap_basename.format(snap_nr=snap_nr))
        scale_factors[j] = soap.metadata.a

        # TrackIds are unique within a catalogue. idx_sample is the position of
        # each matched subhalo in our sample, and idx_soap is its position in
        # the SOAP catalogue for this snapshot
        _, idx_sample, idx_soap = np.intersect1d(
            track_ids,
            soap.input_halos_hbtplus.track_id.value,
            assume_unique=True,
            return_indices=True,
        )

        bound_mass = soap.bound_subhalo.total_mass.to_physical_value("Msun")
        stellar_mass = soap.exclusive_sphere_50kpc.stellar_mass.to_physical_value("Msun")
        bound_masses[idx_sample, j] = bound_mass[idx_soap]
        stellar_masses[idx_sample, j] = stellar_mass[idx_soap]

    # ---------------------------------------------------------
    # Plot the median and 16th-84th percentiles of the sample
    # ---------------------------------------------------------
    fig, ax = plt.subplots(1)

    for masses, label, color in [
        (bound_masses, "Bound mass", "k"),
        (stellar_masses, "Stars (50 kpc)", "tab:orange"),
    ]:
        lo, med, hi = np.nanpercentile(masses, [16, 50, 84], axis=0)
        ax.plot(scale_factors, med, label=label, color=color)
        ax.fill_between(scale_factors, lo, hi, color=color, alpha=0.2)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Scale factor")
    ax.set_ylabel(r"Mass [$M_\odot$]")
    ax.set_title(rf"Main progenitors of $z=0$ halos with $M_{{200c}} > 10^{{13}} \, M_\odot$")
    ax.legend()

    plt.savefig("mass_evolution_vectorised.png", dpi=200)
    plt.close()
