Directory layout
================

The simulations are divided into subdirectories based on their box
size and mass resolution. For example, the directory `/FLAMINGO/L1_m9
</flamingo/viewer.html?path=/FLAMINGO/L1_m9>`__ contains all
simulations run in a 1Gpc box at ``m9`` resolution. Within each
simulation directory there are subdirectories for the available data
products: :doc:`snapshots </snapshots/index>`, :doc:`power spectra
</power_spectra>`, :doc:`halo catalogues </soap/index>` and
:doc:`lightcone outputs </lightcones/index>`.

.. mermaid::

   flowchart LR
     flamingo["`**Project root**
     FLAMINGO/`"]

     flamingo --> L1_m9["`**Box size and resolution**
     L1_m9/`"]
     L1_m9-->L1_m9_fiducial["`**Run name**
     L1_m9/`"]

     L1_m9_fiducial-->snapshots["**Snapshot data**
     snapshots/
     snapshots_reduced/
     snapshots_downsampled/"]
     L1_m9_fiducial-->soap["**Halo catalogues**
     SOAP-HBT/
     HBT-HERONS/"]
     L1_m9_fiducial-->powerspec["**Power spectra**
     power_spectrum/"]
     L1_m9_fiducial-->particle_lc["**Lightcone data**
     particle_lightcones/
     healpix_maps/
     halo_lightcone/
     integrated_maps/"]
