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
   * - .. dropdown:: Thermal_eq

          Equilibrium Chemistry also for H and He
     - ✅
     - ✅
     - ✅
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
   * - .. dropdown:: Thermal_equal_Ndm

          Different number of DM particles
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
   * - .. dropdown:: Thermal_clumping1

          No dust clumping factor
     - ✅
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: Thermal_dust_uncoupled

          Dust uncoupled
     - ✅
     - ✅
     - ✅
     - ❌
