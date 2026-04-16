Construction of the halo lightcones
===================================

For comparison with observations it is useful to create a "lightcone"
halo catalogue where each halo is seen at the time it crossed the
observer's past lightcone. Ideally this would be done by running a
halo finder on the :doc:`lightcone particle
output</lightcones/particle_lightcones>`, but this was not implemented
in FLAMINGO.

Approximate lightcone halo catalogues can be constructed by running a
halo finder on all of the simulation snapshots and then interpolating
halo positions between snapshots to determine when any periodic copy
of a halo crosses the past lightcone of the observer. The FLAMINGO
simulation snapshots are too widely spaced for accurate interpolation,
but we can use black hole particles from the lightcone particle
outputs as tracers of halo positions.

Snapshots and redshift shells
-----------------------------

We divide the redshift range :math:`0 < z < 15` into spherical shells
corresponding to the simulation snapshots. The mid point of each shell
lies at the snapshot redshift and its inner and outer edges lie half
way to the next and previous snapshot redshifts respectively. Each
shell will be populated with halos drawn from the corresponding
snapshot. These shells are illustrated below.

.. warning:: These are not the same as the shells used to construct the
             :doc:`HEALPix maps <healpix_lightcones>`.

.. card::
   :img-top: images/lightcone_shells.png

   Redshift shells used in the construction of the lightcone halo
   catalogue for ``L1_m9``. Only low redshifts are shown for clarity.

Matching halos to the black hole particle lightcone
---------------------------------------------------

The halo catalogue for a particular shell is constructed by matching
between two datasets:

  * The HBT-HERONS halo catalogue for the shell's corresponding snapshot
  * The black hole particles in the shell's redshift range in the
    particle lightcone

For each halo in the snapshot halo catalogue we pick a black hole
particle to serve as a tracer of that halo. Wherever that black hole
particle appears in the particle lightcone within the shell's redshift
range we place a copy of the halo. We repeat this for every shell to
build up a lightcone halo catalogue that extends to :math:`z=15`.

This method only works for halos which contain at least one black hole
particle. All halos below the black hole seeding mass are likely to be
missing from the lightcone catalogue. Black holes are seeded in halos
with masses greater than

  :math:`\mathrm{M_{seed}} = 2.757 \times 10^{11} \mathrm{M}_\odot \frac{\mathrm{M_{gas}}}{1.07 \times 10^9 \mathrm{M}_\odot}`

where :math:`\mathrm{M_{gas}}` is the gas particle mass. The black
hole seeding masses for the fiducial hydro simulations are shown
below:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Simulation
     - :math:`\mathrm{M_{seed} [M_\odot}]`
   * - ``L1_m8``
     - :math:`3.44 \times 10^{10}`
   * - ``L1_m9``
     - :math:`2.76 \times 10^{11}`
   * - ``L1_m10``
     - :math:`2.21 \times 10^{12}`

Some halos above the seeding mass, such as satellite subhalos, may
lose their central black hole in some cases and also not appear in the
halo lightcone.

Choice of tracer particle
-------------------------

The most bound black hole particle in each halo is the obvious choice
to trace the position of the halo over time. However, in FLAMINGO
black hole particles can be destroyed by merging with another black
hole particle. It's also possible for the most bound black hole in a
halo to have formed recently. If the black hole particle which is most
bound at the time of the snapshot does not exist at the time the halo
crossed the lightcone, then that halo will not appear in the lightcone
halo catalogue.

We choose the tracer particle to be the most bound black hole from one
of the following subsets, in descending order of priority:

  * Black hole particles which exist in the next and previous snapshots
  * Black hole particles which exist in the next snapshot
  * Black hole particles which exist in the previous snapshot
  * Any other black hole particles

This is to maximize completeness by avoiding tracers which might cease
to exist by the time of lightcone crossing.
