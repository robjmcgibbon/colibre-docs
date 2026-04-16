HEALPix map directory layout
============================

Each FLAMINGO simulation has a directory ``healpix_maps`` which
contains the HEALPix map data. Maps are available at two resolutions:

  * Full resolution maps with :math:`N_\mathrm{side}=16384` in the directory ``nside_16384``
  * Lower resolution maps with :math:`N_\mathrm{side}=4096` in the directory ``nside_4096``

Within these directories there is one directory ``lightconeX_shells``
for each observer ``X``. Each of the observer directories contains
files ``lightconeX_shell_Y.0.hdf5`` with the map data for shell ``Y``.

This layout is illustrated below. We show the ``nside_16384``
directory here but the structure is the same for both resolutions.

.. mermaid::

   flowchart LR
     hm["`**Full resolution maps**
     healpix_maps/nside_16384/`"]

     hm --> hr_obs0["`**Observer 0**
     lightcone0_shells/`"]
     hm --> hr_obs1["`**Observer 1**
     lightcone1_shells/`"]

     hr_obs0 --> hr_files0_0["`**Shell 0 for observer 0**
     lightcone0.shell_0.0.hdf5`"]
     hr_obs0 --> hr_files0_1["`**Shell 1 for observer 0**
     lightcone0.shell_1.0.hdf5`"]
     hr_obs0 --> hr_files0_2["`**Shell 2 for observer 0**
     lightcone0.shell_2.0.hdf5`"]

     hr_obs1 --> hr_files1_0["`**Shell 0 for observer 1**
     lightcone1.shell_0.0.hdf5`"]
     hr_obs1 --> hr_files1_1["`**Shell 1 for observer 1**
     lightcone1.shell_1.0.hdf5`"]
     hr_obs1 --> hr_files1_2["`**Shell 2 for observer 1**
     lightcone1.shell_2.0.hdf5`"]

As an example, see `/FLAMINGO/L1_m9/L1_m9/healpix_maps/
</flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9/healpix_maps>`__
for the ``L1_m9`` HEALPix maps.
