Halo lightcone directory layout
===============================

Each FLAMINGO simulation has a directory ``halo_lightcones`` which
contains the lightcone halo catalogue data. Several observers were
placed in each simulation and so there is a separate subdirectory
``lightconeX`` containing the lightcone halo catalogue for each
observer ``X``.

The halo catalogue for each observer is distributed over a set of
files with names of the form ``lightcone_halos_YYYY.hdf5``. Each file
contains the halos in a shell around the observer where all of the
halos were drawn from the simulation snapshot indicated by the
``YYYY`` label. See :doc:`halo_lightcone_construction` for
details.

.. mermaid::

   flowchart LR
     lch["halo_lightcones/"]

     lch --> obs0["`**Observer 0**
     lightcone0/`"]
     lch --> obs1["`**Observer 1**
     lightcone1/`"]

     obs0 --> data0["`**Halo data**
     lightcone_halos_0000.hdf5
     lightcone_halos_0001.hdf5
     lightcone_halos_0002.hdf5
     ...`"]

     obs1 --> data1["`**Halo data**
     lightcone_halos_0000.hdf5
     lightcone_halos_0001.hdf5
     lightcone_halos_0002.hdf5
     ...`"]

As an example, see `/FLAMINGO/L1_m9/L1_m9/halo_lightcones/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9/halo_lightcones>`__
for the ``L1_m9`` halo lightcones.
