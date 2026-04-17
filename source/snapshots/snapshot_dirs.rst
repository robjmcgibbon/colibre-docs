Snapshot directory layout
=========================

The layout of the snapshot files for each simulation is shown in the
diagram below. Each simulation has a ``snapshots`` directory with one
``flamingo_XXXX`` subdirectory for each output time, where ``XXXX`` is
the snapshot number. See :doc:`snapshot_redshifts` for the relation
between snapshot number and redshift.

.. tip:: The easiest way to access particle data is to use :doc:`swiftsimio
         </snapshots/swiftsimio>` to read the :ref:`virtual-snapshot`
         so that you don't need to concatenate data from multiple
         files and unit metadata is read automatically.

TODO: Update layout, tell people to use colibre_with_soap_membership

.. mermaid::

  flowchart TD
    snapshots["snapshots/"]

    snapshots --> s0000["`**Snapshot 0**
    flamingo_0000/`"]
    snapshots --> s0001["`**Snapshot 1**
    flamingo_0001/`"]

    s0000 --> s0000_v["`**Virtual snapshot**
    flamingo_0000.hdf5`"]

    s0000 --> swift_dir["`**SWIFT output**
    swift_snapshot_0000/`"]

    s0000 --> xray_dir["`**Recomputed X-rays**
    xray_0000/`"]

    s0000 --> mem_dir["`**Subhalo membership**
    membership_0000/`"]

    swift_dir --> swift_files["`**Snapshot chunks**
    flamingo_0000.0.hdf5
    flamingo_0000.1.hdf5
    ...`"]

    xray_dir --> xray_files["`**Xray chunks**
    xray_0000.0.hdf5
    xray_0000.1.hdf5
    ...`"]

    mem_dir --> mem_files["`**Membership chunks**
    membership_0000.0.hdf5
    membership_0000.1.hdf5
    ...`"]

    s0001 --> s0001_exp["..."]

As an example, see `/FLAMINGO/L1_m9/L1_m9/snapshots/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9/snapshots>`__ for
the ``L1_m9`` snapshot data.

.. _virtual-snapshot:

Virtual snapshot file
---------------------

Each snapshot directory contains a "virtual" snapshot file which has a
name of the form ``flamingo_XXXX.hdf5``. This file contains HDF5
virtual datasets which refer to particle data distributed over a
number of additional HDF5 files in the same directory. This file can
be treated as a single, large snapshot file which contains all of the
particles.

Snapshot data files
-------------------

The virtual snapshot file does not contain any particle data itself.
Instead, the data for each snapshot is split across three (two for DMO)
sets of HDF5 files: the SWIFT output, recomputed X-rays,
and subhalo membership information. Within these sets, the files follow
naming conventions such as ``flamingo_XXXX.Y.hdf5``, where ``XXXX`` is
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


