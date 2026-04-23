Simulations
===========

Directory layout and naming conventions
---------------------------------------

All simulations are kept at ``/cosma8/data/dp004/colibre/Runs``. The simulations are divided into subdirectories based on their box size and mass resolution with names of the form ``LXXXmY``. The value of ``XXX`` corresponds to the simulation box side length in comoving Mpc, and the value of ``Y`` is the mass resolution. For example, the directory ``L100_m6`` contains all simulations run in a :math:`100\rm{Mpc}^3` box at :math:`m_{gas} \approx 10^6 \rm{M_\odot}` resolution. Within each simulation directory there are subdirectories for the available data products.

.. mermaid::

   flowchart LR
     colibre["`**Project root**
     .../colibre/Runs/`"]

     colibre --> L100_m6["`**Box size and resolution**
     L100_m6/
     L200_m6/
     ...`"]

     L100_m6-->Thermal["`**Run name**
     Thermal/
     Hybrid/
     DMO/`"]

     Thermal-->snapshots["**Snapshot data**
     snapshots/"]
     Thermal-->soap["**Halo catalogues**
     SOAP-HBT/
     HBT-HERONS/"]
     Thermal-->powerspec["**Power spectra**
     power_spectra/"]

Hydrodynamical simulations
--------------------------

Tables of the available simulations can be found on the following pages

.. toctree::
   :maxdepth: 2

   thermal
   hybrid
   high_cadence
   variation

Dark matter only simulations
----------------------------

For each hydrodynamical simulation, there is a corresponding DMO simulation that uses the same initial phases and the same total number of particles.
To create the initial conditions for the DMO simulation, baryonic particles from the corresponding hydrodynamic run were converted into CDM particles.

