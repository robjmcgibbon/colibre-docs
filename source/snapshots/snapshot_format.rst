Snapshot file format
====================

Here we describe the basic features of COLIBRE snapshots. For full
details of the SWIFT simulation format, see the `SWIFT documentation
<https://swift.strw.leidenuniv.nl/docs/Snapshots/index.html>`__.

Simulation metadata
-------------------

General information about the snapshot is stored in the form of
attributes attached to HDF5 groups in each snapshot file.

Header
^^^^^^

Snapshots contain a ``Header`` group which contains similar
information to the header in Gadget-2 snapshots. Some of the more
useful attributes are:

.. list-table::
   :header-rows: 1

   * - Attribute name
     - Description
   * - ``Redshift``
     - Redshift of this snapshot
   * - ``Scale-factor``
     - Expansion factor at this snapshot
   * - ``BoxSize``
     - Size of the box in each dimension (COLIBRE runs are all cubic boxes)
   * - ``NumFilesPerSnapshot``
     - Number of files in the snapshot. Always 1 for virtual snapshots.

Code version
~~~~~~~~~~~~

The ``Code`` group contains attributes which can be used to determine
the precise version of SWIFT which was used to run the simulation.

.. list-table::
   :header-rows: 1

   * - Attribute name
     - Description
   * - ``Code Version``
     - SWIFT code version number, as a string
   * - ``Git Branch``
     - Name of the git branch which was used
   * - ``Git Revision``
     - Identifies the exact git revision which was used
   * - ``Git Date``
     - Date associated with this revision
   * - ``Configuration options``
     - Configure script flags which were used for this run

Cosmology
^^^^^^^^^

The ``Cosmology`` group stores the values of the cosmological
parameters used in the simulation and the redshift of the snapshot
output. It includes the following HDF5 attributes:

.. list-table::
   :header-rows: 1

   * - Attribute name
     - Description
   * - ``Redshift``
     - Redshift of this snapshot
   * - ``Scale-factor``
     - Expansion factor at this snapshot
   * - ``Omega_b``
     - Baryon density parameter :math:`\Omega_\mathrm{b}` at z=0
   * - ``Omega_cdm``
     - Cold dark matter density parameter :math:`\Omega_{\mathrm{cdm}}` at z=0
   * - ``Omega_lambda``
     - Dark energy density parameter :math:`\Omega_{\mathrm{\Lambda}}` at z=0
   * - ``Omega_m``
     - Matter density parameter :math:`\Omega_\mathrm{m} = \Omega_{\mathrm{cdm}} + \Omega_\mathrm{b}` at z=0
   * - ``Omega_nu``
     - Neutrino density parameter :math:`\Omega_{\mathrm{\nu}}` at the snapshot redshift
   * - ``Omega_nu_0``
     - Neutrino density parameter :math:`\Omega_{\mathrm{\nu}}` at z=0
   * - ``Omega_r``
     - Radiation density parameter :math:`\Omega_\mathrm{r}` at z=0
   * - ``Omega_k``
     - Curvature density parameter :math:`\Omega_\mathrm{k}` at z=0

.. note:: `swiftsimio
          <https://swiftsimio.readthedocs.io/en/latest/loading_data/index.html>`__
          can create a suitable `astropy <https://www.astropy.org/>`__
          cosmology object from the snapshot metadata. This is the
          safest way to convert redshifts to comoving distances or
          lookback times, for example.

Units
^^^^^

The ``Units`` group describes the system of units used in the
snapshot. It defines basic units of length, mass, time and temperature
in terms of CGS units. Most quantities in the snapshot are expressed
in combinations of these base units. In COLIBRE, the base units used
are as follows:

.. list-table::
   :header-rows: 1

   * - Dimension
     - Unit
   * - Length
     - :math:`\mathrm{Mpc}`
   * - Mass
     - :math:`10^{10}\mathrm{M}_{\odot}`
   * - Time
     - :math:`\mathrm{Mpc} \mathrm{(km/s)}^{-1}`
   * - Temperature
     - :math:`\mathrm{K}`

A few attributes in the snapshot file are expressed in the "internal"
system of units used to run the simulation. This unit system is
described in the ``InternalCodeUnits`` group. In COLIBRE, the
snapshot and internal unit systems are the same.

The exact units used for each particle property are documented in
:doc:`snapshot_particle_properties`.

Particle types
--------------

The COLIBRE simulations contain gas, dark matter, star, black hole
and neutrino particles. There is an HDF5 group for each particle
type. Within these groups particle properties (position, mass,
velocity etc) are stored as HDF5 datasets. The particle type groups
follow Gadget-2's ``PartTypeX`` naming scheme but there are also
symbolic links to the groups with more descriptive names.

.. list-table::
   :header-rows: 1

   * - Particle type
     - HDF5 group name
     - Link name
   * - Gas particles
     - ``PartType0``
     - ``GasParticles``
   * - Dark matter particles
     - ``PartType1``
     - ``DMParticles``
   * - Star particles
     - ``PartType4``
     - ``StarsParticles``
   * - Black hole particles
     - ``PartType5``
     - ``BHParticles``
   * - Neutrino particles
     - ``PartType6``
     - ``NeutrinoParticles``

The quantities stored for each particle type are described in :doc:`snapshot_particle_properties`.

Particle datasets
-----------------

Each particle property (position, mass, velocity etc) is stored as a
separate dataset in the particle type group. For scalar quantities,
such as the particle mass, the dataset has one element per
particle. For vector quantities, the first index is the particle index
and the second index is the x/y/z dimension.

Datasets have a ``Description`` attribute which gives a short
description of their contents.

.. _dataset-units:

Dataset units
^^^^^^^^^^^^^

All datasets are stored in units which are constructed by multiplying
together (usually integer) powers of the base units described
above. Each dataset has attributes which store the exponent of each
base unit for that quantity.

.. list-table::
   :header-rows: 1

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
     - Exponent of the current unit (not used in COLIBRE)

For example, particle velocities have ``U_L exponent`` = 1 and
``U_t exponent`` = -1.

Some quantities are stored in comoving coordinates. We therefore also
include an attribute ``a-scale exponent`` which stores the exponent of
the cosmological expansion factor :math:`a` which is required to
convert the dataset to physical coordinates. Quantities which are
already in physical coordinates have ``a-scale exponent`` = 0. Comoving
particle positions have ``a-scale exponent`` = 1.

There is also a ``h-scale exponent`` attribute which indicates when
units contain powers of the Hubble parameter, :math:`h`. This is
always zero in COLIBRE. Particle positions are stored in
:math:`\mathrm{Mpc}` and not :math:`\mathrm{Mpc/h}`, for example.

There are also attributes which directly give the conversion factor to
CGS, with and without any :math:`a` factors included.

Compression
^^^^^^^^^^^

Many COLIBRE datasets use lossy compression to save disk space when
very precise values are not required. This is indicated by the ``Lossy
compression filter`` attribute. The possible values of this attribute
are:

.. list-table::
   :header-rows: 1

   * - Filter name
     - Description
   * - None
     - No lossy compression has been applied to this dataset
   * - HalfFloat
     - Float numbers with 10-bits mantissa and 5-bits exponent. Accurate to about 3 decimal digits but with limited range 6.1e-5 to 6.5e4.
   * - BFloat16
     - Floating point numbers with 7-bits mantissa and 8-bits exponent. Accurate to about 2.4 decimal digits and has the same range as a 32 bit float.
   * - FMantissa9
     - Floating point numbers with 9-bits mantissa and 8-bits exponent. Accurate to about 3 decimal digits and has the same range as a 32 bit float.
   * - DMantissa9
     - Floating point numbers with 9-bits mantissa and 11-bits exponent. Accurate to about 3 decimal digits and has the same range as a 64 bit double.
   * - DScale1
     - Stores floating point data accurate to 1 decimal place by multiplying by 10 and storing as an integer
   * - DScale5
     - Stores floating point data accurate to 5 decimal places by multiplying by :math:`10^5` and storing as an integer
