Halo lightcones
===============

Lightcone halo catalogues extending to redshift :math:`z=15` have been
constructed by interpolating the HBT-HERONS halo catalogues between
snapshots using black hole particles as tracers of the halo
positions. Note that this causes incompleteness below the minimum halo
mass for seeding black holes. The seeding mass varies with simulation
resolution and is given by

  :math:`\mathrm{M_{seed}} = 2.757 \times 10^{11} \mathrm{M}_\odot \frac{\mathrm{M_{gas}}}{1.07 \times 10^9 \mathrm{M}_\odot}`

where :math:`\mathrm{M_{gas}}` is the gas particle mass. In addition,
any galaxies that have lost their black holes, which is particularly
relevant for satellites, are missing.  See the links below for
details.

.. toctree::
   :maxdepth: 2

   Construction <halo_lightcone_construction>
   Directory layout <halo_lightcone_layout>
   File format <halo_lightcone_format>
   Reading the halos <reading_halos>

.. note:: If you wish to use the halo lightcones in conjunction with
          the :doc:`integrated maps <integrated_lightcones>`, you need
          to ensure you :ref:`apply the same rotations<map_rotations>`
