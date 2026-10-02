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
     - L50m6
     - L50m7
   * - .. dropdown:: 2p0SNenergy

          .. container:: run-dir

             Directory name: ``Thermal_2p0SNenergy``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_SNenergy/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_SNenergy/z0/>`__

          Double SNII energy
     - ✅
     - ✅
     - ✅
     - ✅
   * - .. dropdown:: 0p5SNenergy

          .. container:: run-dir

             Directory name: ``Thermal_0p5SNenergy``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_SNenergy/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_SNenergy/z0/>`__

          Half SNII energy
     - ✅
     - ✅
     - ✅
     - ✅
   * - .. dropdown:: Hybrid_2p0SNenergy

          .. container:: run-dir

             Directory name: ``Hybrid_2p0SNenergy``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Hybrid_SNenergy/z0/>`__

          Double SNII energy
     - ✅
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: Hybrid_0p5SNenergy

          .. container:: run-dir

             Directory name: ``Hybrid_0p5SNenergy``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Hybrid_SNenergy/z0/>`__

          Half SNII energy
     - ✅
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: NoSN

          .. container:: run-dir

             Directory name: ``Thermal_noSN``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_disableSN/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_disableSN/z0/>`__

          No supernovae. Early feedback still enabled
     - ❌
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: NoEarly

          .. container:: run-dir

             Directory name: ``Thermal_noEarly``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_disableSN/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_disableSN/z0/>`__

          No early feedback
     - ✅
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: NoSNIa

          .. container:: run-dir

             Directory name: ``Thermal_noSNIa``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_disableSN/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_disableSN/z0/>`__

          No SNIa (keeping enrichment)
     - ❌
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: NoKineticFixedThermal

          .. container:: run-dir

             Directory name: ``Thermal_noKineticFixedThermal``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_noKinetic/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_noKinetic/z0/>`__

          No kinetic feedback (same thermal energy)
     - ✅
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: NoKineticFixedTotal

          .. container:: run-dir

             Directory name: ``Thermal_noKineticFixedTotal``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_noKinetic/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_noKinetic/z0/>`__

          No kinetic feedback (same total energy)
     - ✅
     - ✅
     - ❌
     - ✅

AGN feedback variations
-----------------------

.. list-table:: 
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m6
     - L50m7
   * - .. dropdown:: NoAGN

          .. container:: run-dir

             Directory name: ``Thermal_noAGN``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_noAGN/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_noAGN/z0/>`__

          No AGN
     - ✅
     - ✅
     - ✅
     - ✅
   * - .. dropdown:: AGNdTminus0p5dex

          .. container:: run-dir

             Directory name: ``Thermal_AGNdTminus0p5dex``

             Pipeline plots: `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_AGNdT/z0/>`__

          dT_AGN - 0.5 dex
     - ❌
     - ❌
     - ✅
     - ✅
   * - .. dropdown:: AGNdTplus0p5dex

          .. container:: run-dir

             Directory name: ``Thermal_AGNdTplus0p5dex``

             Pipeline plots: `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_AGNdT/z0/>`__

          dT_AGN + 0.5 dex
     - ❌
     - ❌
     - ✅
     - ✅
   * - .. dropdown:: epsfplus0p3dex

          .. container:: run-dir

             Directory name: ``Thermal_epsfplus0p3dex``

             Pipeline plots: `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_epsf/z0/>`__

          AGN feedback efficiency + 0.3 dex
     - ❌
     - ❌
     - ❌
     - ✅
   * - .. dropdown:: epsfminus0p3dex

          .. container:: run-dir

             Directory name: ``Thermal_epsfminus0p3dex``

             Pipeline plots: `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_epsf/z0/>`__

          AGN feedback efficiency - 0.3 dex
     - ❌
     - ❌
     - ❌
     - ✅

The runs in the table below were all carried out in an L100m7 volume. ``Thermal_splitAGN``
uses the fiducial thermal AGN model and was run to :math:`z=0`. The other runs were
restarted from it at different times, with black hole gas accretion disabled from
that point onwards. Without accretion the black holes cannot grow (except through
black hole mergers) and receive no energy to use for AGN feedback.

.. list-table::
   :widths: 40 30 30
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - AGN switched off
     - First snapshot after split
   * - .. dropdown:: splitAGN

          .. container:: run-dir

             Directory name: ``Thermal_splitAGN``

             Pipeline plots: `L100m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L100m7/Thermal_splitAGN/z0/>`__

          Parent run with the fiducial thermal AGN feedback
     - Never
     - N/A
   * - .. dropdown:: splitAGN_z1

          .. container:: run-dir

             Directory name: ``Thermal_splitAGN_z1``

             Pipeline plots: `L100m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L100m7/Thermal_splitAGN/z0/>`__

          Black hole accretion disabled from :math:`z=1`
     - :math:`z=1`
     - ``0093``
   * - .. dropdown:: splitAGN_1e9p5yr

          .. container:: run-dir

             Directory name: ``Thermal_splitAGN_1e9p5yr``

             Pipeline plots: `L100m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L100m7/Thermal_splitAGN/z0/>`__

          Black hole accretion disabled :math:`10^{9.5}` yr before :math:`z=0`
     - :math:`10^{9.5}` yr before :math:`z=0`
     - ``0112``
   * - .. dropdown:: splitAGN_1e9p0yr

          .. container:: run-dir

             Directory name: ``Thermal_splitAGN_1e9p0yr``

             Pipeline plots: `L100m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L100m7/Thermal_splitAGN/z0/>`__

          Black hole accretion disabled :math:`10^{9}` yr before :math:`z=0`
     - :math:`10^{9}` yr before :math:`z=0`
     - ``0121``
   * - .. dropdown:: splitAGN_1e8p5yr

          .. container:: run-dir

             Directory name: ``Thermal_splitAGN_1e8p5yr``

             Pipeline plots: `L100m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L100m7/Thermal_splitAGN/z0/>`__

          Black hole accretion disabled :math:`10^{8.5}` yr before :math:`z=0`
     - :math:`10^{8.5}` yr before :math:`z=0`
     - ``0125``
   * - .. dropdown:: splitAGN_1e8p0yr

          .. container:: run-dir

             Directory name: ``Thermal_splitAGN_1e8p0yr``

             Pipeline plots: `L100m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L100m7/Thermal_splitAGN/z0/>`__

          Black hole accretion disabled :math:`10^{8}` yr before :math:`z=0`
     - :math:`10^{8}` yr before :math:`z=0`
     - ``0127``

.. note::

   There is also ``L0100N0752/Thermal_noAGN``, which is a separate L100m7 run
   with no black holes at all. Unlike the runs in the table above, it does not
   share its early evolution with ``Thermal_splitAGN``.
   `Pipeline plots <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L100m7/Thermal_noAGN/z0/>`__

Black hole seed variations
---------------------------

.. list-table::
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m6
     - L50m7
   * - .. dropdown:: Mseed0p5dexscatter

          .. container:: run-dir

             Directory name: ``Thermal_Mseed0p5dexscatter``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_Mseed/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_Mseed/z0/>`__

          0.5 dex scatter in the BH seed mass
     - ✅
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: Hybrid_Mseed0p5dexscatter

          .. container:: run-dir

             Directory name: ``Hybrid_Mseed0p5dexscatter``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Hybrid_Mseed/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Hybrid_Mseed/z0/>`__

          0.5 dex scatter in the BH seed mass
     - ✅
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: Hybrid_thermalSeed

          .. container:: run-dir

             Directory name: ``Hybrid_thermalSeed``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Hybrid_Mseed/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Hybrid_Mseed/z0/>`__

          Thermal seed mass (different SN parameters)
     - ❌
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: Hybrid_thermalSeed_thermalSN

          .. container:: run-dir

             Directory name: ``Hybrid_thermalSeed_thermalSN``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Hybrid_Mseed/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Hybrid_Mseed/z0/>`__

          Thermal seed mass & supernova
     - ❌
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: Mseedminus0p5dex

          .. container:: run-dir

             Directory name: ``Thermal_Mseedminus0p5dex``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_Mseed/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_Mseed/z0/>`__

          BH seed - 0.5 dex
     - ❌
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: Mseedplus0p5dex

          .. container:: run-dir

             Directory name: ``Thermal_Mseedplus0p5dex``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_Mseed/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_Mseed/z0/>`__

          BH seed + 0.5 dex
     - ❌
     - ✅
     - ❌
     - ✅

Cooling variations
---------------------

.. list-table:: 
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m6
     - L50m7
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

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_cooling/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_cooling/z0/>`__

          Interstellar radiation field boosted by factor of 10
     - ✅
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: NoISRF

          .. container:: run-dir

             Directory name: ``Thermal_noISRF``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_cooling/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_cooling/z0/>`__

          No interstellar radiation field
     - ✅
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: CRx0p1

          .. container:: run-dir

             Directory name: ``Thermal_CRx0p1``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_cooling/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_cooling/z0/>`__

          Cosmic Ray / 10
     - ✅
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: Nshx0p5

          .. container:: run-dir

             Directory name: ``Thermal_Nshx0p5``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_selfShielding/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_selfShielding/z0/>`__

          Shielding length halved
     - ✅
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: Nshx2p0

          .. container:: run-dir

             Directory name: ``Thermal_Nshx2p0``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_selfShielding/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_selfShielding/z0/>`__

          Shielding length doubled
     - ✅
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: Chemical equilibrium

          .. container:: run-dir

             Directory name: ``Thermal_equilibrium``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_equilibrium/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_equilibrium/z0/>`__

          Equilibrium Chemistry also for H and He
     - ✅
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: Full non-equilibrium chemistry

          .. container:: run-dir

             Directory name: ``Thermal_NEQ``

          Non-equilibrium chemistry for all species in the CHIMES network
     - ✅
     - ✅
     - ❌
     - ✅

.. note::

   An L25m7 run with full non-equilibrium chemistry is also available

Star formation variations
-------------------------

.. list-table::
   :widths: 40 15 15 15 15
   :width: 100%
   :header-rows: 1

   * - Simulation Name
     - L12m5
     - L25m6
     - L50m6
     - L50m7
   * - .. dropdown:: 2p0SFE

          .. container:: run-dir

             Directory name: ``Thermal_2p0SFE``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_SFE/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_SFE/z0/>`__

          Double SF efficiency
     - ✅
     - ✅
     - ❌
     - ✅
   * - .. dropdown:: 0p5SFE

          .. container:: run-dir

             Directory name: ``Thermal_0p5SFE``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_SFE/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_SFE/z0/>`__

          Half SF efficiency
     - ✅
     - ✅
     - ❌
     - ✅

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
     - L50m6
     - L50m7
   * - .. dropdown:: EagleSF

          .. container:: run-dir

             Directory name: ``Thermal_eagleSF``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_SFthreshold/z0/>`__

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

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_SFthreshold/z0/>`__

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

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_SFthreshold/z0/>`__

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
     - L50m6
     - L50m7
   * - .. dropdown:: NoClumping

          .. container:: run-dir

             Directory name: ``Thermal_noClumping``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_Dust/z0/>`__

          No dust clumping factor
     - ✅
     - ✅
     - ❌
     - ❌
   * - .. dropdown:: UncoupledDust

          .. container:: run-dir

             Directory name: ``Thermal_uncoupledDust``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_Dust/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_Dust/z0/>`__

          Dust uncoupled
     - ✅
     - ✅
     - ❌
     - ✅

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
     - L50m6
     - L50m7
   * - .. dropdown:: EqualNdm

          .. container:: run-dir

             Directory name: ``Thermal_equalNdm``

             Pipeline plots: `L25m6 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L025m6/Thermal_equalNdm/z0/>`__ · `L50m7 <https://home.strw.leidenuniv.nl/~mcgibbon/COLIBRE/documentation/pipeline/variation_runs/L050m7/Thermal_equalNdm/z0/>`__

          Equal number of dark matter and gas particles
     - ✅
     - ✅
     - ❌
     - ✅
