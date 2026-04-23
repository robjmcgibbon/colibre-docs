Halo catalogue directory layout
===============================

SOAP catalogues
---------------

Each simulation has a ``SOAP-HBT`` directory with one
``halo_properties_XXXX.hdf5`` file for each output time, where ``XXXX`` is
the snapshot number. See :doc:`../snapshots/snapshot_redshifts` for the relation
between snapshot number and redshift.

.. tip:: The easiest way to read the SOAP catalogues is to use
         swiftsimio so that unit metadata is read automatically. See
         :doc:`swiftsimio` for an example.

.. _hbt_directory_layout:

HBT-HERONS catalgoues
---------------------

Each simulation has an ``HBT-HERONS/sorted_catalogues`` directory with one
``OrderedSubSnap_XXX.hdf5`` file for each output time, where ``XXX`` is
the snapshot number.
