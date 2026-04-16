HEALPix map file format
=======================

The HEALPix maps are stored in HDF5 files with one file for each
redshift shell. Each map is stored as a single HDF5 dataset in the
file's root group. For descriptions of the available maps see
:doc:`healpix_map_descriptions`.

Shell metadata
--------------

Each file has a ``Shell`` group with attributes specifying the extent
of the shell:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Attribute name
     - Meaning
   * - ``comoving_inner_radius``
     - Inner radius of the shell, in comoving Mpc.
   * - ``comoving_outer_radius``
     - Outer radius of the shell, in comoving Mpc.
   * - ``nr_files_per_shell``
     - How many files the maps are split over. This is always 1 in the FLAMINGO data release.

See :doc:`healpix_shell_redshifts` for a full list of shell redshifts and comoving radii.

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

Map datasets
------------

Each map is stored as a one dimensional HDF5 dataset of 64-bit
floating point type with one element per pixel. See
:doc:`healpix_map_descriptions` for the full list of maps. The map
datasets have the following attributes:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Attribute name
     - Attribute description
   * - ``comoving_inner_radius``
     - Inner radius of the shell, in comoving Mpc.
   * - ``comoving_outer_radius``
     - Outer radius of the shell, in comoving Mpc.
   * - ``nside``
     - HEALPix resolution parameter for the map
   * - ``number_of_pixels``
     - Number of pixels in the map. Equal to the dataset size.
   * - ``pixel_ordering_scheme``
     - HEALPix pixel ordering. Always "ring" in the FLAMINGO data release.
   * - ``U_L exponent``
     - Exponent of the simulation base length unit in the units of this map
   * - ``U_M exponent``
     - Exponent of the simulation base mass unit in the units of this map
   * - ``U_T exponent``
     - Exponent of the simulation base temperature unit in the units of this map
   * - ``U_t exponent``
     - Exponent of the simulation base time unit in the units of this map
   * - ``U_I exponent``
     - Exponent of the current unit (not used in FLAMINGO)

The ``U_*`` exponent attributes specify the units of each map the same
way as in the :ref:`snapshots <dataset-units>`.
