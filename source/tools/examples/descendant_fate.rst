:orphan:

Fate of satellite galaxies
==========================

This example takes all the satellite galaxies with :math:`M_* > 10^9 \, M_\odot` at :math:`z=1` in the
L25m7 simulation, and determines what has happened to them by :math:`z=0`. Each satellite either:

* survives to :math:`z=0`,
* merges with another subhalo (it disrupts or sinks), in which case its :math:`z=0` descendant is the
  subhalo which contains its remains,
* or disrupts without leaving a descendant, because the majority of its most bound particles are not bound to any
  subhalo.

``SOAP/DescendantIndex`` gives the index of the descendant of each subhalo in the SOAP catalogue of the next
snapshot, and ``SOAP/DescendantType`` says what happened to the subhalo between the two snapshots
(0: survived, 1: disrupted, 2: sunk, 3: disrupted with no descendant).
``SOAP/DescendantIndex`` only links neighbouring snapshots, so we have to step forward one snapshot at a time.
However, all the satellites are followed at once by indexing the ``SOAP/DescendantIndex`` array with the current
descendant index of every satellite, so each catalogue only needs to be read once. Only the
``SOAP/DescendantIndex`` and ``SOAP/DescendantType`` arrays are read at each snapshot, and
the full SOAP catalogues are only read at :math:`z=1` and :math:`z=0`.

After a satellite merges we keep following the descendant, so the descendant index points to the subhalo
it merged with, then to whatever that subhalo merges with, and so on. If any of these
subhalos disrupts without a descendant then the descendant index becomes -1.

.. note::

   The ``SOAP/DescendantIndex`` in the current SOAP catalogues only follows the main progenitor branch,
   so this example reads ``SOAP/DescendantIndex`` and ``SOAP/DescendantType`` from the
   :ref:`SOAP-DescendantInfo <soap_descendant_info>` catalogues, which have the same ordering as the
   SOAP catalogues.

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np
    import swiftsimio as sw

    base_dir = "/cosma8/data/dp004/colibre/Runs"
    descendant_info_dir = "/cosma8/data/dp004/dc-mcgi1/COLIBRE"
    run = "L0025N0188/Thermal"
    start_snap_nr = 92  # z=1
    final_snap_nr = 127  # z=0
    soap_basename = f"{base_dir}/{run}/SOAP-HBT/halo_properties_{{snap_nr:04}}.hdf5"
    descendant_info_basename = (
        f"{descendant_info_dir}/{run}/SOAP-DescendantInfo/descendant_info_{{snap_nr:04}}.hdf5"
    )

    # ---------------------------------------------------------
    # Select satellites with M* > 1e9 Msun at z=1
    # ---------------------------------------------------------
    soap = sw.load(soap_basename.format(snap_nr=start_snap_nr))
    stellar_mass = soap.exclusive_sphere_50kpc.stellar_mass.to_physical_value("Msun")
    is_central = soap.input_halos.is_central.value == 1
    sample_idx = np.nonzero((~is_central) & (stellar_mass > 1e9))[0]
    n_sample = sample_idx.shape[0]
    print(f"Selected {n_sample} satellites")

    # ---------------------------------------------------------
    # Follow the descendants forward one snapshot at a time
    # ---------------------------------------------------------
    # Index of the descendant of each satellite in the current snapshot
    desc_idx = sample_idx.copy()
    # Whether each satellite is still the same subhalo (i.e. has not merged)
    survived = np.ones(n_sample, dtype=bool)
    # What happened to each satellite (0: survived, 1: disrupted, 2: sunk,
    # 3: disrupted with no descendant), and the first snapshot after it merged
    fate = np.zeros(n_sample, dtype=int)
    merger_snap_nr = np.full(n_sample, -1)
    # Lookback time of each snapshot, used for plotting
    lookback_time_gyr = {}

    for snap_nr in range(start_snap_nr, final_snap_nr + 1):
        descendant_info = sw.load(descendant_info_basename.format(snap_nr=snap_nr))
        metadata = descendant_info.metadata
        lookback_time_gyr[snap_nr] = metadata.cosmology.lookback_time(metadata.z).to_value("Gyr")
        if snap_nr == final_snap_nr:
            break
        print(f"Snapshot {snap_nr}: {np.sum(survived)} satellites have not merged")

        descendant_index = descendant_info.soap.descendant_index.value
        descendant_type = descendant_info.soap.descendant_type.value

        # Record the satellites which stop being the same subhalo between this
        # snapshot and the next. A satellite which has not merged always has a
        # valid descendant index, so it is safe to index with desc_idx here
        merging = survived.copy()
        merging[survived] = descendant_type[desc_idx[survived]] != 0
        fate[merging] = descendant_type[desc_idx[merging]]
        merger_snap_nr[merging] = snap_nr + 1
        survived[merging] = False

        # Move every satellite which still has a descendant to the next snapshot
        has_desc = desc_idx != -1
        desc_idx[has_desc] = descendant_index[desc_idx[has_desc]]

    # ---------------------------------------------------------
    # Summarise the fates of the satellites
    # ---------------------------------------------------------
    merged = (fate == 1) | (fate == 2)
    print(f"Survived to z=0: {np.sum(fate == 0) / n_sample:.2f}")
    print(f"Disrupted: {np.sum(fate == 1) / n_sample:.2f}")
    print(f"Sunk: {np.sum(fate == 2) / n_sample:.2f}")
    print(f"Disrupted with no descendant: {np.sum(fate == 3) / n_sample:.2f}")

    # For the satellites which merged, check whether their z=0 descendant
    # is a central galaxy. desc_idx is -1 if the subhalo they merged with
    # later disrupted without a descendant
    soap = sw.load(soap_basename.format(snap_nr=final_snap_nr))
    is_central_z0 = soap.input_halos.is_central.value == 1
    merged_desc_idx = desc_idx[merged]
    has_desc = merged_desc_idx != -1
    n_merged_into_central = np.sum(is_central_z0[merged_desc_idx[has_desc]])
    print(
        f"Of the {np.sum(merged)} satellites which merged, {n_merged_into_central} "
        f"have a z=0 descendant which is a central galaxy, and "
        f"{np.sum(~has_desc)} have no z=0 descendant"
    )

    # ---------------------------------------------------------
    # Plot when the satellites merged
    # ---------------------------------------------------------
    # merger_snap_nr is the first snapshot after the merger, so the merger
    # happened in the time between merger_snap_nr - 1 and merger_snap_nr
    merger_lookback_time_gyr = np.array(
        [lookback_time_gyr[snap_nr] for snap_nr in merger_snap_nr[merged]]
    )
    bins = np.linspace(0, lookback_time_gyr[start_snap_nr], 11)

    fig, ax = plt.subplots(1)
    ax.hist(
        [merger_lookback_time_gyr[fate[merged] == 1], merger_lookback_time_gyr[fate[merged] == 2]],
        bins=bins,
        stacked=True,
        label=["Disrupted", "Sunk"],
        color=["tab:blue", "tab:orange"],
    )
    ax.set_xlim(lookback_time_gyr[start_snap_nr], 0)
    ax.set_xlabel("Lookback time [Gyr]")
    ax.set_ylabel("Number of satellites")
    ax.set_title(r"Mergers of $z=1$ satellites with $M_* > 10^9 \, M_\odot$")
    ax.legend()

    plt.savefig("descendant_fate.png", dpi=200)
    plt.close()
