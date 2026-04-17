Snapshot directory layout
=========================

The layout of the snapshot files for each simulation is shown in the
diagram below. The ``snapshots`` directory is output by SWIFT, with one
``colibre_XXXX`` subdirectory for each output time, where ``XXXX`` is
the snapshot number.
See :doc:`snapshot_redshifts` for the relation
between snapshot number and redshift.
The ``SOAP-HBT`` directory contains particle membership
information (what subhalo each particle is bound to).

.. tip:: The easiest way to access particle data is to use :doc:`swiftsimio
         </snapshots/swiftsimio>` to read the :ref:`virtual-snapshot`
         so that you don't need to concatenate data from multiple
         files and unit metadata is read automatically.

.. mermaid::

  flowchart LR
    run["`**Run directory**
    `"]

    run --> snapshots["`**Snapshots**
    snapshots/`"]

    snapshots --> s0000["`**Snapshot 0**
    colibre_0000/`"]

    s0000 --> swift_files["`**Snapshot chunks**
    colibre_0000.0.hdf5
    colibre_0000.1.hdf5
    ...`"]

    s0000 --> s0000_v["`**Virtual snapshot**
    colibre_0000.hdf5`"]

    run --> soap["`**SOAP**
    SOAP-HBT/`"]

    soap --> soap_v["`**Virtual snapshot**
    colibre_with_soap_membership_0000.hdf5`"]

    soap --> m0000["`**Membership 0**
    membership_0000/`"]

    m0000 --> membership["`**Membership chunks**
    membership_0000.0.hdf5
    membership_0000.1.hdf5
    ...`"]


.. _virtual-snapshot:

Virtual snapshot file
---------------------

The ``SOAP-HBT`` directories contains "virtual" snapshot files which have
names of the form ``colibre_with_soap_membership_XXXX.hdf5``. 
These files contains HDF5
virtual datasets which refer to particle data distributed over a
number of additional HDF5 files. This file can
be treated as a single, large snapshot file which contains all of the
particle properties.

Each snapshot directory (``snapshots/colibre_XXXX``) also contains a virtual 
snapshot file named ``colibre_XXXX.hdf5``. This 
should only be used if the ``colibre_with_soap_membership_XXXX.hdf5`` file
is missing, since it does not contain subhalo membership information.

Snapshot data files
-------------------

The virtual snapshot file does not contain any particle data itself.
Instead, the data for each snapshot is split across two
sets of HDF5 files: the SWIFT output
and subhalo membership information. Within these sets, the files follow
naming conventions such as ``colibre_XXXX.Y.hdf5``, where ``XXXX`` is
the snapshot number and ``Y`` numbers the files that make up the snapshot.
Each one of these files contains the properties of particles for part of
the simulation volume. To read the complete data for a snapshot, it is necessary
to read from all of the files in the corresponding set.

If you download the virtual snapshot file, it will only be readable
if you also download all the snapshot data files and
maintain the original directory structure.

.. warning:: If HDF5 can't find the data for a virtual dataset, it
   silently returns incorrect "fill" values! So if you download a
   virtual snapshot and get strange results, it may be that HDF5 isn't
   finding the real data files.


