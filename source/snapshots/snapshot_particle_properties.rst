.. _snapshot_particle_properties:

Particle properties
===================

This page documents all of the properties which are stored for each
type of particle in a COLIBRE snapshot. The first column in each table gives the
name of the property when opened using the swiftsimio library.
Clicking on each property name will open a dropdown box,
which contains information about the dataset within the HDF5 file.
The second column gives a description of the property. Certain
properties also contain a link to a footnote at the bottom of this page
The final column indicates whether the property is present in both
snapshots and snipshots.

.. note:: Units are provided here for information, but it's usually
          better to use the metadata in the files for any unit
          conversions. The `swiftsimio
          <https://swiftsimio.readthedocs.io/en/latest/loading_data/index.html>`__
          python module handles units automatically in snapshots and
          SOAP halo catalogues.

The runs with hybrid AGN feedback and globular clusters contain
additional properties not present the the standard thermal AGN runs.
These properties are listed in a separate tables.

Dark matter particles
---------------------

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Snipshot
   * - .. dropdown:: ``coordinates``

          * **HDF5 name:** ``Coordinates``
          * **Shape:** 3
          * **Datatype:** float64
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** 1 pc accurate
     - Co-moving position of the particles
     - ✅
   * - .. dropdown:: ``fofgroup_ids``

          * **HDF5 name:** ``FOFGroupIDs``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - Friends-Of-Friends ID of the group the particles belong to
     - ✅
   * - .. dropdown:: ``halo_catalogue_index``

          * **HDF5 name:** ``HaloCatalogueIndex``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - Index of halo in which this particle is a bound member, or -1 if none
     - ❌
   * - .. dropdown:: ``masses``

          * **HDF5 name:** ``Masses``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** no compression
     - Masses of the particles
     - ✅
   * - .. dropdown:: ``particle_ids``

          * **HDF5 name:** ``ParticleIDs``
          * **Shape:** 1
          * **Datatype:** uint64
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - Unique ID of the particles
     - ✅
   * - .. dropdown:: ``potentials``

          * **HDF5 name:** ``Potentials``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a^{-1.0} \cdot \rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Gravitational potentials of the particles
     - ✅
   * - .. dropdown:: ``rank_bound``

          * **HDF5 name:** ``Rank_bound``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - Ranking by binding energy of the bound particles (first in halo=0), or -1 if not bound
     - ❌
   * - .. dropdown:: ``specific_potential_energies``

          * **HDF5 name:** ``SpecificPotentialEnergies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** no compression
     - Specific potential energy of the bound particles
     - ❌
   * - .. dropdown:: ``velocities``

          * **HDF5 name:** ``Velocities``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** 0.1 km/s accurate
     - Peculiar velocities of the particles. This is :math:`a \frac{dx}{dt}` where :math:`x` is the co-moving position of the particles.
     - ✅


Gas particles
-------------

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Snipshot
   * - .. dropdown:: ``averaged_star_formation_rates``

          * **HDF5 name:** ``AveragedStarFormationRates``
          * **Shape:** 2
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Star formation rates of the particles averaged over the period set by the first two snapshot triggers. See :ref:`footnote_averaged`
     - ❌
   * - .. dropdown:: ``compton_yparameters``

          * **HDF5 name:** ``ComptonYParameters``
          * **Shape:** 1
          * **Datatype:** float64
          * **Units:** :math:`\rm{Mpc}^{2}`
          * **Compression:** :math:`1.3669345{\rm{}e}10 \rightarrow{} 1.36693{\rm{}e}10`
     - Compton y parameters in the physical frame computed based on the cooling tables. This is 0 for star-forming particles.
     - ❌
   * - .. dropdown:: ``coordinates``

          * **HDF5 name:** ``Coordinates``
          * **Shape:** 3
          * **Datatype:** float64
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** 1 pc accurate
     - Co-moving positions of the particles
     - ✅
   * - .. dropdown:: ``densities``

          * **HDF5 name:** ``Densities``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a^{-3.0} \cdot 10^{10}\ \frac{\rm{M}_\odot}{\rm{Mpc}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Co-moving mass densities of the particles
     - ✅
   * - .. dropdown:: ``densities_at_last_agnevent``

          * **HDF5 name:** ``DensitiesAtLastAGNEvent``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot}{\rm{Mpc}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical density (not subgrid) of the gas at the last AGN feedback event that hit the particles. -1 if the particles have never been heated.
     - ❌
   * - .. dropdown:: ``densities_at_last_supernova_event``

          * **HDF5 name:** ``DensitiesAtLastSupernovaEvent``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot}{\rm{Mpc}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical density (not subgrid) of the gas at the last SN (type-II or type-Ia) thermal feedback event that hit the particles. -1 if the particles have never been heated.
     - ❌
   * - .. dropdown:: ``diffusion_parameters``

          * **HDF5 name:** ``DiffusionParameters``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Diffusion coefficient (alpha_diff) of the particles
     - ❌
   * - .. dropdown:: ``dust_mass_fractions``

          * **HDF5 name:** ``DustMassFractions``
          * **Shape:** 6
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in a given species of dust grain. See :ref:`dust-names`.
     - ❌
   * - .. dropdown:: ``element_mass_fractions``

          * **HDF5 name:** ``ElementMassFractions``
          * **Shape:** 12
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in the given element. ``ReducedElementMassFractions`` is available for snipshots. See :ref:`element-names`.
     - ❌
   * - .. dropdown:: ``element_mass_fractions_diffuse``

          * **HDF5 name:** ``ElementMassFractionsDiffuse``
          * **Shape:** 12
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in the given element and in the diffuse (non-dust) phase. See :ref:`element-names`.
     - ❌
   * - .. dropdown:: ``energies_received_from_agnfeedback``

          * **HDF5 name:** ``EnergiesReceivedFromAGNFeedback``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Total amount of thermal energy from AGN feedback events received by the particles.
     - ❌
   * - .. dropdown:: ``entropies``

          * **HDF5 name:** ``Entropies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{-7}\ \frac{10^{10416679084301/31250000000000} \cdot \rm{Mpc}^{2} \cdot \rm{km}^{2}}{\rm{M}_\odot^{208333320915699/312500000000000} \cdot \rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Co-moving entropies per unit mass of the particles
     - ❌
   * - .. dropdown:: ``fofgroup_ids``

          * **HDF5 name:** ``FOFGroupIDs``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - Friends-Of-Friends ID of the group the particles belong to
     - ✅
   * - .. dropdown:: ``hiiregions_end_time``

          * **HDF5 name:** ``HIIregionsEndTime``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{Mpc} \cdot \rm{s} / \rm{km}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Time until particle is in HII region. See :ref:`hii_end_time`
     - ❌
   * - .. dropdown:: ``halo_catalogue_index``

          * **HDF5 name:** ``HaloCatalogueIndex``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - Index of halo in which this particle is a bound member, or -1 if none
     - ❌
   * - .. dropdown:: ``internal_energies``

          * **HDF5 name:** ``InternalEnergies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a^{-2.0} \cdot \rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Co-moving thermal energies per unit mass of the particles
     - ✅
   * - .. dropdown:: ``iron_mass_fractions_from_snia``

          * **HDF5 name:** ``IronMassFractionsFromSNIa``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in iron produced by SNIa stars (incorporating both depleted and nebular phases)Fractions of the particles' masses that are in metals (incorporating both depleted and nebular phases)
     - ❌
   * - .. dropdown:: ``iron_mass_fractions_from_snia_diffuse``

          * **HDF5 name:** ``IronMassFractionsFromSNIaDiffuse``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in iron originating from SNIa, but not depleted into dust
     - ❌
   * - .. dropdown:: ``laplacian_internal_energies``

          * **HDF5 name:** ``LaplacianInternalEnergies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a^{-4.0} \cdot \frac{\rm{km}^{2}}{\rm{Mpc}^{2} \cdot \rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Laplacian (del squared) of the Internal Energy per unit mass of the particles
     - ❌
   * - .. dropdown:: ``last_agnfeedback_scale_factors``

          * **HDF5 name:** ``LastAGNFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by AGN feedback. -1 if a particle has never been hit by feedback
     - ✅
   * - .. dropdown:: ``last_energies_received_from_agnfeedback``

          * **HDF5 name:** ``LastEnergiesReceivedFromAGNFeedback``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The energy the particles received the last time they were heated by AGN feedback.
     - ❌
   * - .. dropdown:: ``last_fofhalo_masses``

          * **HDF5 name:** ``LastFOFHaloMasses``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the last FOF haloes the particles where part of. -1 if the particle has never been in a FOF group
     - ❌
   * - .. dropdown:: ``last_fofhalo_masses_scale_factors``

          * **HDF5 name:** ``LastFOFHaloMassesScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particle was last in a FOF group
     - ❌
   * - .. dropdown:: ``last_ismscale_factors``

          * **HDF5 name:** ``LastISMScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factor at which the particle was part of the ISM for the last time, i.e. its density was larger than 100 times the mean density and (its neutral fraction larger than 50% OR be an HII region). -1 if the particle was never part of the ISM.
     - ✅
   * - .. dropdown:: ``last_kinetic_early_feedback_scale_factors``

          * **HDF5 name:** ``LastKineticEarlyFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by kinetic early feedback. -1 if a particle has never been hit by feedback
     - ❌
   * - .. dropdown:: ``last_sniikinetic_feedback_scale_factors``

          * **HDF5 name:** ``LastSNIIKineticFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by SNII kinetic feedback. -1 if a particle has never been hit by feedback
     - ❌
   * - .. dropdown:: ``last_sniikinetic_feedbackvkick``

          * **HDF5 name:** ``LastSNIIKineticFeedbackvkick``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical kick velocity the particles were kicked with at last SNII kinetic feedback event. -1 if a particle has never been hit by feedback
     - ❌
   * - .. dropdown:: ``last_sniithermal_feedback_scale_factors``

          * **HDF5 name:** ``LastSNIIThermalFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by SNII thermal feedback. -1 if a particle has never been hit by feedback
     - ✅
   * - .. dropdown:: ``last_snia_thermal_feedback_scale_factors``

          * **HDF5 name:** ``LastSNIaThermalFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by SNIa thermal feedback. -1 if a particle has never been hit by feedback
     - ❌
   * - .. dropdown:: ``last_star_formation_scale_factors``

          * **HDF5 name:** ``LastStarFormationScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the stars last had a non-zero star formation rate.
     - ❌
   * - .. dropdown:: ``mass_fractions_from_agb``

          * **HDF5 name:** ``MassFractionsFromAGB``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by AGN stars
     - ❌
   * - .. dropdown:: ``mass_fractions_from_cejsn``

          * **HDF5 name:** ``MassFractionsFromCEJSN``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by common-envelop jets SN events
     - ❌
   * - .. dropdown:: ``mass_fractions_from_collapsar``

          * **HDF5 name:** ``MassFractionsFromCollapsar``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by collapsar events
     - ❌
   * - .. dropdown:: ``mass_fractions_from_nsm``

          * **HDF5 name:** ``MassFractionsFromNSM``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by neutron star merger events
     - ❌
   * - .. dropdown:: ``mass_fractions_from_snii``

          * **HDF5 name:** ``MassFractionsFromSNII``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by SNII stars
     - ❌
   * - .. dropdown:: ``mass_fractions_from_snia``

          * **HDF5 name:** ``MassFractionsFromSNIa``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by SNIa stars
     - ❌
   * - .. dropdown:: ``masses``

          * **HDF5 name:** ``Masses``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** no compression
     - Masses of the particles
     - ✅
   * - .. dropdown:: ``maximal_sniikinetic_feedbackvkick``

          * **HDF5 name:** ``MaximalSNIIKineticFeedbackvkick``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Maximal physical kick velocity the particles were kicked with in SNII kinetic feedback. -1 if a particle has never been hit by feedback
     - ❌
   * - .. dropdown:: ``maximal_temperature_scale_factors``

          * **HDF5 name:** ``MaximalTemperatureScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the maximal temperature was reached
     - ❌
   * - .. dropdown:: ``maximal_temperatures``

          * **HDF5 name:** ``MaximalTemperatures``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Maximal temperatures ever reached by the particles
     - ❌
   * - .. dropdown:: ``mean_iron_weighted_redshifts``

          * **HDF5 name:** ``MeanIronWeightedRedshifts``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Mean redshift of SNIa events weighted by the iron mass imparted by each event. -1 if a particle has never been enriched by SNIa.
     - ❌
   * - .. dropdown:: ``mean_metal_weighted_redshifts``

          * **HDF5 name:** ``MeanMetalWeightedRedshifts``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Mean redshift of enrichment events weighted by the metal mass imparted by each event. -1 if a particle has never been enriched.
     - ❌
   * - .. dropdown:: ``metal_mass_fractions``

          * **HDF5 name:** ``MetalMassFractions``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in metals (incorporating both depleted and nebular phases)
     - ✅
   * - .. dropdown:: ``metal_mass_fractions_from_agb``

          * **HDF5 name:** ``MetalMassFractionsFromAGB``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in metals produced by AGB stars (incorporating both depleted and nebular phases)
     - ❌
   * - .. dropdown:: ``metal_mass_fractions_from_snii``

          * **HDF5 name:** ``MetalMassFractionsFromSNII``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in metals produced by SNII stars (incorporating both depleted and nebular phases)
     - ❌
   * - .. dropdown:: ``metal_mass_fractions_from_snia``

          * **HDF5 name:** ``MetalMassFractionsFromSNIa``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in metals produced by SNIa stars (incorporating both depleted and nebular phases)
     - ❌
   * - .. dropdown:: ``minimal_smoothing_length_scale_factors``

          * **HDF5 name:** ``MinimalSmoothingLengthScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the minimal smoothing length was reached
     - ❌
   * - .. dropdown:: ``minimal_smoothing_lengths``

          * **HDF5 name:** ``MinimalSmoothingLengths``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Minimal smoothing lengths ever reached by the particles
     - ❌
   * - .. dropdown:: ``particle_ids``

          * **HDF5 name:** ``ParticleIDs``
          * **Shape:** 1
          * **Datatype:** uint64
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - Unique IDs of the particles
     - ✅
   * - .. dropdown:: ``potentials``

          * **HDF5 name:** ``Potentials``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a^{-1.0} \cdot \rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Co-moving gravitational potential at position of the particles
     - ❌
   * - .. dropdown:: ``pressures``

          * **HDF5 name:** ``Pressures``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a^{-5.0} \cdot 10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{Mpc}^{3} \cdot \rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Co-moving pressures of the particles
     - ✅
   * - .. dropdown:: ``progenitor_particle_ids``

          * **HDF5 name:** ``ProgenitorParticleIDs``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - ID of the progenitor of this particle. If this particle is the result of one (or many) splitting events, this ID corresponds to the ID of the particle in the initial conditions that its lineage can be traced back to. If the particle was never split, this is the same as ParticleIDs.
     - ✅
   * - .. dropdown:: ``rank_bound``

          * **HDF5 name:** ``Rank_bound``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - Ranking by binding energy of the bound particles (first in halo=0), or -1 if not bound
     - ❌
   * - .. dropdown:: ``smoothing_lengths``

          * **HDF5 name:** ``SmoothingLengths``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Co-moving smoothing lengths (FWHM of the kernel) of the particles
     - ✅
   * - .. dropdown:: ``species_fractions``

          * **HDF5 name:** ``SpeciesFractions``
          * **Shape:** 10
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Species fractions array for all ions and molecules in the CHIMES network. The fraction of species i is defined in terms of its number density relative to hydrogen, i.e. :math:`n_i` / :math:`n_{H_{tot}}`. ``ReducedSpeciesFractions`` is available for snipshots. See :ref:`species-names`.
     - ❌
   * - .. dropdown:: ``specific_potential_energies``

          * **HDF5 name:** ``SpecificPotentialEnergies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** no compression
     - Specific potential energy of the bound particles
     - ❌
   * - .. dropdown:: ``split_counts``

          * **HDF5 name:** ``SplitCounts``
          * **Shape:** 1
          * **Datatype:** uint8
          * **Units:** dimensionless
          * **Compression:** no compression
     - Number of times this particle has been split. Note that both particles that take part in the splitting have their counter incremented.
     - ✅
   * - .. dropdown:: ``split_trees``

          * **HDF5 name:** ``SplitTrees``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - Binary tree describing splitting events. Particles that keep the original ID have a value of zero in a splitting event, whereasparticles given a new ID have a value of one.
     - ✅
   * - .. dropdown:: ``star_formation_rates``

          * **HDF5 name:** ``StarFormationRates``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Star formation rates of the particles.
     - ✅
   * - .. dropdown:: ``temperature_increases_at_last_agnevent``

          * **HDF5 name:** ``TemperatureIncreasesAtLastAGNEvent``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The increase in temperature of the gas at the last AGN feedback event that hit the particles. -1 if the particles have never been heated.
     - ✅
   * - .. dropdown:: ``temperature_increases_at_last_supernova_event``

          * **HDF5 name:** ``TemperatureIncreasesAtLastSupernovaEvent``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The increase in temperature of the gas at the last SN (type-II or type-Ia) thermal feedback event that hit the particles. -1 if the particles have never been heated.
     - ✅
   * - .. dropdown:: ``temperatures``

          * **HDF5 name:** ``Temperatures``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Temperature of the particles
     - ✅
   * - .. dropdown:: ``total_dust_mass_fractions``

          * **HDF5 name:** ``TotalDustMassFractions``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in dust (sum of all grains species)
     - ✅
   * - .. dropdown:: ``total_electron_number_densities``

          * **HDF5 name:** ``TotalElectronNumberDensities``
          * **Shape:** 1
          * **Datatype:** float64
          * **Units:** :math:`\frac{1}{\rm{Mpc}^{3}}`
          * **Compression:** :math:`1.3669345{\rm{}e}10 \rightarrow{} 1.36693{\rm{}e}10`
     - Total electron number densities in the physical frame computed as the sum of the electron number densities from the elements evolved with the non-equilibrium network CHIMES and the electron number densities from the other elements based on the equilibrium cooling tables.
     - ✅
   * - .. dropdown:: ``velocities``

          * **HDF5 name:** ``Velocities``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** 0.1 km/s accurate
     - Peculiar velocities of the particles. This is :math:`a \frac{dx}{dt}` where :math:`x` is the co-moving position of the particles.
     - ✅
   * - .. dropdown:: ``velocity_dispersions``

          * **HDF5 name:** ``VelocityDispersions``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical velocity dispersions (3D) squared, this is the velocity dispersion of the total velocity (peculiar velocity + Hubble flow, a H x + a (dx/dt) ). Values of the Velocity dispersion that have the value of FLT_MAX are particles that do not have neighbours and therefore the velocity dispersion of these particles cannot be calculated
     - ❌
   * - .. dropdown:: ``velocity_divergence_time_differentials``

          * **HDF5 name:** ``VelocityDivergenceTimeDifferentials``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\frac{\rm{km}^{2}}{\rm{Mpc}^{2} \cdot \rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Time differential (over the previous step) of the velocity divergence field around the particles. Again, provided without cosmology as this includes a Hubble flow term.
     - ❌
   * - .. dropdown:: ``velocity_divergences``

          * **HDF5 name:** ``VelocityDivergences``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Local velocity divergence field around the particles. Provided without cosmology, as this includes the Hubble flow.
     - ❌
   * - .. dropdown:: ``viscosity_parameters``

          * **HDF5 name:** ``ViscosityParameters``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Visosity coefficient (alpha_visc) of the particles, multiplied by the balsara switch
     - ❌
   * - .. dropdown:: ``xray_luminosities``

          * **HDF5 name:** ``XrayLuminosities``
          * **Shape:** 3
          * **Datatype:** float64
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{3}}{\rm{Mpc} \cdot \rm{s}^{3}}`
          * **Compression:** :math:`1.3669345{\rm{}e}10 \rightarrow{} 1.36693{\rm{}e}10`
     - Intrinsic X-ray luminosities in various bands. This is 0 for star-forming particles. See :ref:`xray-bands`.
     - ❌
   * - .. dropdown:: ``xray_photon_luminosities``

          * **HDF5 name:** ``XrayPhotonLuminosities``
          * **Shape:** 3
          * **Datatype:** float64
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.3669345{\rm{}e}10 \rightarrow{} 1.36693{\rm{}e}10`
     - Intrinsic X-ray photon luminosities in various bands. This is 0 for star-forming particles. See :ref:`xray-bands`.
     - ❌


Hybrid properties
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Snipshot
   * - .. dropdown:: ``energies_received_from_jet_feedback``

          * **HDF5 name:** ``EnergiesReceivedFromJetFeedback``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Total amount of kinetic energy from AGN jet feedback events received by the particles.
     - ❌
   * - .. dropdown:: ``internal_energy_viscous_time_differentials``

          * **HDF5 name:** ``InternalEnergyViscousTimeDifferentials``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a^{-2.0} \cdot \frac{\rm{km}^{3}}{\rm{Mpc} \cdot \rm{s}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Co-moving time differentials of the internal energy (per unit mass) due to artificial viscosity. This is the rate at which particles are converting their specific kinetic energy to internal energy due to shocks.
     - ❌
   * - .. dropdown:: ``jet_radio_emission_gamma_effective_integrals``

          * **HDF5 name:** ``JetRadioEmissionGammaEffectiveIntegrals``
          * **Shape:** 2
          * **Datatype:** float32
          * **Units:** :math:`10^{20}\ \frac{\rm{M}_\odot^{2} \cdot \rm{km}^{3}}{\rm{Mpc}^{2} \cdot \rm{s}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Integrals over the gamma integrals, which are used to compute values weighted by the shock injection rates as a function of time. These are in physical frame.
     - ❌
   * - .. dropdown:: ``jet_radio_emission_gamma_integrals``

          * **HDF5 name:** ``JetRadioEmissionGammaIntegrals``
          * **Shape:** 2
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}}{\rm{Mpc}^{2} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Integrals over the synchrotron photon and CMB photon energy densities, respectively, in physical frame. These are used for radio emission modeling (see documentation).
     - ❌
   * - .. dropdown:: ``jet_radio_emission_shocking_integrals``

          * **HDF5 name:** ``JetRadioEmissionShockingIntegrals``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The integrals over the shocking rates, used for radio emission modeling, in physical frame. The first integral corresponds to the electron integral, the second to the magnetic field integral, and the last to the 'minimum' auxilliary integral (see documentation).
     - ❌
   * - .. dropdown:: ``kicked_by_jet_feedback``

          * **HDF5 name:** ``KickedByJetFeedback``
          * **Shape:** 1
          * **Datatype:** int8
          * **Units:** dimensionless
          * **Compression:** no compression
     - Flags the particles that have been directly kicked by an AGN jet feedback event at some point in the past. If greater than 0, contains the number of individual events
     - ❌
   * - .. dropdown:: ``last_agnjet_feedback_initial_volumes``

          * **HDF5 name:** ``LastAGNJetFeedbackInitialVolumes``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{Mpc}^{3}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The physical volumes the particles had the last time they were heated by AGN.
     - ❌
   * - .. dropdown:: ``last_agnjet_feedback_scale_factors``

          * **HDF5 name:** ``LastAGNJetFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by jet feedback. -1 if a particle has never been hit by feedback
     - ✅
   * - .. dropdown:: ``last_agnjet_kick_bhid``

          * **HDF5 name:** ``LastAGNJetKickBHId``
          * **Shape:** 1
          * **Datatype:** int8
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - The id of the BH that last kicked this particle.
     - ❌
   * - .. dropdown:: ``last_agnjet_kick_mode``

          * **HDF5 name:** ``LastAGNJetKickMode``
          * **Shape:** 1
          * **Datatype:** int8
          * **Units:** dimensionless
          * **Compression:** no compression
     - The accretion/feedback mode the BH was in when it kicked this particle. 0 corresponds to the thick disc, 1 to the thin disc and 2 to the slim disc.
     - ❌
   * - .. dropdown:: ``last_agnjet_kick_velocities``

          * **HDF5 name:** ``LastAGNJetKickVelocities``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Kick velocity at last AGN jet event.
     - ❌
   * - .. dropdown:: ``weighted_jet_injection_scale_factors``

          * **HDF5 name:** ``WeightedJetInjectionScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - The integral of the scale factor times shocking rate (injection rate of relativistic electrons), in physical frame. Once divided by a similar integral over the shocking rate, we get a weighted scale factor of when most of the injection occurred.
     - ❌


Star particles
--------------

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Snipshot
   * - .. dropdown:: ``ages``

          * **HDF5 name:** ``Ages``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{Mpc} \cdot \rm{s} / \rm{km}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Ages of the stars.
     - ✅
   * - .. dropdown:: ``averaged_star_formation_rates``

          * **HDF5 name:** ``AveragedStarFormationRates``
          * **Shape:** 2
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Star formation rates of the particles averaged over the period set by the first two snapshot triggers. See :ref:`footnote_averaged`
     - ✅
   * - .. dropdown:: ``birth_densities``

          * **HDF5 name:** ``BirthDensities``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot}{\rm{Mpc}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical densities at the time of birth of the gas particles that turned into stars (note that we store the physical density at the birth redshift, no conversion is needed)
     - ✅
   * - .. dropdown:: ``birth_scale_factors``

          * **HDF5 name:** ``BirthScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the stars were born
     - ✅
   * - .. dropdown:: ``birth_temperatures``

          * **HDF5 name:** ``BirthTemperatures``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Temperatures at the time of birth of the gas particles that turned into stars
     - ✅
   * - .. dropdown:: ``birth_velocity_dispersions``

          * **HDF5 name:** ``BirthVelocityDispersions``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical velocity dispersions (3D) squared at the birth time of the gas particles that turned into stars, this is the velocity dispersion of the total velocity (peculiar velocity + Hubble flow, a H x + a (dx/dt) ).
     - ✅
   * - .. dropdown:: ``coordinates``

          * **HDF5 name:** ``Coordinates``
          * **Shape:** 3
          * **Datatype:** float64
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** 1 pc accurate
     - Co-moving position of the particles
     - ✅
   * - .. dropdown:: ``densities_at_last_agnevent``

          * **HDF5 name:** ``DensitiesAtLastAGNEvent``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot}{\rm{Mpc}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical density (not subgrid) of the gas at the last AGN feedback event that hit the particles when they were still gas particles. -1 if the particles have never been heated.
     - ❌
   * - .. dropdown:: ``densities_at_last_supernova_event``

          * **HDF5 name:** ``DensitiesAtLastSupernovaEvent``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot}{\rm{Mpc}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical density (not subgrid) of the gas at the last SN (type-II or type-Ia) thermal feedback event that hit the particles when they were still gas particles. -1 if the particles have never been heated.
     - ❌
   * - .. dropdown:: ``element_mass_fractions``

          * **HDF5 name:** ``ElementMassFractions``
          * **Shape:** 12
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in the given element. ``ReducedElementMassFractions`` is available for snipshots. See :ref:`element-names`.
     - ✅
   * - .. dropdown:: ``energies_received_from_agnfeedback``

          * **HDF5 name:** ``EnergiesReceivedFromAGNFeedback``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Total amount of thermal energy from AGN feedback events received by the particles when the particles were still gas particles.
     - ❌
   * - .. dropdown:: ``fofgroup_ids``

          * **HDF5 name:** ``FOFGroupIDs``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - Friends-Of-Friends ID of the group the particles belong to
     - ✅
   * - .. dropdown:: ``halo_catalogue_index``

          * **HDF5 name:** ``HaloCatalogueIndex``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - Index of halo in which this particle is a bound member, or -1 if none
     - ❌
   * - .. dropdown:: ``initial_masses``

          * **HDF5 name:** ``InitialMasses``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the star particles at birth time
     - ✅
   * - .. dropdown:: ``iron_mass_fractions_from_snia``

          * **HDF5 name:** ``IronMassFractionsFromSNIa``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in iron produced by SNIa stars
     - ✅
   * - .. dropdown:: ``last_agnfeedback_scale_factors``

          * **HDF5 name:** ``LastAGNFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by AGN feedback when they were still gas particles. -1 if a particle has never been hit by feedback
     - ✅
   * - .. dropdown:: ``last_energies_received_from_agnfeedback``

          * **HDF5 name:** ``LastEnergiesReceivedFromAGNFeedback``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The energy the particles received the last time they were heated by AGN feedback while they were still gas particles.
     - ❌
   * - .. dropdown:: ``last_fofhalo_masses``

          * **HDF5 name:** ``LastFOFHaloMasses``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the last FOF haloes the particles where part of when they were still a gas particle. -1 if the particle has never been in a FOF group
     - ✅
   * - .. dropdown:: ``last_fofhalo_masses_scale_factors``

          * **HDF5 name:** ``LastFOFHaloMassesScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particle was last in a FOF group when they were still a gas particle
     - ✅
   * - .. dropdown:: ``last_kinetic_early_feedback_scale_factors``

          * **HDF5 name:** ``LastKineticEarlyFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by kinetic early feedback when they were still gas particles. -1 if a particle has never been hit by feedback
     - ✅
   * - .. dropdown:: ``last_sniikinetic_feedback_scale_factors``

          * **HDF5 name:** ``LastSNIIKineticFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by SNII kinetic feedback when they were still gas particles. -1 if a particle has never been hit by feedback
     - ❌
   * - .. dropdown:: ``last_sniikinetic_feedbackvkick``

          * **HDF5 name:** ``LastSNIIKineticFeedbackvkick``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical kick velocity at last SNII kinetic feedback event when the stellar particles were kicked with when they were still gas particles. -1 if a particle has never been hit by feedback
     - ❌
   * - .. dropdown:: ``last_sniithermal_feedback_scale_factors``

          * **HDF5 name:** ``LastSNIIThermalFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by SNII thermal feedback when they were still gas particles. -1 if a particle has never been hit by feedback
     - ✅
   * - .. dropdown:: ``last_snia_thermal_feedback_scale_factors``

          * **HDF5 name:** ``LastSNIaThermalFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by SNIa thermal feedback when they were still gas particles. -1 if a particle has never been hit by feedback
     - ✅
   * - .. dropdown:: ``luminosities``

          * **HDF5 name:** ``Luminosities``
          * **Shape:** 9
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Rest-frame dust-free AB-luminosities of the star particles in the GAMA bands. See :ref:`luminosities`.
     - ✅
   * - .. dropdown:: ``mass_fractions_from_agb``

          * **HDF5 name:** ``MassFractionsFromAGB``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by AGN stars
     - ✅
   * - .. dropdown:: ``mass_fractions_from_cejsn``

          * **HDF5 name:** ``MassFractionsFromCEJSN``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by common-envelop jets SN events
     - ✅
   * - .. dropdown:: ``mass_fractions_from_collapsar``

          * **HDF5 name:** ``MassFractionsFromCollapsar``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by collapsar events
     - ✅
   * - .. dropdown:: ``mass_fractions_from_nsm``

          * **HDF5 name:** ``MassFractionsFromNSM``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by neutron star merger events
     - ✅
   * - .. dropdown:: ``mass_fractions_from_snii``

          * **HDF5 name:** ``MassFractionsFromSNII``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by SNII stars
     - ✅
   * - .. dropdown:: ``mass_fractions_from_snia``

          * **HDF5 name:** ``MassFractionsFromSNIa``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that have been produced by SNIa stars
     - ✅
   * - .. dropdown:: ``masses``

          * **HDF5 name:** ``Masses``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** no compression
     - Masses of the particles at the current point in time (i.e. after stellar losses)
     - ✅
   * - .. dropdown:: ``maximal_sniikinetic_feedbackvkick``

          * **HDF5 name:** ``MaximalSNIIKineticFeedbackvkick``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Maximal physical kick velocity in SNII kinetic feedback when the stellar particles were kicked with when they were still gas particles. -1 if a particle has never been hit by feedback
     - ❌
   * - .. dropdown:: ``maximal_temperature_scale_factors``

          * **HDF5 name:** ``MaximalTemperatureScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the maximal temperature was reached
     - ✅
   * - .. dropdown:: ``maximal_temperatures``

          * **HDF5 name:** ``MaximalTemperatures``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Maximal temperatures ever reached by the particles before they got converted to stars
     - ✅
   * - .. dropdown:: ``metal_mass_fractions``

          * **HDF5 name:** ``MetalMassFractions``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in metals
     - ✅
   * - .. dropdown:: ``metal_mass_fractions_from_agb``

          * **HDF5 name:** ``MetalMassFractionsFromAGB``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in metals produced by AGB stars
     - ✅
   * - .. dropdown:: ``metal_mass_fractions_from_snii``

          * **HDF5 name:** ``MetalMassFractionsFromSNII``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in metals produced by SNII stars
     - ✅
   * - .. dropdown:: ``metal_mass_fractions_from_snia``

          * **HDF5 name:** ``MetalMassFractionsFromSNIa``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the particles' masses that are in metals produced by SNIa stars
     - ✅
   * - .. dropdown:: ``particle_ids``

          * **HDF5 name:** ``ParticleIDs``
          * **Shape:** 1
          * **Datatype:** uint64
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - Unique ID of the particles
     - ✅
   * - .. dropdown:: ``potentials``

          * **HDF5 name:** ``Potentials``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a^{-1.0} \cdot \rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Gravitational potentials of the particles
     - ✅
   * - .. dropdown:: ``progenitor_particle_ids``

          * **HDF5 name:** ``ProgenitorParticleIDs``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - Progenitor ID of the gas particle that became this star. If this particle is the result of one (or many) splitting events, this ID corresponds to the ID of the particle in the initial conditions that its lineage can be traced back to. If the particle was never split, this is the same as ParticleIDs.
     - ✅
   * - .. dropdown:: ``rank_bound``

          * **HDF5 name:** ``Rank_bound``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - Ranking by binding energy of the bound particles (first in halo=0), or -1 if not bound
     - ❌
   * - .. dropdown:: ``sniifeedback_energy_fractions``

          * **HDF5 name:** ``SNIIFeedbackEnergyFractions``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fractions of the canonical feedback energy that was used for the stars' SNII feedback events
     - ✅
   * - .. dropdown:: ``snia_rates``

          * **HDF5 name:** ``SNIaRates``
          * **Shape:** 1
          * **Datatype:** float64
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.3669345{\rm{}e}10 \rightarrow{} 1.36693{\rm{}e}10`
     - SNIa rate averaged over the last enrichment timestep
     - ✅
   * - .. dropdown:: ``smoothing_lengths``

          * **HDF5 name:** ``SmoothingLengths``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Co-moving smoothing lengths (FWHM of the kernel) of the particles
     - ✅
   * - .. dropdown:: ``specific_potential_energies``

          * **HDF5 name:** ``SpecificPotentialEnergies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** no compression
     - Specific potential energy of the bound particles
     - ❌
   * - .. dropdown:: ``split_counts``

          * **HDF5 name:** ``SplitCounts``
          * **Shape:** 1
          * **Datatype:** uint8
          * **Units:** dimensionless
          * **Compression:** no compression
     - Number of times the gas particle that turned into this star particle was split. Note that both particles that take part in the splitting have their counter incremented.
     - ✅
   * - .. dropdown:: ``split_trees``

          * **HDF5 name:** ``SplitTrees``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - Binary tree describing splitting events. Particles that keep the original ID have a value of zero in a splitting event, whereasparticles given a new ID have a value of one.
     - ✅
   * - .. dropdown:: ``temperature_increases_at_last_agnevent``

          * **HDF5 name:** ``TemperatureIncreasesAtLastAGNEvent``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The increase in temperature of the gas at the last AGN feedback event that hit the particles when they were still gas particles. -1 if the particles have never been heated.
     - ✅
   * - .. dropdown:: ``temperature_increases_at_last_supernova_event``

          * **HDF5 name:** ``TemperatureIncreasesAtLastSupernovaEvent``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The increase in temperature of the gas at the last SN (type-II or type-Ia) thermal feedback event that hit the particles when they were still gas particles. -1 if the particles have never been heated.
     - ✅
   * - .. dropdown:: ``velocities``

          * **HDF5 name:** ``Velocities``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** 0.1 km/s accurate
     - Peculiar velocities of the particles. This is :math:`a \frac{dx}{dt}` where :math:`x` is the co-moving position of the particles.
     - ✅


Hybrid properties
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Snipshot
   * - .. dropdown:: ``energies_received_from_jet_feedback``

          * **HDF5 name:** ``EnergiesReceivedFromJetFeedback``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Total amount of kinetic energy from AGN jet feedback events received by the particles while they were still gas particles.
     - ✅
   * - .. dropdown:: ``kicked_by_jet_feedback``

          * **HDF5 name:** ``KickedByJetFeedback``
          * **Shape:** 1
          * **Datatype:** int8
          * **Units:** dimensionless
          * **Compression:** no compression
     - Flags the particles that have been directly kicked by an AGN jet feedback event at some point in the past. If greater than 0, contains the number of individual events
     - ✅
   * - .. dropdown:: ``last_agnjet_feedback_scale_factors``

          * **HDF5 name:** ``LastAGNJetFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the particles were last hit by jet feedback while they were still gas particles. -1 if a particle has never been hit by feedback
     - ✅
   * - .. dropdown:: ``last_agnjet_kick_bhid``

          * **HDF5 name:** ``LastAGNJetKickBHId``
          * **Shape:** 1
          * **Datatype:** int8
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - The id of the BH that last kicked this particle.
     - ✅
   * - .. dropdown:: ``last_agnjet_kick_mode``

          * **HDF5 name:** ``LastAGNJetKickMode``
          * **Shape:** 1
          * **Datatype:** int8
          * **Units:** dimensionless
          * **Compression:** no compression
     - The accretion/feedback mode the BH was in when it kicked this particle. 0 corresponds to the thick disc, 1 to the thin disc and 2 to the slim disc.
     - ✅
   * - .. dropdown:: ``last_agnjet_kick_velocities``

          * **HDF5 name:** ``LastAGNJetKickVelocities``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Kick velocity at last AGN jet event.
     - ✅


Globular cluster properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Snipshot
   * - .. dropdown:: ``gcs_birth_circular_frequency``

          * **HDF5 name:** ``GCs_BirthCircularFrequency``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Circular frequency at time of star formation
     - ❌
   * - .. dropdown:: ``gcs_birth_epicyclic_frequency``

          * **HDF5 name:** ``GCs_BirthEpicyclicFrequency``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Epicyclic frequency at time of star formation
     - ❌
   * - .. dropdown:: ``gcs_birth_gas_fraction``

          * **HDF5 name:** ``GCs_BirthGasFraction``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Local gas fraction (within cell) at time of star formation
     - ❌
   * - .. dropdown:: ``gcs_birth_toomre_mass``

          * **HDF5 name:** ``GCs_BirthToomreMass``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Local Toomre mass at formation
     - ❌
   * - .. dropdown:: ``gcs_cluster_formation_efficiency``

          * **HDF5 name:** ``GCs_ClusterFormationEfficiency``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fraction of star formation which occurs in bound star clusters
     - ❌
   * - .. dropdown:: ``gcs_cluster_mass_total``

          * **HDF5 name:** ``GCs_ClusterMassTotal``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Sum of surviving star cluster masses
     - ✅
   * - .. dropdown:: ``gcs_cluster_truncation_mass``

          * **HDF5 name:** ``GCs_ClusterTruncationMass``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Exponential truncation of star cluster initial mass function (Mcstar)
     - ❌
   * - .. dropdown:: ``gcs_disruption_scale_factors``

          * **HDF5 name:** ``GCs_DisruptionScaleFactors``
          * **Shape:** 40
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which clusters became disrupted (-1 if surviving)
     - ❌
   * - .. dropdown:: ``gcs_fgas_cell_width``

          * **HDF5 name:** ``GCs_FgasCellWidth``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Cell width at point of gas fraction calculation
     - ❌
   * - .. dropdown:: ``gcs_initial_cluster_mass_evo_lim``

          * **HDF5 name:** ``GCs_InitialClusterMassEvoLim``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Sum of initial star cluster masses above evolution mass limit
     - ❌
   * - .. dropdown:: ``gcs_initial_cluster_mass_total``

          * **HDF5 name:** ``GCs_InitialClusterMassTotal``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Sum of initial star cluster masses
     - ❌
   * - .. dropdown:: ``gcs_initial_masses``

          * **HDF5 name:** ``GCs_InitialMasses``
          * **Shape:** 40
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Initial masses of clusters tagged to particle
     - ❌
   * - .. dropdown:: ``gcs_initial_number_of_clusters``

          * **HDF5 name:** ``GCs_InitialNumberOfClusters``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Number of star clusters tried to form in total
     - ✅
   * - .. dropdown:: ``gcs_initial_number_of_clusters_evo_lim``

          * **HDF5 name:** ``GCs_InitialNumberOfClustersEvoLim``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Number of star clusters formed above evolution mass limit
     - ❌
   * - .. dropdown:: ``gcs_mass_loss_shocks``

          * **HDF5 name:** ``GCs_MassLossShocks``
          * **Shape:** 40
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Cluster mass lost to tidal shocks
     - ❌
   * - .. dropdown:: ``gcs_masses``

          * **HDF5 name:** ``GCs_Masses``
          * **Shape:** 40
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of clusters tagged to particle
     - ❌
   * - .. dropdown:: ``gcs_number_of_clusters``

          * **HDF5 name:** ``GCs_NumberOfClusters``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Surviving number of subgrid star clusters
     - ❌
   * - .. dropdown:: ``gcs_subgrid_field_mass``

          * **HDF5 name:** ``GCs_SubgridFieldMass``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Subgrid field mass component of star particle
     - ✅
   * - .. dropdown:: ``gcs_toomre_collapse_fraction``

          * **HDF5 name:** ``GCs_ToomreCollapseFraction``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Fraction of Toomre mass which can collapse to a GMC
     - ❌
   * - .. dropdown:: ``tidal_tensors``

          * **HDF5 name:** ``TidalTensors``
          * **Shape:** 6
          * **Datatype:** float32
          * **Units:** :math:`a^{-3.0} \cdot \frac{\rm{km}^{2}}{\rm{Mpc}^{2} \cdot \rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Components of co-moving the tidal tensor (Hessian matrix of the gravitational potential). Since the matrix is symmetric, only 6 values per tensor are stored (xx, yy, zz, xy, xz, yz)
     - ✅


Black hole particles
--------------------

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Snipshot
   * - .. dropdown:: ``agntotal_injected_energies``

          * **HDF5 name:** ``AGNTotalInjectedEnergies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Total (cumulative) physical energies injected into gas particles in AGN feedback.
     - ✅
   * - .. dropdown:: ``accreted_angular_momenta``

          * **HDF5 name:** ``AccretedAngularMomenta``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{Mpc} \cdot \rm{M}_\odot \cdot \rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical angular momenta that the black holes have accumulated through subgrid accretion.
     - ✅
   * - .. dropdown:: ``accretion_boost_factors``

          * **HDF5 name:** ``AccretionBoostFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Multiplicative factors by which the Bondi-Hoyle-Lyttleton accretion rates have been increased by the density-dependent Booth & Schaye (2009) accretion model.
     - ✅
   * - .. dropdown:: ``accretion_limited_time_steps``

          * **HDF5 name:** ``AccretionLimitedTimeSteps``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{Mpc} \cdot \rm{s} / \rm{km}`
          * **Compression:** no compression
     - Accretion-limited time steps of black holes. The actual time step of the particles may differ due to the minimum allowed value.
     - ✅
   * - .. dropdown:: ``accretion_rates``

          * **HDF5 name:** ``AccretionRates``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical instantaneous accretion rates of the particles
     - ✅
   * - .. dropdown:: ``averaged_accretion_rates``

          * **HDF5 name:** ``AveragedAccretionRates``
          * **Shape:** 2
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}}{\rm{Mpc} \cdot \rm{s}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Accretion rates of the black holes averaged over the period set by the first two snapshot triggers. See :ref:`footnote_averaged`
     - ✅
   * - .. dropdown:: ``coordinates``

          * **HDF5 name:** ``Coordinates``
          * **Shape:** 3
          * **Datatype:** float64
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** 1 pc accurate
     - Co-moving position of the particles
     - ✅
   * - .. dropdown:: ``cumulative_number_of_seeds``

          * **HDF5 name:** ``CumulativeNumberOfSeeds``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - Total number of BH seeds that have merged into this black hole
     - ✅
   * - .. dropdown:: ``dust_masses``

          * **HDF5 name:** ``DustMasses``
          * **Shape:** 6
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Mass contents of the BH particles in a given dust grain species
     - ✅
   * - .. dropdown:: ``dynamical_masses``

          * **HDF5 name:** ``DynamicalMasses``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** no compression
     - Dynamical masses of the particles
     - ✅
   * - .. dropdown:: ``eddington_fractions``

          * **HDF5 name:** ``EddingtonFractions``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Accretion rates of black holes in units of their Eddington rates. This is based on the unlimited accretion rates, so these fractions can be above the limiting fEdd.
     - ✅
   * - .. dropdown:: ``element_masses``

          * **HDF5 name:** ``ElementMasses``
          * **Shape:** 12
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Mass contents of the BH particles in a given element
     - ✅
   * - .. dropdown:: ``element_masses_diffuse``

          * **HDF5 name:** ``ElementMassesDiffuse``
          * **Shape:** 12
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH that are in the given element and were in the gas phase when accreted
     - ✅
   * - .. dropdown:: ``energy_reservoirs``

          * **HDF5 name:** ``EnergyReservoirs``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physcial energy contained in the feedback reservoir of the particles
     - ✅
   * - .. dropdown:: ``fofgroup_ids``

          * **HDF5 name:** ``FOFGroupIDs``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - Friends-Of-Friends ID of the group the particles belong to
     - ✅
   * - .. dropdown:: ``formation_scale_factors``

          * **HDF5 name:** ``FormationScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the BHs were formed
     - ✅
   * - .. dropdown:: ``gwmass_losses``

          * **HDF5 name:** ``GWMassLosses``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Cumulative masses lost to GW via BH-BH mergers over the history of the black holes. This includes the mass loss from all the progenitors.
     - ✅
   * - .. dropdown:: ``gas_circular_velocities``

          * **HDF5 name:** ``GasCircularVelocities``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Circular velocities of the gas around the black hole at the smoothing radius. This is j / h_BH, where j is the smoothed, peculiar specific angular momentum of gas around the black holes, and h_BH is the smoothing length of each black hole.
     - ✅
   * - .. dropdown:: ``gas_curl_velocities``

          * **HDF5 name:** ``GasCurlVelocities``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Velocity curl (3D) of the gas particles around the black holes.
     - ✅
   * - .. dropdown:: ``gas_densities``

          * **HDF5 name:** ``GasDensities``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot}{\rm{Mpc}^{3}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Co-moving densities of the gas around the particles
     - ✅
   * - .. dropdown:: ``gas_relative_velocities``

          * **HDF5 name:** ``GasRelativeVelocities``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Peculiar relative velocities of the gas particles around the black holes. This is a * dx/dt where x is the co-moving position of the particles.
     - ✅
   * - .. dropdown:: ``gas_sound_speeds``

          * **HDF5 name:** ``GasSoundSpeeds``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a^{-1.0} \cdot \rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Co-moving sound-speeds of the gas around the particles
     - ✅
   * - .. dropdown:: ``gas_temperatures``

          * **HDF5 name:** ``GasTemperatures``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{K}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Temperature of the gas surrounding the black holes.
     - ✅
   * - .. dropdown:: ``gas_velocity_dispersions``

          * **HDF5 name:** ``GasVelocityDispersions``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Velocity dispersion (3D) of the gas particles around the black holes. This is :math:`a \sqrt{<|dx/dt|^2> - <|dx/dt|>^2}` where x is the co-moving position of the particles relative to the black holes.
     - ✅
   * - .. dropdown:: ``halo_catalogue_index``

          * **HDF5 name:** ``HaloCatalogueIndex``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - Index of halo in which this particle is a bound member, or -1 if none
     - ❌
   * - .. dropdown:: ``iron_masses_from_snia``

          * **HDF5 name:** ``IronMassesFromSNIa``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH particles in iron that have been produced by SNIa stars
     - ✅
   * - .. dropdown:: ``iron_masses_from_snia_diffuse``

          * **HDF5 name:** ``IronMassesFromSNIaDiffuse``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH particles in iron that have been produced by SNIa stars and were in the gas phase when accreted
     - ✅
   * - .. dropdown:: ``last_agnfeedback_scale_factors``

          * **HDF5 name:** ``LastAGNFeedbackScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the black holes last had an AGN event.
     - ✅
   * - .. dropdown:: ``last_high_eddington_fraction_scale_factors``

          * **HDF5 name:** ``LastHighEddingtonFractionScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the black holes last reached a large Eddington ratio. -1 if never reached.
     - ✅
   * - .. dropdown:: ``last_major_merger_scale_factors``

          * **HDF5 name:** ``LastMajorMergerScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the black holes last had a major merger.
     - ✅
   * - .. dropdown:: ``last_minor_merger_scale_factors``

          * **HDF5 name:** ``LastMinorMergerScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the black holes last had a minor merger.
     - ✅
   * - .. dropdown:: ``last_reposition_velocities``

          * **HDF5 name:** ``LastRepositionVelocities``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical speeds at which the black holes repositioned most recently. This is 0 for black holes that have never repositioned, or if the simulation has been run without prescribed repositioning speed.
     - ✅
   * - .. dropdown:: ``masses_from_agb``

          * **HDF5 name:** ``MassesFromAGB``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH particles that have been produced by AGB stars
     - ✅
   * - .. dropdown:: ``masses_from_cejsn``

          * **HDF5 name:** ``MassesFromCEJSN``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH particles in europium that have been produced by common-envelop jets SN events
     - ✅
   * - .. dropdown:: ``masses_from_collapsar``

          * **HDF5 name:** ``MassesFromCollapsar``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH particles in europium that have been produced by collapsar events
     - ✅
   * - .. dropdown:: ``masses_from_nsm``

          * **HDF5 name:** ``MassesFromNSM``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH particles in europium that have been produced by neutron star merger events
     - ✅
   * - .. dropdown:: ``masses_from_snii``

          * **HDF5 name:** ``MassesFromSNII``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH particles that have been produced by SNII stars
     - ✅
   * - .. dropdown:: ``masses_from_snia``

          * **HDF5 name:** ``MassesFromSNIa``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH particles that have been produced by SNIa stars
     - ✅
   * - .. dropdown:: ``metal_masses``

          * **HDF5 name:** ``MetalMasses``
          * **Shape:** 12
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Mass contents of the BH particles in a metals
     - ✅
   * - .. dropdown:: ``metal_masses_from_agb``

          * **HDF5 name:** ``MetalMassesFromAGB``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH particles in metals that have been produced by AGB stars
     - ✅
   * - .. dropdown:: ``metal_masses_from_snii``

          * **HDF5 name:** ``MetalMassesFromSNII``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH particles in metals that have been produced by SNII stars
     - ✅
   * - .. dropdown:: ``metal_masses_from_snia``

          * **HDF5 name:** ``MetalMassesFromSNIa``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Masses of the BH particles in metals that have been produced by SNIa stars
     - ✅
   * - .. dropdown:: ``minimal_time_bin_scale_factors``

          * **HDF5 name:** ``MinimalTimeBinScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the minimal time-bin was reached
     - ✅
   * - .. dropdown:: ``minimal_time_bins``

          * **HDF5 name:** ``MinimalTimeBins``
          * **Shape:** 1
          * **Datatype:** int8
          * **Units:** dimensionless
          * **Compression:** no compression
     - Minimal Time Bins reached by the black holes
     - ✅
   * - .. dropdown:: ``number_of_agnevents``

          * **HDF5 name:** ``NumberOfAGNEvents``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - Integer number of AGN events the black hole has had so far (the number of time steps in which the BH did AGN feedback).
     - ✅
   * - .. dropdown:: ``number_of_gas_neighbours``

          * **HDF5 name:** ``NumberOfGasNeighbours``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - Integer number of gas neighbour particles within the black hole kernels.
     - ✅
   * - .. dropdown:: ``number_of_heating_events``

          * **HDF5 name:** ``NumberOfHeatingEvents``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - Integer number of (thermal) energy injections the black hole has had so far. This counts each heated gas particle separately, and so can increase by more than one during a single time step.
     - ✅
   * - .. dropdown:: ``number_of_mergers``

          * **HDF5 name:** ``NumberOfMergers``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - Number of mergers the black holes went through. This does not include the number of mergers accumulated by any merged black hole.
     - ✅
   * - .. dropdown:: ``number_of_repositions``

          * **HDF5 name:** ``NumberOfRepositions``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - Number of repositioning events the black holes went through. This does not include the number of reposition events accumulated by any merged black holes.
     - ✅
   * - .. dropdown:: ``number_of_time_steps``

          * **HDF5 name:** ``NumberOfTimeSteps``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - Total number of time steps at which the black holes were active.
     - ✅
   * - .. dropdown:: ``particle_ids``

          * **HDF5 name:** ``ParticleIDs``
          * **Shape:** 1
          * **Datatype:** uint64
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - Unique ID of the particles
     - ✅
   * - .. dropdown:: ``potentials``

          * **HDF5 name:** ``Potentials``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a^{-1.0} \cdot \rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Gravitational potentials of the particles
     - ✅
   * - .. dropdown:: ``progenitor_particle_ids``

          * **HDF5 name:** ``ProgenitorParticleIDs``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** Store less bits
     - Progenitor ID of the gas particle that became the seed BH. If this particle is the result of one (or many) splitting events, this ID corresponds to the ID of the particle in the initial conditions that its lineage can be traced back to. If the particle was never split, this is the same as ParticleIDs.
     - ✅
   * - .. dropdown:: ``rank_bound``

          * **HDF5 name:** ``Rank_bound``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - Ranking by binding energy of the bound particles (first in halo=0), or -1 if not bound
     - ❌
   * - .. dropdown:: ``smoothing_lengths``

          * **HDF5 name:** ``SmoothingLengths``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`a \cdot \rm{Mpc}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Co-moving smoothing lengths (FWHM of the kernel) of the particles
     - ✅
   * - .. dropdown:: ``specific_potential_energies``

          * **HDF5 name:** ``SpecificPotentialEnergies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km}^{2} / \rm{s}^{2}`
          * **Compression:** no compression
     - Specific potential energy of the bound particles
     - ❌
   * - .. dropdown:: ``split_counts``

          * **HDF5 name:** ``SplitCounts``
          * **Shape:** 1
          * **Datatype:** uint8
          * **Units:** dimensionless
          * **Compression:** no compression
     - Number of times the gas particle that became this BH seed was split. Note that both particles that take part in the splitting have their counter incremented.
     - ✅
   * - .. dropdown:: ``split_trees``

          * **HDF5 name:** ``SplitTrees``
          * **Shape:** 1
          * **Datatype:** int64
          * **Units:** dimensionless
          * **Compression:** no compression
     - Binary tree describing splitting events prior to BH seeding. Particles that keep the original ID have a value of zero in a splitting event, whereas particles given a new ID have a value of one.
     - ✅
   * - .. dropdown:: ``subgrid_masses``

          * **HDF5 name:** ``SubgridMasses``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Subgrid masses of the particles
     - ✅
   * - .. dropdown:: ``swallowed_angular_momenta``

          * **HDF5 name:** ``SwallowedAngularMomenta``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{Mpc} \cdot \rm{M}_\odot \cdot \rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Physical angular momenta that the black holes have accumulated by swallowing gas particles.
     - ✅
   * - .. dropdown:: ``total_accreted_masses``

          * **HDF5 name:** ``TotalAccretedMasses``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Total mass accreted onto the main progenitor of the black holes since birth. This does not include any mass accreted onto any merged black holes.
     - ✅
   * - .. dropdown:: ``velocities``

          * **HDF5 name:** ``Velocities``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** 0.1 km/s accurate
     - Peculiar velocities of the particles. This is :math:`a \frac{dx}{dt}` where :math:`x` is the co-moving position of the particles.
     - ✅


Hybrid properties
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Snipshot
   * - .. dropdown:: ``agntotal_injected_energies_by_mode``

          * **HDF5 name:** ``AGNTotalInjectedEnergiesByMode``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The total energy injected in the thermal AGN feedback mode, including the contributions of both radiation and wind feedback, split by accretion mode. The components correspond to the thermal energy dumped in the thick, thin and slim disc modes, respectively.
     - ✅
   * - .. dropdown:: ``accretion_modes``

          * **HDF5 name:** ``AccretionModes``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - Accretion flow regime. 0 - Thick disk, 1 - Thin disk, 2 - Slim disk
     - ✅
   * - .. dropdown:: ``angular_momentum_directions``

          * **HDF5 name:** ``AngularMomentumDirections``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Direction of the black hole spin vector, normalised to unity.
     - ✅
   * - .. dropdown:: ``cos_accretion_disk_angle``

          * **HDF5 name:** ``CosAccretionDiskAngle``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Cosine of the angle between the spin vector and the accreting gas angular momentum.
     - ✅
   * - .. dropdown:: ``injected_jet_energies``

          * **HDF5 name:** ``InjectedJetEnergies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Total jet energy injected into AGN surroundings.
     - ✅
   * - .. dropdown:: ``injected_jet_energies_by_mode``

          * **HDF5 name:** ``InjectedJetEnergiesByMode``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The total energy injected in the kinetic jet AGN feedback mode, split by accretion mode. The components correspond to the jet energy dumped in the thick, thin and slim disc modes, respectively.
     - ✅
   * - .. dropdown:: ``jet_efficiencies``

          * **HDF5 name:** ``JetEfficiencies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Jet power divided by accretion rate.
     - ✅
   * - .. dropdown:: ``jet_reservoir``

          * **HDF5 name:** ``JetReservoir``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Total jet energy waiting to be released (once it grows large enough to kick a single particle).
     - ✅
   * - .. dropdown:: ``jet_time_steps``

          * **HDF5 name:** ``JetTimeSteps``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{Mpc} \cdot \rm{s} / \rm{km}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Jet-launching-limited time-steps of black holes.
     - ✅
   * - .. dropdown:: ``jet_velocities``

          * **HDF5 name:** ``JetVelocities``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`\rm{km} / \rm{s}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The current jet velocities.
     - ✅
   * - .. dropdown:: ``last_agnjet_scale_factors``

          * **HDF5 name:** ``LastAGNJetScaleFactors``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
     - Scale-factors at which the black holes last had an AGN jet event.
     - ✅
   * - .. dropdown:: ``number_of_agnjet_events``

          * **HDF5 name:** ``NumberOfAGNJetEvents``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - Integer number of AGN jet launching events the black hole has had (the number of times the BH did AGN jet feedback)
     - ✅
   * - .. dropdown:: ``number_of_jet_particles_launched``

          * **HDF5 name:** ``NumberOfJetParticlesLaunched``
          * **Shape:** 1
          * **Datatype:** int32
          * **Units:** dimensionless
          * **Compression:** no compression
     - Integer number of (kinetic) energy injections the black hole has had so far
     - ✅
   * - .. dropdown:: ``radiated_energies_by_mode``

          * **HDF5 name:** ``RadiatedEnergiesByMode``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The total energy launched into radiation by the black holes, split by accretion mode. The components correspond to the radiative energy dumped in the thick, thin and slim disc modes, respectively.
     - ✅
   * - .. dropdown:: ``radiative_efficiencies``

          * **HDF5 name:** ``RadiativeEfficiencies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - AGN luminosity divided by accretion rate.
     - ✅
   * - .. dropdown:: ``spins``

          * **HDF5 name:** ``Spins``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - Dimensionless spins of the black holes. Negative values indicate retrograde accretion.
     - ✅
   * - .. dropdown:: ``total_accreted_masses_by_mode``

          * **HDF5 name:** ``TotalAccretedMassesByMode``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \rm{M}_\odot`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The total accreted mass in each accretion mode. The components to the mass accreted in the thick, thin and slim disc modes, respectively.
     - ✅
   * - .. dropdown:: ``total_radiated_energies``

          * **HDF5 name:** ``TotalRadiatedEnergies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The total energy launched into radiation by the black holes, in all accretion modes. 
     - ✅
   * - .. dropdown:: ``total_wind_energies``

          * **HDF5 name:** ``TotalWindEnergies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The total energy launched into accretion disc winds by the black holes, in all accretion modes. 
     - ✅
   * - .. dropdown:: ``wind_efficiencies``

          * **HDF5 name:** ``WindEfficiencies``
          * **Shape:** 1
          * **Datatype:** float32
          * **Units:** dimensionless
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The wind efficiencies of the black holes.
     - ✅
   * - .. dropdown:: ``wind_energies_by_mode``

          * **HDF5 name:** ``WindEnergiesByMode``
          * **Shape:** 3
          * **Datatype:** float32
          * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{2}}{\rm{s}^{2}}`
          * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
     - The total energy launched into accretion disc winds by the black holes, split by accretion mode. The components correspond to the radiative energy dumped in the thick, thin and slim disc modes, respectively.
     - ✅


Footnotes
---------


.. _footnote_averaged:

Averaged quantities
~~~~~~~~~~~~~~~~~~~

Averaged quantities are calculated by accumulating 
the quantity over the 10 Myr/100 Myr that precedes the writing of a 
snapshot, and then normalizing. For example, for SFR, we start a clock 
precisely 10 Myr before a snapshot dump, accumulate SFR * dt at each 
step during that window, and then divide by 10 Myr at the point of writing.
AveragedStarFormationRates for star particles should not be used.

.. _dust-names:

Dust fractions
~~~~~~~~~~~~~~

The ``DustMassFractions`` dataset contains the following species.

+-------------+---------------------+
| Array index | Species name        |
+=============+=====================+
| 0           | GraphiteLarge       |
+-------------+---------------------+
| 1           | GraphiteSmall       |
+-------------+---------------------+
| 2           | MgSilicatesLarge    |
+-------------+---------------------+
| 3           | MgSilicatesSmall    |
+-------------+---------------------+
| 4           | FeSilicatesLarge    |
+-------------+---------------------+
| 5           | FeSilicatesSmall    |
+-------------+---------------------+

.. _element-names:

Element fractions
~~~~~~~~~~~~~~~~~

The ``ElementMassFractions`` and ``ElementMassFractionsDiffuse``
datasets contain the following elements.

+-------------+---------------------+
| Array index | Element name        |
+=============+=====================+
| 0           | Hydrogen            |
+-------------+---------------------+
| 1           | Helium              |
+-------------+---------------------+
| 2           | Carbon              |
+-------------+---------------------+
| 3           | Nitrogen            |
+-------------+---------------------+
| 4           | Oxygen              |
+-------------+---------------------+
| 5           | Neon                |
+-------------+---------------------+
| 6           | Magnesium           |
+-------------+---------------------+
| 7           | Silicon             |
+-------------+---------------------+
| 8           | Iron                |
+-------------+---------------------+
| 9           | Strontium           |
+-------------+---------------------+
| 10          | Barium              |
+-------------+---------------------+
| 11          | Europium            |
+-------------+---------------------+

The ``ReducedElementMassFractions`` dataset contains the following elements.

+-------------+---------------------+
| Array index | Element name        |
+=============+=====================+
| 0           | Hydrogen            |
+-------------+---------------------+
| 1           | Helium              |
+-------------+---------------------+

.. _species-names:

Species fractions
~~~~~~~~~~~~~~~~~

The ``SpeciesFractions`` dataset contains the following species.
Note that the fraction of species i in this dataset is defined 
in terms of its number density relative to hydrogen (i.e.
:math:`n_i` / :math:`n_{H_{tot}}`), which is not the same as the mass fraction.

+-------------+---------------------+
| Array index | Species name        |
+=============+=====================+
| 0           | Electron            |
+-------------+---------------------+
| 1           | HI                  |
+-------------+---------------------+
| 2           | HII                 |
+-------------+---------------------+
| 3           | Hm                  |
+-------------+---------------------+
| 4           | HeI                 |
+-------------+---------------------+
| 5           | HeII                |
+-------------+---------------------+
| 6           | HeIII               |
+-------------+---------------------+
| 7           | H2                  |
+-------------+---------------------+
| 8           | H2p                 |
+-------------+---------------------+
| 9           | H3p                 |
+-------------+---------------------+

The ``ReducedSpeciesFractions`` dataset contains the following elements.

+-------------+---------------------+
| Array index | Species name        |
+=============+=====================+
| 0           | HI                  |
+-------------+---------------------+
| 1           | HeI                 |
+-------------+---------------------+
| 2           | HeII                |
+-------------+---------------------+
| 3           | H2                  |
+-------------+---------------------+

.. _xray-bands:

X-ray bands
~~~~~~~~~~~

Gas particles have ``XrayLuminosities`` (energy per unit time) and
``XrayPhotonLuminosities`` (number of photons per unit time) datasets
which contain data for three different observer frame X-ray bands:

+-------------+---------------------+
| Array index | Band                |
+=============+=====================+
| 0           | eROSITA 0.2-2.3keV  |
+-------------+---------------------+
| 1           | eROSITA 2.3-8.0keV  |
+-------------+---------------------+
| 2           | ROSAT 0.5-2.0keV    |
+-------------+---------------------+

.. _luminosities:

Stellar luminosities
~~~~~~~~~~~~~~~~~~~~

.. warning:: Star particle "luminosities" are stored in terms of flux
             and do NOT use the same units as the X-ray luminosity
             datasets described above.

Star particles have a ``Luminosities`` dataset. For each particle and
photometric band this contains the rest frame flux at 10pc, expressed
in maggies. Maggies are a dimensionless measure of flux defined as the
ratio :math:`F/F_0`, where :math:`F_0=3631\mathrm{Jy}` is the flux
corresponding to an AB magnitude of zero. Dust extinction is not
included. These were computed using the `BC03
<https://ui.adsabs.harvard.edu/abs/2003MNRAS.344.1000B/abstract>`_
(GALAXEV) models convolved with the different filter bands, as used in
the dust-free modelling of `Trayford et al. (2015)
<https://ui.adsabs.harvard.edu/abs/2015MNRAS.452.2879T/abstract>`_.

The rest frame, absolute AB-magnitude can be computed as:

  :math:`M = -2.5 \log10(L)`

where ``L`` is the dimensionless number stored in the
dataset. Luminosities for the `GAMA <https://www.gama-survey.org/>`__
bands are stored in the following order:

+-------------+---------------------+
| Array index | Band                |
+=============+=====================+
| 0           | u                   |
+-------------+---------------------+
| 1           | g                   |
+-------------+---------------------+
| 2           | r                   |
+-------------+---------------------+
| 3           | i                   |
+-------------+---------------------+
| 4           | z                   |
+-------------+---------------------+
| 5           | Y                   |
+-------------+---------------------+
| 6           | J                   |
+-------------+---------------------+
| 7           | H                   |
+-------------+---------------------+
| 8           | K                   |
+-------------+---------------------+

.. _hii_end_time:

HII regions end time
~~~~~~~~~~~~~~~~~~~~

This property was originally not enabled to be output, and so is completely missing
from certain runs, is only available for low redshift outputs of other runs.


