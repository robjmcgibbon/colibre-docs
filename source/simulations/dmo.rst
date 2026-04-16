Dark matter only simulations
============================

The tables below list all of the dark matter only simulations which
are part of the FLAMINGO data release and provide a link to the
simulation data.

For exact model parameters see the `table of FLAMINGO simulations
<https://flamingo.strw.leidenuniv.nl/simulations.html>`__.

Fiducial models
---------------

These simulations use the fiducial cosmological model.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Simulation name
     - Path to data
     - Description
   * - ``L1_m8_DMO``
     - `FLAMINGO/L1_m8/L1_m8_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m8/L1_m8_DMO>`__
     - Fiducial model in a 1Gpc box at high (``m8``) resolution
   * - ``L1_m9_DMO``
     - `FLAMINGO/L1_m9/L1_m9_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9_DMO>`__
     - Fiducial model in a 1Gpc box at intermediate (``m9``) resolution
   * - ``L1_m10_DMO``
     - `FLAMINGO/L1_m10/L1_m10_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m10/L1_m10_DMO>`__
     - Fiducial model in a 1Gpc box at low (``m10``) resolution
   * - ``L2p8_m9_DMO``
     - `FLAMINGO/L2p8_m9/L2p8_m9_DMO </flamingo/viewer.html?path=/FLAMINGO/L2p8_m9/L2p8_m9_DMO>`__
     - Fiducial model in a 2.8Gpc box at intermediate (``m9``) resolution
   * - ``L5p6_m10_DMO``
     - `FLAMINGO/L5p6_m10/L5p6_m10_DMO </flamingo/viewer.html?path=/FLAMINGO/L5p6_m10/L5p6_m10_DMO>`__
     - Fiducial model in a 5.6Gpc box at low (``m10``) resolution
   * - ``L11p2_m11_DMO``
     - `FLAMINGO/L11p2_m11/L11p2_m11_DMO </flamingo/viewer.html?path=/FLAMINGO/L11p2_m11/L11p2_m11_DMO>`__
     - Fiducial model in a 11.2Gpc box at very low (``m11``) resolution
   * - ``FLAMINGO-10K``
     - `FLAMINGO/L2p8_m8/FLAMINGO-10K </flamingo/viewer.html?path=/FLAMINGO/L2p8_m8/FLAMINGO-10K>`__
     - Fiducial model in a 2.8Gpc box at high (``m8``) resolution

Cosmology variations
--------------------

These simulations are run in 1Gpc boxes at intermediate (``m9``)
resolution with varying cosmological parameters.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Simulation name
     - Path to data
     - Description
   * - ``Planck_DMO``
     - `FLAMINGO/L1_m9/Planck_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m9/Planck_DMO>`__
     - Model with Planck cosmology
   * - ``PlanckNu0p12Var_DMO``
     - `FLAMINGO/L1_m9/PlanckNu0p12Var_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckNu0p12Var_DMO>`__
     - Model with best fitting Planck parameters for neutrino mass :math:`\sum m_\nu c^2 = 0.12 \mathrm{eV}`
   * - ``PlanckNu0p24Var_DMO``
     - `FLAMINGO/L1_m9/PlanckNu0p24Var_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckNu0p24Var_DMO>`__
     - Model with best fitting Planck parameters for neutrino mass :math:`\sum m_\nu c^2 = 0.24 \mathrm{eV}`
   * - ``PlanckNu0p24Fix_DMO``
     - `FLAMINGO/L1_m9/PlanckNu0p24Fix_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckNu0p24Fix_DMO>`__
     - Model with Planck cosmology and increased neutrino mass :math:`\sum m_\nu c^2 = 0.24 \mathrm{eV}`
   * - ``PlanckNu0p48Fix_DMO``
     - `FLAMINGO/L1_m9/PlanckNu0p48Fix_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckNu0p48Fix_DMO>`__
     - Model with Planck cosmology and increased neutrino mass :math:`\sum m_\nu c^2 = 0.48 \mathrm{eV}`
   * - ``LS8_DMO``
     - `FLAMINGO/L1_m9/LS8_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m9/LS8_DMO>`__
     - 'Lensing cosmology' model
   * - ``PlanckDCDM12_DMO``
     - `FLAMINGO/L1_m9/PlanckDCDM12_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckDCDM12_DMO>`__
     - Decaying dark matter hydro model with decay rate :math:`\Gamma h / H_0 = 12` (see `Elbers et al 2025 <https://ui.adsabs.harvard.edu/abs/2025MNRAS.537.2160E/abstract>`__)
   * - ``PlanckDCDM24_DMO``
     - `FLAMINGO/L1_m9/PlanckDCDM24_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckDCDM24_DMO>`__
     - Decaying dark matter hydro model with decay rate :math:`\Gamma h / H_0 = 24` (see `Elbers et al 2025 <https://ui.adsabs.harvard.edu/abs/2025MNRAS.537.2160E/abstract>`__)

Fiducial model with inverted phases
-----------------------------------

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Simulation name
     - Path to data
     - Description
   * - ``L1_m9_ip_DMO``
     - `FLAMINGO/L1_m9/L1_m9_ip_DMO </flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9_ip_DMO>`__
     - Identical to ``L1_m9_DMO`` except that the phases in the initial conditions were inverted
