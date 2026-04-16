Hydrodynamical simulations
==========================

The tables below list all of the hydrodynamical simulations which are
part of the FLAMINGO data release and provide a link to the simulation
data.

For exact model parameters see the `table of FLAMINGO simulations
<https://flamingo.strw.leidenuniv.nl/simulations.html>`__.


Fiducial models
---------------

These simulations use the fiducial cosmology and galaxy formation
model. They consist of a 1Gpc box run at three different resolutions
and larger, 2.8Gpc box at intermediate resolution.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Simulation name
     - Path to data
     - Description
   * - ``L1_m8``
     - `FLAMINGO/L1_m8/L1_m8 </flamingo/viewer.html?path=/FLAMINGO/L1_m8/L1_m8>`__
     - Fiducial model in a 1Gpc box at high (``m8``) resolution
   * - ``L1_m9``
     - `FLAMINGO/L1_m9/L1_m9 </flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9>`__
     - Fiducial model in a 1Gpc box at intermediate (``m9``) resolution
   * - ``L1_m10``
     - `FLAMINGO/L1_m10/L1_m10 </flamingo/viewer.html?path=/FLAMINGO/L1_m10/L1_m10>`__
     - Fiducial model in a 1Gpc box at low (``m10``) resolution
   * - ``L2p8_m9``
     - `FLAMINGO/L2p8_m9/L2p8_m9 </flamingo/viewer.html?path=/FLAMINGO/L2p8_m9/L2p8_m9>`__
     - Fiducial model in a 2.8Gpc box at intermediate (``m9``) resolution

Model variations
----------------

These simulations are run in 1Gpc box at ``m9`` resolution, varying
the cosmological and galaxy formation model parameters.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Simulation name
     - Path to data
     - Description
   * - ``fgas+2σ``
     - `FLAMINGO/L1_m9/fgas+2sigma </flamingo/viewer.html?path=/FLAMINGO/L1_m9/fgas%2B2sigma>`__
     - Calibrated to cluster gas fractions 2σ above observed
   * - ``fgas-2σ``
     - `FLAMINGO/L1_m9/fgas-2sigma </flamingo/viewer.html?path=/FLAMINGO/L1_m9/fgas-2sigma>`__
     - Calibrated to cluster gas fractions 2σ below observed
   * - ``fgas-4σ``
     - `FLAMINGO/L1_m9/fgas-4sigma </flamingo/viewer.html?path=/FLAMINGO/L1_m9/fgas-4sigma>`__
     - Calibrated to cluster gas fractions 4σ below observed
   * - ``fgas-8σ``
     - `FLAMINGO/L1_m9/fgas-8sigma </flamingo/viewer.html?path=/FLAMINGO/L1_m9/fgas-8sigma>`__
     - Calibrated to cluster gas fractions 8σ below observed
   * - ``M*-1σ``
     - `FLAMINGO/L1_m9/Mstar-1sigma </flamingo/viewer.html?path=/FLAMINGO/L1_m9/Mstar-1sigma>`__
     - Calibrated to stellar masses 1σ below observed
   * - ``M*-1σ_fgas-4σ``
     - `FLAMINGO/L1_m9/Mstar-1sigma_fgas-4sigma </flamingo/viewer.html?path=/FLAMINGO/L1_m9/Mstar-1sigma_fgas-4sigma>`__
     - Calibrated to cluster gas fractions 4σ below and stellar masses 1σ below observed
   * - ``Jet``
     - `FLAMINGO/L1_m9/Jet </flamingo/viewer.html?path=/FLAMINGO/L1_m9/Jet>`__
     - Model with jet AGN feedback implementation
   * - ``Jet_fgas-4σ``
     - `FLAMINGO/L1_m9/Jet_fgas-4sigma </flamingo/viewer.html?path=/FLAMINGO/L1_m9/Jet_fgas-4sigma>`__
     - Model with jet AGN feedback implementation, calibrated to cluster gas fractions 4σ below observed
   * - ``Planck``
     - `FLAMINGO/L1_m9/Planck </flamingo/viewer.html?path=/FLAMINGO/L1_m9/Planck>`__
     - Model with Planck cosmology
   * - ``PlanckNu0p24Var``
     - `FLAMINGO/L1_m9/PlanckNu0p24Var </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckNu0p24Var>`__
     - Model with best fitting Planck parameters for neutrino mass :math:`\sum m_\nu c^2 = 0.24 \mathrm{eV}`
   * - ``PlanckNu0p24Fix``
     - `FLAMINGO/L1_m9/PlanckNu0p24Fix </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckNu0p24Fix>`__
     - Model with Planck cosmology and increased neutrino mass :math:`\sum m_\nu c^2 = 0.24 \mathrm{eV}`
   * - ``PlanckNu0p48Fix``
     - `FLAMINGO/L1_m9/PlanckNu0p48Fix </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckNu0p48Fix>`__
     - Model with Planck cosmology and increased neutrino mass :math:`\sum m_\nu c^2 = 0.48 \mathrm{eV}`
   * - ``LS8``
     - `FLAMINGO/L1_m9/LS8 </flamingo/viewer.html?path=/FLAMINGO/L1_m9/LS8>`__
     - 'Lensing cosmology' model
   * - ``PlanckDCDM12``
     - `FLAMINGO/L1_m9/PlanckDCDM12 </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckDCDM12>`__
     - Decaying dark matter hydro model with decay rate :math:`\Gamma h / H_0 = 12` (see `Elbers et al 2025 <https://ui.adsabs.harvard.edu/abs/2025MNRAS.537.2160E/abstract>`__)
   * - ``PlanckDCDM24``
     - `FLAMINGO/L1_m9/PlanckDCDM24 </flamingo/viewer.html?path=/FLAMINGO/L1_m9/PlanckDCDM24>`__
     - Decaying dark matter hydro model with decay rate :math:`\Gamma h / H_0 = 24` (see `Elbers et al 2025 <https://ui.adsabs.harvard.edu/abs/2025MNRAS.537.2160E/abstract>`__)
   * - ``LS8_fgas-8σ``
     - `FLAMINGO/L1_m9/LS8_fgas-8sigma </flamingo/viewer.html?path=/FLAMINGO/L1_m9/LS8_fgas-8sigma>`__
     - 'Lensing cosmology' model calibrated to cluster gas fractions 8σ below observed
   * - ``NoCooling``
     - `FLAMINGO/L1_m9/NoCooling </flamingo/viewer.html?path=/FLAMINGO/L1_m9/NoCooling>`__
     - Model with no cooling, star formation or feedback
   * - ``L1_m9_extraDM``
     - `FLAMINGO/L1_m9/L1_m9_extraDM </flamingo/viewer.html?path=/FLAMINGO/L1_m9/L1_m9_extraDM>`__
     - Model with increased dark matter resolution
