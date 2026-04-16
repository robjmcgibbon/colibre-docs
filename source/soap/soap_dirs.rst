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

As an example, see `/FLAMINGO/L1_m9/L1_m9/SOAP-HBT/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9/SOAP-HBT>`__ for
the ``L1_m9`` SOAP catalogues.


.. _hbt_directory_layout:

HBT-HERONS catalgoues
---------------------

Each simulation has an ``HBT-HERONS`` directory with one
``OrderedSubSnap_XXX.hdf5`` file for each output time, where ``XXX`` is
the snapshot number.

As an example, see `/FLAMINGO/L1_m9/L1_m9/HBT-HERONS/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9/HBT-HERONS>`__ for
the ``L1_m9`` HBT-HERONS catalogues.

