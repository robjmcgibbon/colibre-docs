:orphan:

Merger history of a galaxy
==========================

This example counts the number of major and minor mergers a galaxy in the L25m7 simulation has had in the
1 Gyr before :math:`z=2`. It uses ``SOAP/ProgenitorIndex`` to follow the
main progenitor branch of the galaxy back in time (see :doc:`mass_evolution`), and
``SOAP/DescendantIndex`` to find the other subhalos which merged with it.

``SOAP/DescendantIndex`` points to the subhalo itself in the next snapshot if it survives,
otherwise it points to the subhalo it merged with. Therefore all the progenitors of a subhalo at
snapshot :math:`n` are the subhalos at snapshot :math:`n-1` whose ``SOAP/DescendantIndex`` points to it.
One of these is the main progenitor (the subhalo with the same ``TrackId``, which survives). The others
are subhalos which merged between snapshot :math:`n-1` and snapshot :math:`n`, and they have
``SOAP/DescendantType`` equal to 1 (disrupted) or 2 (sunk).

.. note::

   The ``SOAP/DescendantIndex`` in the current SOAP catalogues only follows the main progenitor branch,
   so this example reads ``SOAP/ProgenitorIndex``, ``SOAP/DescendantIndex`` and ``SOAP/DescendantType`` from the
   :ref:`SOAP-DescendantInfo <soap_descendant_info>` catalogues, which have the same ordering as the
   SOAP catalogues.

The example works as follows:

#. Determine which snapshots lie within the 1 Gyr before :math:`z=2`, using the lookback time of each snapshot.
   Only mergers which happen between two of these snapshots are counted.
#. Select the galaxy using its ``TrackId``. We use ``TrackId = 389``, which has one major and one minor merger
   in this time.
#. Step back one snapshot at a time. At each step find the main progenitor of the galaxy and the
   subhalos which merged with it.
#. Compute the stellar mass ratio of each merger, as the stellar mass of the less massive
   progenitor divided by the stellar mass of the more massive progenitor. Mergers with a ratio
   above 1/4 are counted as major mergers, and mergers with a ratio between 1/10 and 1/4 are counted
   as minor mergers.

.. note::

   The stellar mass ratio is computed using the stellar masses at the last snapshot before the merger.
   Satellites lose mass due to tidal stripping as they orbit within their host, so their stellar mass just
   before they merge will be lower than their stellar mass when they fell in. This biases the mass ratios
   low, so some mergers will be classified as minor (or not counted at all) when they would be major (or minor)
   if the mass ratio was computed at infall, or using the peak stellar mass of each progenitor.

.. code-block:: python

    import numpy as np
    import swiftsimio as sw

    base_dir = "/cosma8/data/dp004/colibre/Runs"
    descendant_info_dir = "/cosma8/data/dp004/dc-mcgi1/COLIBRE"
    run = "L0025N0188/Thermal"
    target_snap_nr = 76  # z=2
    target_track_id = 389
    soap_basename = f"{base_dir}/{run}/SOAP-HBT/halo_properties_{{snap_nr:04}}.hdf5"
    descendant_info_basename = (
        f"{descendant_info_dir}/{run}/SOAP-DescendantInfo/descendant_info_{{snap_nr:04}}.hdf5"
    )

    # Count mergers which happen in the max_time_gyr before target_snap_nr
    max_time_gyr = 1.0
    # Minimum stellar mass ratio for major and minor mergers
    major_merger_ratio = 1 / 4
    minor_merger_ratio = 1 / 10

    # ---------------------------------------------------------
    # Find the earliest snapshot within max_time_gyr of target_snap_nr
    # ---------------------------------------------------------
    def get_lookback_time_gyr(snap_nr):
        metadata = sw.load(soap_basename.format(snap_nr=snap_nr)).metadata
        return metadata.cosmology.lookback_time(metadata.z).to_value("Gyr")

    target_lookback_time_gyr = get_lookback_time_gyr(target_snap_nr)
    first_snap_nr = target_snap_nr
    while first_snap_nr > 0:
        lookback_time_gyr = get_lookback_time_gyr(first_snap_nr - 1)
        if lookback_time_gyr - target_lookback_time_gyr > max_time_gyr:
            break
        first_snap_nr -= 1
    print(f"Counting mergers between snapshots {first_snap_nr} and {target_snap_nr}")

    # ---------------------------------------------------------
    # Find the galaxy in the target snapshot using its TrackId
    # ---------------------------------------------------------
    soap = sw.load(soap_basename.format(snap_nr=target_snap_nr))
    idx = np.nonzero(soap.input_halos_hbtplus.track_id.value == target_track_id)[0][0]
    stellar_mass = soap.exclusive_sphere_50kpc.stellar_mass[idx].to_physical_value("Msun")
    print(f"Selected galaxy with TrackId={target_track_id}, M*={stellar_mass:.2e} Msun")

    # ---------------------------------------------------------
    # Step back along the main progenitor branch, counting mergers
    # ---------------------------------------------------------
    descendant_type_names = {1: "disrupted", 2: "sunk"}
    n_major = 0
    n_minor = 0
    descendant_info = sw.load(descendant_info_basename.format(snap_nr=target_snap_nr))
    for snap_nr in range(target_snap_nr, first_snap_nr, -1):
        # Index of the main progenitor of the galaxy at snapshot snap_nr - 1.
        # This is -1 if the galaxy was not resolved at the previous snapshot
        main_prog_idx = descendant_info.soap.progenitor_index[idx].value
        if main_prog_idx == -1:
            print(f"Main progenitor branch starts at snapshot {snap_nr}")
            break

        # Find all subhalos at snapshot snap_nr - 1 whose descendant is the
        # galaxy. Removing the main progenitor leaves the subhalos which merged
        prev_descendant_info = sw.load(descendant_info_basename.format(snap_nr=snap_nr - 1))
        prog_idx = np.nonzero(prev_descendant_info.soap.descendant_index.value == idx)[0]
        merger_idx = prog_idx[prog_idx != main_prog_idx]

        if merger_idx.shape[0] > 0:
            # Get the stellar masses of the progenitors at snapshot snap_nr - 1
            prev_soap = sw.load(soap_basename.format(snap_nr=snap_nr - 1))
            prev_stellar_mass = prev_soap.exclusive_sphere_50kpc.stellar_mass.to_physical_value("Msun")
            main_prog_stellar_mass = prev_stellar_mass[main_prog_idx]
            descendant_type = prev_descendant_info.soap.descendant_type.value

            for i in merger_idx:
                # The merging subhalo can be more massive than the main progenitor,
                # so always divide by the larger stellar mass
                m_low = min(prev_stellar_mass[i], main_prog_stellar_mass)
                m_high = max(prev_stellar_mass[i], main_prog_stellar_mass)
                ratio = m_low / m_high if m_high > 0 else 0
                if ratio >= major_merger_ratio:
                    n_major += 1
                    merger_class = "major"
                elif ratio >= minor_merger_ratio:
                    n_minor += 1
                    merger_class = "minor"
                else:
                    continue
                print(
                    f"  {merger_class.capitalize()} merger between snapshots {snap_nr - 1} and {snap_nr}: "
                    f"M*={prev_stellar_mass[i]:.2e} Msun, ratio={ratio:.2f}, "
                    f"{descendant_type_names[descendant_type[i]]}"
                )

        # Move to the previous snapshot
        idx = main_prog_idx
        descendant_info = prev_descendant_info

    print(f"Number of major mergers: {n_major}")
    print(f"Number of minor mergers: {n_minor}")
