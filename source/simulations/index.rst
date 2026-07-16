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

Directory symlinks
-------------------

The ``LXXX_mY`` box size/resolution names (e.g. ``L100_m6``) and the standardised
AGN feedback run names (e.g. ``THERMAL_AGN_m6``, ``HYBRID_AGN_m6``)
are symlinks rather than the real directory names. The box
size/resolution symlinks point to directories named after the particle
count, e.g. ``L100_m6 -> L0100N1504``. The AGN feedback run symlinks point
to directories whose names can vary between box sizes and resolutions,
since the ``Hybrid`` name in particular encodes the current calibration
parameters, e.g. ``HYBRID_AGN_m6 -> Hybrid_non_equilibrium_dVplus0p5dex``.

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

