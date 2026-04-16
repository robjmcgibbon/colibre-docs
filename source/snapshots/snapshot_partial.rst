Partial snapshots
=================

Alongside the full particle snapshots, we have retained partial snapshots for all of the original outputs (see :doc:`snapshot_redshifts` for the list). There are two kinds of partial snapshots. Both kinds have the same file format as the original snapshots, and can be opened using
`swiftsimio
<https://swiftsimio.readthedocs.io/en/latest/loading_data/index.html>`__.

Downsampled snapshots
---------------------

For the downsampled snapshots at each output we select a random 1% of particles to keep (not the same 1% for each output). All black hole particles have been retained. The following fields are available for each particle type, with the description for each the same as in the
:doc:`full snapshots <snapshot_particle_properties>`.

.. note:: Masses (except for black hole masses) have been rescaled by a factor of 100 to conserve the total mass within the snapshot.

.. list-table::
   :header-rows: 1

   * - Particle Type
     - Included Fields
   * - Gas
     - ``ComptonYParameters``, ``Coordinates``, ``Masses``, ``Velocities``
   * - Dark matter
     - ``Coordinates``, ``Masses``, ``Velocities``
   * - Stars
     - ``Coordinates``, ``Masses``, ``Velocities``
   * - Black holes
     - ``Coordinates``, ``DynamicalMasses``, ``SubgridMasses``, ``Velocities``
   * - Neutrinos
     - ``Coordinates``, ``Masses``, ``SampledSpeeds``, ``Velocities``, ``Weights``

Downsampled snapshots are not available for the ``L1_m9``, ``L1_m9_DMO``, ``L1_m10``, and ``L1_m10_DMO`` runs (since the full snapshots are available for all outputs). Downsampled snapshots are also not available for the ``L1_m8`` and ``L1_m8_DMO`` simulations (as downsampling the high resolution runs effectively gives you the low resolution runs).

As an example, see `/FLAMINGO/L1_m9/Planck/snapshots_downsampled/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/Planck/snapshots_downsampled>`__ for
the ``Planck`` simulation snapshot data.

Reduced snapshots
-----------------

The reduced snapshots contains all the particles within the :math:`R_{100c}` radius of a selection of massive halos. Within the SOAP catalogues each subhalo has a flag ``SOAP/IncludedInReducedSnapshot`` which indicates whether its particles are included in the reduced snapshot. To pick these halos we define a set of :math:`M_{200c}` halo mass bins of width 0.05 dex, with the lowest mass bin starting at :math:`M_{200c}=10^{13} M_\odot`. If a bin has less than 200 halos then we include all of them in the reduced snapshot, if not then we include a random 200.

All of the properties available in the :doc:`full snapshots <snapshot_particle_properties>` are present in the reduced snapshots.

Reduced snapshots are not available for the ``L1_m9``, ``L1_m9_DMO``, ``L1_m10``, and ``L1_m10_DMO`` runs (since the full snapshots are available for all outputs).

As an example, see `/FLAMINGO/L1_m9/Planck/snapshots_reduced/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/Planck/snapshots_reduced>`__ for
the ``Planck`` simulation snapshot data.
