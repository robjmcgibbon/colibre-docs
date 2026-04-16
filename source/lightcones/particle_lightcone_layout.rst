Particle lightcone directory layout
===================================

Each FLAMINGO simulation has a directory ``particle_lightcones`` which
contains the particle lightcone data. Several observers were placed in
each simulation and so there is a separate subdirectory
``lightconeX_particles`` containing the lightcone particle data for
each observer ``X``.

The particles for each observer are distributed over a set of files
``lightconeX_0000.Y.hdf5``, where the integer ``Y`` numbers the files
within the set. As with the :ref:`snapshots <virtual-snapshot>`, there
is also a file containing HDF5 virtual datasets which refer to the
data in all of the separate data files. This can be treated as a
single, large file containing all of the data. It has a name of the
form ``lightconeX_0000.hdf5``.

This structure is illustrated below.

.. mermaid::

   flowchart LR
     lcp["particle_lightcones/"]

     lcp --> obs0["`**Observer 0**
     lightcone0_particles/`"]
     lcp --> obs1["`**Observer 1**
     lightcone1_particles/`"]

     obs0 --> virt0["`**Virtual file**
     lightcone0_0000.hdf5`"]

     obs0 --> data0["`**Lightcone chunks**
     lightcone0_0000.0.hdf5
     lightcone0_0000.1.hdf5
     lightcone0_0000.2.hdf5
     ...`"]

     obs1 --> virt1["`**Virtual file**
     lightcone1_0000.hdf5`"]

     obs1 --> data1["`**Lightcone chunks**
     lightcone1_0000.0.hdf5
     ...`"]

As an example, see `/FLAMINGO/L1_m9/L1_m9/particle_lightcones/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9/particle_lightcones>`__
for the ``L1_m9`` particle lightcones.
