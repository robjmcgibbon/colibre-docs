Variation runs
==============

The following table provides a list of model variation runs,
which are simulations where specific subgrid parameters
have been modified relative to the fiducial COLIBRE model.
The first column contains the internal of these variations,
and each entry can be clicked to reveal a description of the variation.
The subsequent columns indicate the availability of these runs 
across different box sizes and resolutions.

Several of these runs are still ongoing, please contact Rob
McGibbon if you are interested in using them.
These runs will be presented in an upcoming paper by Chaikin et al.

Supernova feedback variations
-----------------------------

.. list-table:: 
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m7
     - L50m6
   * - .. dropdown:: Thermal_2p0SNenergy

          Double SNII energy
     - ✅
     - ✅
     - ✅
     - ✅
   * - .. dropdown:: Thermal_0p5SNenergy

          Half SNII energy
     - ✅
     - ✅
     - ✅
     - ✅
   * - .. dropdown:: Hybrid_2p0SNenergy

          Double SNII energy
     - ✅
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: Hybrid_0p5SNenergy

          Half SNII energy
     - ✅
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: Thermal_noSN

          No supernova. Early feedback still enabled
     - ❌
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_noEarly

          No early feedback
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_noSNIa

          No SNIa (keeping enrichment)
     - ❌
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_noKineticFixedThermal

          No kinetic feedback (same thermal energy)
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_noKineticFixedTotal

          No kinetic feedback (same total energy)
     - ✅
     - ✅
     - ✅
     - ❌

AGN feedback variations
-----------------------

.. list-table:: 
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m7
     - L50m6
   * - .. dropdown:: Thermal_noAGN

          No AGN
     - ✅
     - ✅
     - ✅
     - ✅
   * - .. dropdown:: Thermal_AGNdTminus0p5dex

          dT_AGN - 0.5 dex
     - ❌
     - ❌
     - ✅
     - ✅
   * - .. dropdown:: Thermal_AGNdTplus0p5dex

          dT_AGN + 0.5 dex
     - ❌
     - ❌
     - ✅
     - ✅
   * - .. dropdown:: Thermal_Mseed0p5dexscatter

          0.5 dex scatter in the BH seed mass
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Hybrid_Mseed0p5dexscatter

          0.5 dex scatter in the BH seed mass
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_epsfplus0p3dex

          AGN feedback efficiency + 0.3 dex
     - ❌
     - ❌
     - ✅
     - ❌
   * - .. dropdown:: Thermal_epsfminus0p3dex

          AGN feedback efficiency - 0.3 dex
     - ❌
     - ❌
     - ✅
     - ❌
   * - .. dropdown:: Hybrid_thermalSeed

          Thermal seed mass (different SN parameters)
     - ❌
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Hybrid_thermalSeed_thermalSN

          Thermal seed mass & supernova
     - ❌
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_Mseedminus0p5dex

          BH seed - 0.5 dex
     - ❌
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_Mseedplus0p5dex

          BH seed + 0.5 dex
     - ❌
     - ✅
     - ✅
     - ❌

Cooling variations
---------------------

.. list-table:: 
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m7
     - L50m6
   * - .. dropdown:: Thermal_eq_with_O

          Non-equil. Chemistry incl. O for H2
     - ❌
     - ❌
     - ✅
     - ✅
   * - .. dropdown:: Thermal_ISRFx10

          ISRF x 10
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_noISRF

          No ISRF
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_CRx0p1

          Cosmic Ray / 10
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_equilibrium

          Equilibrium Chemistry also for H and He
     - ✅
     - ✅
     - ✅
     - ❌


Star formation threshold variations
-----------------------------------

The following runs use different criteria to determine whether a gas particle is star forming.
The star formation rate of particles that satisfy the star formation criterion is still given by the Schmidt law.
For all these runs HII regions cannot form stars.

.. list-table:: 
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m7
     - L50m6
   * - .. dropdown:: Thermal_eagleSF

          Uses the EAGLE metallicity dependent density threshold
          (eqn 2 of the EAGLE overview paper), and
          also requires :math:`T < 10^{4.5} \rm{K}`.
     - ❌
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: Thermal_fixedRhoSF

          SF threshold :math:`n_H > 0.1 \rm{cm}^{-3}` and :math:`T < 10^{4.5} \rm{K}`,
          where :math:`n_H = \rho X_H / m_H`,
          with :math:`X_H` the primordial hydrogen mass fraction.
     - ❌
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: Thermal_noTurbSF

          Uses the same gravitational instability SF threshold criterion as
          the fiducial COLIBRE model (eqn 6 of the overview paper), but with
          :math:`\sigma_{turb}` set to zero.
     - ✅
     - ✅
     - ❌
     - ❌


Additional variations
---------------------

.. list-table:: 
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m7
     - L50m6
   * - .. dropdown:: Thermal_equalNdm

          Equal number of dark matter and gas particles
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_2p0SFE

          Double SF efficiency
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_0p5SFE

          Half SF efficiency
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Thermal_noClumping

          No dust clumping factor
     - ✅
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: Thermal_uncoupledDust

          Dust uncoupled
     - ✅
     - ✅
     - ✅
     - ❌
