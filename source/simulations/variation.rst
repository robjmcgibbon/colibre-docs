Variation runs
==============

The following table provides a list of model variation runs,
which are simulations where specific subgrid parameters
have been modified relative to the fiducial COLIBRE model.
The first column contains the name of these variations,
and each entry can be clicked to reveal a description of the variation
along with the name of the directory containing the run.
The subsequent columns indicate the availability of these runs 
across different box sizes and resolutions.

On COSMA the variation runs for each box size and resolution are located in a
``VariationRuns`` directory within the corresponding run directory, e.g. the
L25m6 variations are at ``/cosma8/data/dp004/colibre/Runs/L0025N0376/VariationRuns``.

Several of these runs are still ongoing, so if you cannot find one in the
directory above, please contact Rob McGibbon.
These runs will be presented in an upcoming paper by Chaikin et al.

.. contents::
   :local:
   :backlinks: none

Stellar feedback variations
----------------------------

.. list-table:: 
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m7
     - L50m6
   * - .. dropdown:: 2p0SNenergy

          .. container:: run-dir

             Directory name: ``Thermal_2p0SNenergy``

          Double SNII energy
     - ✅
     - ✅
     - ✅
     - ✅
   * - .. dropdown:: 0p5SNenergy

          .. container:: run-dir

             Directory name: ``Thermal_0p5SNenergy``

          Half SNII energy
     - ✅
     - ✅
     - ✅
     - ✅
   * - .. dropdown:: Hybrid_2p0SNenergy

          .. container:: run-dir

             Directory name: ``Hybrid_2p0SNenergy``

          Double SNII energy
     - ✅
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: Hybrid_0p5SNenergy

          .. container:: run-dir

             Directory name: ``Hybrid_0p5SNenergy``

          Half SNII energy
     - ✅
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: NoSN

          .. container:: run-dir

             Directory name: ``Thermal_noSN``

          No supernova. Early feedback still enabled
     - ❌
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: NoEarly

          .. container:: run-dir

             Directory name: ``Thermal_noEarly``

          No early feedback
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: NoSNIa

          .. container:: run-dir

             Directory name: ``Thermal_noSNIa``

          No SNIa (keeping enrichment)
     - ❌
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: NoKineticFixedThermal

          .. container:: run-dir

             Directory name: ``Thermal_noKineticFixedThermal``

          No kinetic feedback (same thermal energy)
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: NoKineticFixedTotal

          .. container:: run-dir

             Directory name: ``Thermal_noKineticFixedTotal``

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
   * - .. dropdown:: NoAGN

          .. container:: run-dir

             Directory name: ``Thermal_noAGN``

          No AGN
     - ✅
     - ✅
     - ✅
     - ✅
   * - .. dropdown:: AGNdTminus0p5dex

          .. container:: run-dir

             Directory name: ``Thermal_AGNdTminus0p5dex``

          dT_AGN - 0.5 dex
     - ❌
     - ❌
     - ✅
     - ✅
   * - .. dropdown:: AGNdTplus0p5dex

          .. container:: run-dir

             Directory name: ``Thermal_AGNdTplus0p5dex``

          dT_AGN + 0.5 dex
     - ❌
     - ❌
     - ✅
     - ✅
   * - .. dropdown:: epsfplus0p3dex

          .. container:: run-dir

             Directory name: ``Thermal_epsfplus0p3dex``

          AGN feedback efficiency + 0.3 dex
     - ❌
     - ❌
     - ✅
     - ❌
   * - .. dropdown:: epsfminus0p3dex

          .. container:: run-dir

             Directory name: ``Thermal_epsfminus0p3dex``

          AGN feedback efficiency - 0.3 dex
     - ❌
     - ❌
     - ✅
     - ❌

Black hole seed variations
---------------------------

.. list-table::
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m7
     - L50m6
   * - .. dropdown:: Mseed0p5dexscatter

          .. container:: run-dir

             Directory name: ``Thermal_Mseed0p5dexscatter``

          0.5 dex scatter in the BH seed mass
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Hybrid_Mseed0p5dexscatter

          .. container:: run-dir

             Directory name: ``Hybrid_Mseed0p5dexscatter``

          0.5 dex scatter in the BH seed mass
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Hybrid_thermalSeed

          .. container:: run-dir

             Directory name: ``Hybrid_thermalSeed``

          Thermal seed mass (different SN parameters)
     - ❌
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Hybrid_thermalSeed_thermalSN

          .. container:: run-dir

             Directory name: ``Hybrid_thermalSeed_thermalSN``

          Thermal seed mass & supernova
     - ❌
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Mseedminus0p5dex

          .. container:: run-dir

             Directory name: ``Thermal_Mseedminus0p5dex``

          BH seed - 0.5 dex
     - ❌
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Mseedplus0p5dex

          .. container:: run-dir

             Directory name: ``Thermal_Mseedplus0p5dex``

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
   * - .. dropdown:: Non-equilibrium Oxygen

          .. container:: run-dir

             Directory name: ``Thermal_eq_with_O``

          Non-equil. Chemistry incl. O for H2
     - ❌
     - ❌
     - ✅
     - ✅
   * - .. dropdown:: ISRFx10

          .. container:: run-dir

             Directory name: ``Thermal_ISRFx10``

          Interstellar radiation field boosted by factor of 10
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: NoISRF

          .. container:: run-dir

             Directory name: ``Thermal_noISRF``

          No interstellar radiation field
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: CRx0p1

          .. container:: run-dir

             Directory name: ``Thermal_CRx0p1``

          Cosmic Ray / 10
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: Chemical equilibrium

          .. container:: run-dir

             Directory name: ``Thermal_equilibrium``

          Equilibrium Chemistry also for H and He
     - ✅
     - ✅
     - ✅
     - ❌


Star formation variations
-------------------------

.. list-table::
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m7
     - L50m6
   * - .. dropdown:: 2p0SFE

          .. container:: run-dir

             Directory name: ``Thermal_2p0SFE``

          Double SF efficiency
     - ✅
     - ✅
     - ✅
     - ❌
   * - .. dropdown:: 0p5SFE

          .. container:: run-dir

             Directory name: ``Thermal_0p5SFE``

          Half SF efficiency
     - ✅
     - ✅
     - ✅
     - ❌

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
   * - .. dropdown:: EagleSF

          .. container:: run-dir

             Directory name: ``Thermal_eagleSF``

          Uses the EAGLE metallicity dependent density threshold
          (eqn 2 of the EAGLE overview paper), and
          also requires :math:`T < 10^{4.5} \rm{K}`.

     - ❌
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: FixedRhoSF

          .. container:: run-dir

             Directory name: ``Thermal_fixedRhoSF``

          SF threshold :math:`n_H > 0.1 \rm{cm}^{-3}` and :math:`T < 10^{4.5} \rm{K}`,
          where :math:`n_H = \rho X_H / m_H`,
          with :math:`X_H` the primordial hydrogen mass fraction.
     - ❌
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: NoTurbSF

          .. container:: run-dir

             Directory name: ``Thermal_noTurbSF``

          Uses the same gravitational instability SF threshold criterion as
          the fiducial COLIBRE model (eqn 6 of the overview paper), but with
          :math:`\sigma_{turb}` set to zero.
     - ✅
     - ✅
     - ❌
     - ❌

Dust variations
----------------

.. list-table::
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m7
     - L50m6
   * - .. dropdown:: NoClumping

          .. container:: run-dir

             Directory name: ``Thermal_noClumping``

          No dust clumping factor
     - ✅
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: UncoupledDust

          .. container:: run-dir

             Directory name: ``Thermal_uncoupledDust``

          Dust uncoupled
     - ✅
     - ✅
     - ✅
     - ❌

.. note::

   ``L0100N0752/Thermal_noGrainGrowth`` is a dust variation run with grain growth
   disabled. It has been run to :math:`z=9`. Contact Evgenii Chaikin.


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
   * - .. dropdown:: EqualNdm

          .. container:: run-dir

             Directory name: ``Thermal_equalNdm``

          Equal number of dark matter and gas particles
     - ✅
     - ✅
     - ✅
     - ❌
