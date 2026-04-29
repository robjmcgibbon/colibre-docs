HBT-HERONS merger trees
=======================

.. note::
  To track the evolution of a galaxy (i.e. the main progenitor branch) then the full HBT-HERONS merger trees are not required.
  Each subhalo is assigned a unique ``TrackId`` which remains consistent across all snapshots,
  and this allows the quick retrieval of the main progenitor of a given subhalo.
  For example, the main progenitor of a :math:`z = 0` subhalo with ``TrackId = 10`` corresponds to the subhalo whose ``TrackId = 10`` at earlier times.
  ``TrackId`` is stored in the SOAP catalogues as ``data.input_halos_hbtplus.track_id``.
  The fields ``data.soap.progenitor_index`` and ``data.soap.descendant_index`` can also be used to track individual objects.
  Note that, due to SOAP not storing the information for subhaloes with :math:`N_{bound} < 20` (e.g. disrupted, merged or poorly resolved),
  some ``TrackId`` values will be missing from the SOAP catalogues. 
  In practice, this means there could be an object with ``TrackId = 11`` in the :math:`z = 2` catalogue,
  but no object with ``TrackId = 11`` in the :math:`z = 0` catalogue.

Full merger trees are provided in the form of HBT-HERONS
`(Forouhar Moreno et al. 2025) <https://ui.adsabs.harvard.edu/abs/2025MNRAS.543.1339F>`__
outputs. A more detailed description of the quantities, and additional examples,
can be found on the
`HBT-HERONS website. <https://hbt-herons.strw.leidenuniv.nl/>`__
The source code is available `on github
<https://github.com/SWIFTSIM/HBT-HERONS>`__, and the exact git revision which
was used to generate a subhalo catalogue can be found by inspecting the
``git_hash`` attribute of the ``Header`` group in the HDF5 output file.

The catalogues are sorted by ``TrackId``. This makes file reads for single objects fast, since the index location of a subhalo is known beforehand, as it is simply its ``TrackId``. The following properties are available for each subhalo:


.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Units
   * - ``Nbound``
     - The total number of particles bound to the subhalo.
     - :math:`-`
   * - ``Mbound``
     - The total mass of particles bound to the subhalo.
     - :math:`10^{10} \mathrm{M}_\odot`
   * - ``NboundType``
     - The total number of particles bound to the subhalo, classified according to their particle type.
     - :math:`-`
   * - ``MboundType``
     - The total mass of particles bound to the subhalo, classified according to their particle type.
     - :math:`10^{10} \mathrm{M}_\odot`
   * - ``VmaxPhysical``
     - The maximum value of the circularised rotation curve of the subhalo. The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``
     - :math:`\mathrm{km/s}`
   * - ``BoundM200Crit``
     - Mass of a region with a spherical overdensity of 200 times the critical density of the universe. Only bound mass is included and only for centrals. The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``. :ref:`Note the warning below<warning_hbt_m200>`.
     - :math:`10^{10} \mathrm{M}_\odot`
   * - ``RmaxComoving``
     - The radius at which the circularised rotation curve of the subhalo reaches its maximum value (``VmaxPhysical``). The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``
     - :math:`a\mathrm{Mpc}`
   * - ``RHalfComoving``
     - The smallest radius that encloses 50% of the total bound mass. The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``
     - :math:`a\mathrm{Mpc}`
   * - ``REncloseComoving``
     - The smallest radius that encloses 100% of the total bound mass. Useful when interested in doing spatial masking. The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``
     - :math:`a\mathrm{Mpc}`
   * - ``BoundR200CritComoving``
     - The radius of a sphere enclosing a mean density that is 200 times the critical density of the Universe. Only bound mass is included and it is only computed for centrals. The centre of the aperture used to compute this quantity corresponds to ``ComovingMostBoundPosition``. :ref:`Note the warning below<warning_hbt_m200>`
     - :math:`a\mathrm{Mpc}`
   * - ``ComovingAveragePosition``
     - Mass-weighted average position of all bound particles.
     - :math:`a\mathrm{Mpc}`
   * - ``PhysicalAverageVelocity``
     - Mass-weighted average velocity of all bound particles.
     - :math:`\mathrm{km/s}`
   * - ``ComovingMostBoundPosition``
     - Position of the most bound particle.
     - :math:`a\mathrm{Mpc}`
   * - ``PhysicalMostBoundVelocity``
     - Velocity of the most bound particle.
     - :math:`\mathrm{km/s}`
   * - ``InertialTensor``
     - Flattened representation of the inertia tensor of the subhalo.
     - :math:`a^2\mathrm{Mpc}^2`
   * - ``InertialTensorWeighted``
     - Flattened representation of the inertia tensor of the subhalo, weighted by particle mass and 3D distance to ``ComovingMostBoundPosition``
     - :math:`-`
   * - ``SpecificSelfPotentialEnergy``
     - Mass-weighted average potential energy of bound particles.
     - :math:`\mathrm{km^2/s^2}`
   * - ``SpecificSelfKineticEnergy``
     - Mass-weighted average kinetic energy of bound particles in the centre of mass reference frame of the subhalo.
     - :math:`\mathrm{km^2/s^2}`
   * - ``SpecificAngularMomentum``
     - Mass-weighted average angular momentum of bound particles in the centre of mass reference frame of the subhalo.
     - :math:`\mathrm{km/s}`
   * - ``TracerIndex``
     - Bound ranking of the most bound tracer particle.
     - :math:`-`
   * - ``MostBoundParticleId``
     - ID of the most bound particle.
     - :math:`-`
   * - ``SnapshotIndexOfBirth``
     - The output when the subhalo was first identified.
     - :math:`-`
   * - ``SnapshotIndexOfSink``
     - If the subhalo has sunk, the output when that happened. If it has not sunk, it equals -1.
     - :math:`-`
   * - ``SnapshotIndexOfDeath``
     - If the subhalo has sunk or disrupted, the output when that happened. If neither has happened, it equals -1.
     - :math:`-`
   * - ``SnapshotIndexOfLastIsolation``
     - The snapshot index of the most recent output when this subhalo was a central.
     - :math:`-`
   * - ``SnapshotIndexOfLastMaxVmax``
     - The output when the subhalo reached its maximum value of ``VmaxPhysical``.
     - :math:`-`
   * - ``SnapshotIndexOfLastMaxMass``
     - The output when the subhalo reached its maximum value of ``Mbound``.
     - :math:`-`
   * - ``LastMaxMass``
     - The maximum mass that the subhalo has reached so far.
     - :math:`10^{10} \mathrm{M}_\odot`
   * - ``LastMaxVmaxPhysical``
     - The maximum VmaxPhysical that the subhalo has reached so far.
     - :math:`\mathrm{km/s}`
   * - ``TrackId``
     - Unique identifier for the subhalo, which persists across time.
     - :math:`-`
   * - ``SinkTrackId``
     - If the subhalo has sunk, the ``TrackId`` of the subhalo that accreted it. If it has not happened, it equals -1.
     - :math:`-`
   * - ``DescendantTrackId``
     - If the subhalo has sunk or disrupted, the ``TrackId`` of the subhalo that accreted its most bound particles. If neither has happened, it equals -1.
     - :math:`-`
   * - ``NestedParentTrackId``
     - The ``TrackId`` of the parent subhalo. Central subhaloes have -1.
     - :math:`-`
   * - ``HostHaloId``
     - The Friends of Friends group that this subhalo is a part of.
     - :math:`-`
   * - ``Rank``
     - The mass ranking of the subhalo compared to all of the subhaloes that have the same ``HostHaloId``
     - :math:`-`
   * - ``Depth``
     - The number of hierarchical connections that the subhalo is away from the central, e.g. 0 for centrals, 1 for satellites, 2 for satellites of satellites.
     - :math:`-`

In order to get access to :doc:`all the halo/galaxy properties calculated by SOAP<soap_property_table>`, the two catalogues can be linked using the ``TrackId`` field, as shown in the example below.

.. _warning_hbt_m200:

.. warning:: Since the HBT-HERONS definition of spherical overdensity is based on the 
             enclosed mass of bound particles only, it does not follow the common convention in the 
             literature, which includes the mass contribution of all particles. The values
             in the SOAP catalogues should be used instead.

.. _hbt_evolution_example:

Evolution of a subhalo example
------------------------------

.. code-block:: python

    import h5py
    import matplotlib.pyplot as plt
    import numpy as np
    import swiftsimio as sw

    root_dir = '/cosma8/data/dp004/colibre/Runs'
    sim = 'L0025N0188/Thermal'
    final_snap_nr = 127

    # Load the z=0 SOAP catalogue from the L1_m9 simulation
    soap = sw.load(f"{root_dir}/{sim}/SOAP-HBT/halo_properties_{final_snap_nr:04}.hdf5")

    # Pick the most massive satellite which has lost at least 70% of its mass
    mask = soap.input_halos.is_central.value == 0
    last_max_mass_msun = soap.input_halos_hbtplus.last_max_mass.to_physical_value('Msun')
    bound_mass_msun = soap.bound_subhalo.total_mass.to_physical_value('Msun')
    mask &= (bound_mass_msun / last_max_mass_msun) < 0.3
    i = np.argmax(np.where(mask, bound_mass_msun, 0))

    # Get the TrackId of the object we have selected
    track_id = soap.input_halos_hbtplus.track_id[i].value

    # Get the first snapshot this object appeared
    birth_snap_nr = soap.input_halos_hbtplus.snapshot_index_of_birth[i].value

    # Create an array to hold the evolution
    n_exist = final_snap_nr - birth_snap_nr + 1
    mass_evolution_msun = np.zeros((n_exist, 6))
    scale_factor = np.zeros(n_exist)

    # Loop through the catalogues and extract the mass for this object
    hbt_basename = f"{root_dir}/{sim}/HBT-HERONS/sorted_hbt/OrderedSubSnap_{{snap_nr:03}}.hdf5"
    for i in range(n_exist):
        hbt_filename = hbt_basename.format(snap_nr=birth_snap_nr+i)
        with hdfstream.open('cosma', hbt_filename) as file:
            # Mass is stored in units of 10^10 Msun
            mass_evolution_msun[i] = file["Subhalos/MboundType"][track_id] * 10 ** 10
            scale_factor[i] = file['Cosmology']['ScaleFactor'][0]

    # Plot the results
    fig, ax = plt.subplots(1)
    ax.plot(scale_factor, mass_evolution_msun[:, 1], label='Dark matter', color='k')
    ax.plot(scale_factor, mass_evolution_msun[:, 0], label='Gas', color='tab:green')
    ax.plot(scale_factor, mass_evolution_msun[:, 4], label='Stars', color='tab:orange')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Scale factor')
    ax.set_ylabel('Bound mass [Msun]')
    ax.legend()
    plt.savefig('hbt_example.png')
    plt.close()

