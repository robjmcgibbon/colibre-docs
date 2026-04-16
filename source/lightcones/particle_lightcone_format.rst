Particle lightcone file format
==============================

This page describes the format of the particle lightcone outputs. The
particles for each lightcone observer are split across a number of
HDF5 files. For full details of all of the available particle
properties see :doc:`particle_lightcone_properties`.

.. tip:: The `lightcone_io
         <https://lightconeio.readthedocs.io/en/latest/>`__ python
         module can be used to read particle lightcone data without
         needing to know the file format details below. It also
         implements efficient retrieval of particles in specific
         redshift ranges or positions on the sky.


Lightcone metadata
------------------

Each file contains a HDF5 group ``Lightcone``, which has attributes
with general information about the output. These include:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Attribute name
     - Meaning
   * - ``nr_mpi_ranks``
     - Number of files in the set.
   * - ``mpi_rank``
     - Index of this file within the set.
   * - ``observer_position``
     - Three element array with the observer position in the simulation box at :math:`z=0`, in comoving :math:`\mathrm{Mpc}`.
   * - ``maximum_redshift_Gas``
     - Maximum redshift at which gas particles were output
   * - ``maximum_redshift_DM``
     - Maximum redshift at which dark matter particles were output
   * - ``maximum_redshift_Stars``
     - Maximum redshift at which star particles were output
   * - ``maximum_redshift_BH``
     - Maximum redshift at which black hole particles were output
   * - ``maximum_redshift_Neutrino``
     - Maximum redshift at which neutrino particles were output

Unit system
-----------

Each file has a HDF5 group ``Units`` with attributes specifying the
simulation base units used, which are the same as in the snapshots:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Attribute name
     - Meaning
     - Value in FLAMINGO
   * - ``Unit length in cgs (U_L)``
     - Simulation base length unit in CGS
     - :math:`\mathrm{Mpc}`
   * - ``Unit mass in cgs (U_M)``
     - Simulation base mass unit in CGS
     - :math:`10^{10}\mathrm{M}_{\odot}`
   * - ``Unit time in cgs (U_M)``
     - Simulation base time unit in CGS
     - :math:`\mathrm{Mpc} \mathrm{(km/s)}^{-1}`
   * - ``Unit temperature in cgs (U_M)``
     - Simulation base temperature unit in CGS
     - :math:`\mathrm{K}`


Particle types
--------------

Each file contains one HDF5 group for each particle type. These are:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Group name
     - Particle type
   * - ``Gas``
     - Gas particles
   * - ``DM``
     - Dark matter particles
   * - ``Stars``
     - Star particles
   * - ``BH``
     - Black hole particles
   * - ``Neutrino``
     - Neutrino particles

Not all particle types were output in all simulations or for all
observers, so some groups may be absent in some cases.

Particle datasets
-----------------

Each :doc:`particle property <particle_lightcone_properties>`
(position, mass, velocity etc) is stored as a separate dataset in the
particle type group. For scalar quantities, such as the particle mass,
the dataset has one element per particle. For vector quantities, the
first index is the particle index and the second index is the x/y/z
dimension.

The lightcone particle datasets have the following attributes:

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Attribute name
     - Attribute description
   * - ``U_L exponent``
     - Exponent of the length unit
   * - ``U_M exponent``
     - Exponent of the mass unit
   * - ``U_T exponent``
     - Exponent of the temperature unit
   * - ``U_t exponent``
     - Exponent of the time unit
   * - ``U_I exponent``
     - Exponent of the current unit (not used in FLAMINGO)

The ``U_*`` exponent attributes specify the units of each quantity in
the same way as in the :ref:`snapshots <dataset-units>`.

.. note:: the conversion factor to physical CGS units is not given as
          an attribute here because different particles in the dataset
          crossed the lightcone at different times and therefore have
          different values of :math:`a`.

Spatial indexing
----------------

The comoving volume of the lightcone increases rapidly with redshift
so the number of particles in the outputs can be very large. We
organize the lightcone particle files to allow efficient retrieval of
particles in specified redshift ranges or positions on the sky. This
is similar to the spatial indexing scheme used in the snapshots but
adapted to spherical coordinates.

The volume within the maximum redshift of the lightcone is divided
into concentric spherical shells. The thickness of these shells is
chosen such that each shell contains approximately the same number of
particles. We divide each shell into pixels using a low resolution
HEALPix map. This has the effect of dividing the lightcone volume into
cells which are identified their shell and pixel index.

The particles in the lightcone are then sorted by shell index and
particles with the same shell index are sorted by pixel index within
the shell. In each lightcone file we store the offset to the first
particle in each cell and the number of particles in each cell. If we
wish to find particles in a particular redshift range and/or position
on the sky we can compute which cells overlap the required volume and
look up which ranges of particles to read.

Each file has a HDF5 group ``Cells`` which contains this spatial
indexing information. Each particle type is indexed separately, so the
``Cells`` group contains one sub-group for each particle type with
the following information:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Dataset name
     - Meaning
   * - ``cell_length``
     - Total number of particles in each cell.
   * - ``cell_offset``
     - Offset to the first particle in each cell. If there are a total
       of :math:`N` particles across all files in the set, then offset
       :math:`0` is the first particle in the first file and offset
       :math:`N-1` is the last particle in the last file.
   * - ``cell_pixel``
     - The HEALPix pixel index of each cell.
   * - ``cell_z_min``
     - The minimum redshift of each cell.
   * - ``cell_z_max``
     - The maximum redshift of each cell.
   * - ``first_particle_in_file``
     - The offset to the first particle in each file, defined in the
       same way as ``cell_offset``. Has one element for each file in
       the set.
   * - ``num_particles_in_file``
     - The number of particles in each file. Has one element for each
       file in the set.
   * - ``num_cells``
     - The total number of cells across all files. Equal to the number
       of HEALPix pixels times the number of redshift cells. This is
       the size of the ``cell_*`` datasets.
   * - ``redshift_bins``
     - The edges of the redshift bins used in this output. If
       :math:`N` redshift shells were used this has :math:`N+1`
       elements.
   * - ``redshift_first``
     - Specifies the sorting order of the particles. If 1, particles
       are sorted by redshift shell index and then by pixel index
       within the shell. If 0, particles are sorted by pixel index and
       then by redshift shell index within the pixel.
   * - ``nside``
     - Specifies the resolution of the HEALPix map used for spatial
       indexing.
   * - ``order``
     - Specifies the pixel ordering used: either ``ring`` or ``nest``.
