Halo lightcone file format
==========================

Each halo lightcone file contains the halos in a single redshift
shell. These halos were drawn from a single simulation snapshot and
positioned on the lightcone using black hole particles as tracers, as
described in :doc:`halo_lightcone_construction`.

The lightcone halo catalogues contain only a minimal set of halo
properties to save disk space. Indexes into the HBT-HERONS and SOAP
outputs are provided to allow looking up additional halo
properties. The halo lightcones are stored in HDF5 files with the
contents described below.

.. tip:: The `lightcone_io
         <https://lightconeio.readthedocs.io/en/latest/>`__ python
         module can read these halo catalogues and cross reference
         with SOAP to look up additional halo properties. It can also
         use the :ref:`spatial ordering
         <lightcone_halo_spatial_index>` of the catalogues to cut out
         regions on the sky. See :doc:`reading_halos`.

Halo properties from the input halo catalogue
---------------------------------------------

The HDF5 group ``InputHalos`` contains some information passed through
from the input HBT-HERONS catalogue for the snapshot that was used to
populate this redshift shell. Datasets in this group have an entry for
every halo in this lightcone shell. I.e. the size of the dataset in
the first dimension is equal to the number of halos in the lightcone
in the redshift range covered by this file.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Type
     - Shape
     - Units
     - Description
   * - ``HBTplus/TrackId``
     - int64
     - N
     - :math:`-`
     - Track identifier assigned by HBT-HERONS. Note that periodic
       replications of the same TrackId may appear in different parts
       of the lightcone.
   * - ``HaloCatalogueIndex``
     - int64
     - N
     - :math:`-`
     - Index of the halo in the HBT-HERONS output used to construct
       the lightcone. The first halo is 0.
   * - ``HaloCentre``
     - float64
     - N,3
     - :math:`a\mathrm{Mpc}`
     - The position of the halo centre given by the halo finder. Note
       that this is the position in the snapshot and NOT a position in
       the lightcone.
   * - ``IsCentral``
     - int64
     - N
     - :math:`-`
     - Indicates if the halo is central (1) or satellite (0).
   * - ``NumberOfBoundParticles``
     - int64
     - N
     - :math:`-`
     - Number of bound particles in the halo.
   * - ``SOAPIndex``
     - int64
     - N
     - :math:`-`
     - Index of the halo in the input SOAP catalogue. The first halo is 0.

The HDF5 group ``BoundSubhalos`` contains additional halo properties
passed through from SOAP. In FLAMINGO this is just the total bound mass.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Type
     - Shape
     - Units
     - Description
   * - ``TotalMass``
     - float64
     - N
     - :math:`-`
     - Total mass of the bound particles in the halo.

Halo properties specific to the lightcone
-----------------------------------------

The HDF5 group ``Lightcone`` contains information about where and when
each halo crossed the observer's lightcone. As before, these datasets
have one entry for each halo in the lightcone in this file's redshift
range.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Type
     - Shape
     - Units
     - Description
   * - ``HaloCentre``
     - float64
     - N,3
     - :math:`a\mathrm{Mpc}`
     - Coordinates of the halo relative to the observer at the time of lightcone crossing.
   * - ``Redshift``
     - float64
     - N
     - :math:`-`
     - Redshift of the halo at the time of lightcone crossing.
   * - ``SnapshotNumber``
     - int64
     - N
     - :math:`-`
     - Snapshot which this halo was taken from. All halos in the same file have the same value.

.. _lightcone_halo_spatial_index:

Spatial indexing
----------------

The HDF5 group ``Index`` contains information that can be used to look
up halos according to their position on the sky. Each halo is assigned
a HEALPix pixel index. We sort the halos in each file by their pixel
index and for each pixel we store the index of the first halo in that
pixel and the number of halos in the pixel.

The ``Index`` group has attributes ``nside`` and ``order`` which
specify the resolution of the HEALPix map used for indexing and the
pixel ordering ("ring" or "nest"). It also contains the following
datasets with one element for each HEALPix pixel:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Type
     - Description
   * - ``FirstHaloInPixel``
     - int64
     - Index of the first halo in each pixel.
   * - ``NumHalosInPixel``
     - int64
     - Number of halos in each pixel.

