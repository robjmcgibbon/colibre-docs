Particle properties in the lightcones
=====================================

This page documents all of the properties which are stored for each
type of particle in the FLAMINGO lightcone particle outputs.

In the Units column in the tables below we use :math:`a` to indicate
the expansion factor. Comoving megaparsecs are expressed as
:math:`a\mathrm{Mpc}`, but note that the expansion factor varies with
comoving distance from the observer so coordinates cannot be converted
to physical units with a simple multiplication. In the Shape column, N
indicates the number of particles in the dataset.

Gas particles
-------------

Gas particles are stored in the HDF5 group ``/Gas`` in the lightcone
particle files. This group contains HDF5 datasets which store the
following particle properties:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Type
     - Shape
     - Units
     - Description
   * - ``ComptonYParameters``
     - float64
     - N
     - :math:`\mathrm{Mpc}^{2}`
     - Compton y parameters in the physical frame computed based on the cooling tables. This is 0 for star-forming particles.
   * - ``Coordinates``
     - float64
     - N, 3
     - :math:`a\mathrm{Mpc}`
     - Co-moving position of the particle relative to the observer at the time of lightcone crossing
   * - ``Densities``
     - float32
     - N
     - :math:`a^{-3}10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-3}`
     - Co-moving mass densities of the particles
   * - ``ElectronNumberDensities``
     - float64
     - N
     - :math:`\mathrm{Mpc}^{-3}`
     - Electron number densities in the physical frame computed based on the cooling tables. This is 0 for star-forming particles.
   * - ``ExpansionFactors``
     - float32
     - N
     - :math:`-`
     - Expansion factor at which this particle crossed the observer's lightcone
   * - ``FOFGroupIDs``
     - int64
     - N
     - :math:`-`
     - Friends-Of-Friends ID of the group the particle belonged to at
       the last FoF calculation before the particle was output. Note
       that this relates to the on-the-fly FoF used for black hole
       seeding. FoF was run again with different parameters for
       HBT-HERONS and SOAP.
   * - ``LastAGNFeedbackScaleFactors``
     - float32
     - N
     - :math:`-`
     - Scale-factors at which the particles were last hit by AGN feedback. -1 if a particle has never been hit by feedback
   * - ``Masses``
     - float32
     - N
     - :math:`10^{10}\mathrm{M}_\odot`
     - Masses of the particles
   * - ``MetalMassFractions``
     - float32
     - N
     - :math:`-`
     - Fractions of the particles' masses that are in metals
   * - ``ParticleIDs``
     - int64
     - N
     - :math:`-`
     - Unique IDs of the particles
   * - ``SmoothedElementMassFractions``
     - float32
     - N, 9
     - :math:`-`
     - Smoothed fractions of the particles' masses that are in the given element
   * - ``SmoothedMetalMassFractions``
     - float32
     - N
     - :math:`-`
     - Smoothed fractions of the particles masses that are in metals
   * - ``SmoothingLengths``
     - float32
     - N
     - :math:`\mathrm{Mpc}`
     - Co-moving smoothing lengths (FWHM of the kernel) of the particles
   * - ``StarFormationRates``
     - float32
     - N
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-1}\mathrm{km/s}`
     - If positive, star formation rates of the particles. If negative, stores the last time/scale-factor at which the gas particle was star-forming. If zero, the particle was never star-forming.
   * - ``Temperatures``
     - float32
     - N
     - :math:`\mathrm{K}`
     - Temperatures of the gas particles
   * - ``Velocities``
     - float32
     - N, 3
     - :math:`\mathrm{km/s}`
     - Peculiar velocities of the stars. This is :math:`(a * dx/dt)` where :math:`x` is the co-moving positions of the particles

Dark matter particles
---------------------

Dark matter particles are stored in the HDF5 group ``/DM`` in the
lightcone particle files. This group contains HDF5 datasets which
store the following particle properties:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Type
     - Shape
     - Units
     - Description
   * - ``Coordinates``
     - float64
     - N, 3
     - :math:`a\mathrm{Mpc}`
     - Co-moving position of the particle relative to the observer at the time of lightcone crossing
   * - ``ExpansionFactors``
     - float32
     - N
     - :math:`-`
     - Expansion factor at which this particle crossed the observer's lightcone
   * - ``Masses``
     - float32
     - N
     - :math:`10^{10}\mathrm{M}_\odot`
     - Masses of the particles
   * - ``ParticleIDs``
     - int64
     - N
     - :math:`-`
     - Unique ID of the particles
   * - ``Velocities``
     - float32
     - N, 3
     - :math:`\mathrm{km/s}`
     - Peculiar velocities of the stars. This is :math:`a * dx/dt` where :math:`x` is the co-moving position of the particles.

Star particles
--------------

Star particles are stored in the HDF5 group ``/Stars`` in the
lightcone particle files. This group contains HDF5 datasets which
store the following particle properties:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Type
     - Shape
     - Units
     - Description
   * - ``BirthDensities``
     - float32
     - N
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-3}`
     - Physical densities at the time of birth of the gas particles that turned into stars (note that we store the physical density at the birth redshift, no conversion is needed)
   * - ``BirthScaleFactors``
     - float32
     - N
     - :math:`-`
     - Scale-factors at which the stars were born
   * - ``Coordinates``
     - float64
     - N, 3
     - :math:`a\mathrm{Mpc}`
     - Co-moving position of the particle relative to the observer at the time of lightcone crossing
   * - ``ExpansionFactors``
     - float32
     - N
     - :math:`-`
     - Expansion factor at which this particle crossed the observer's lightcone
   * - ``FOFGroupIDs``
     - int64
     - N
     - :math:`-`
     - Friends-Of-Friends ID of the group the particle belonged to at
       the last FoF calculation before the particle was output. Note
       that this relates to the on-the-fly FoF used for black hole
       seeding. FoF was run again with different parameters for
       HBT-HERONS and SOAP.
   * - ``InitialMasses``
     - float32
     - N
     - :math:`10^{10}\mathrm{M}_\odot`
     - Masses of the star particles at birth time
   * - ``LastAGNFeedbackScaleFactors``
     - float32
     - N
     - :math:`-`
     - Scale-factors at which the particles were last hit by AGN feedback. -1 if a particle has never been hit by feedback
   * - ``Luminosities``
     - float32
     - N, 9
     - :math:`-`
     - Rest-frame, dust-free AB flux at 10pc distance in each of the GAMA bands (see :ref:`luminosities` for details)
   * - ``Masses``
     - float32
     - N
     - :math:`10^{10}\mathrm{M}_\odot`
     - Masses of the particles at the current point in time (i.e. after stellar losses
   * - ``MetalMassFractions``
     - float32
     - N
     - :math:`-`
     - Fractions of the particles' masses that are in metals
   * - ``ParticleIDs``
     - int64
     - N
     - :math:`-`
     - Unique ID of the particles
   * - ``SmoothedElementMassFractions``
     - float32
     - N, 9
     - :math:`-`
     - Smoothed fractions of the particles' masses that are in the given element
   * - ``SmoothedMetalMassFractions``
     - float32
     - N
     - :math:`-`
     - Smoothed fractions of the particles masses that are in metals
   * - ``Velocities``
     - float32
     - N, 3
     - :math:`\mathrm{km/s}`
     - Peculiar velocities of the particles. This is :math:`a * dx/dt` where x is the co-moving position of the particles.

Black hole particles
--------------------

Black hole particles are stored in the HDF5 group ``/BH`` in the
lightcone particle files. This group contains HDF5 datasets which
store the following particle properties.

.. note:: Runs using the jet AGN feedback model only contain
          ``Coordinates``, ``DynamicalMasses``, ``ExpansionFactors``,
          ``ParticleIDs`` and ``Velocities`` datasets for black hole
          particles in the lightcone.

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Type
     - Shape
     - Units
     - Description
   * - ``AccretionRates``
     - float32
     - N
     - :math:`10^{10}\mathrm{M}_\odot\mathrm{Mpc}^{-1}\mathrm{km/s}`
     - Physical instantaneous accretion rates of the particles
   * - ``Coordinates``
     - float64
     - N, 3
     - :math:`a\mathrm{Mpc}`
     - Co-moving position of the particle relative to the observer at the time of lightcone crossing
   * - ``CumulativeNumberOfSeeds``
     - int32
     - N
     - :math:`-`
     - Total number of BH seeds that have merged into this black hole
   * - ``DynamicalMasses``
     - float32
     - N
     - :math:`10^{10}\mathrm{M}_\odot`
     - Dynamical masses of the black hole particles
   * - ``ExpansionFactors``
     - float32
     - N
     - :math:`-`
     - Expansion factor at which this particle crossed the observer's lightcone
   * - ``FOFGroupIDs``
     - int64
     - N
     - :math:`-`
     - Friends-Of-Friends ID of the group the particle belonged to at
       the last FoF calculation before the particle was output. Note
       that this relates to the on-the-fly FoF used for black hole
       seeding. FoF was run again with different parameters for
       HBT-HERONS and SOAP.
   * - ``FormationScaleFactors``
     - float32
     - N
     - :math:`-`
     - Scale-factors at which the BHs were formed
   * - ``LastAGNFeedbackScaleFactors``
     - float32
     - N
     - :math:`-`
     - Scale-factors at which the black holes last had an AGN event.
   * - ``LastHighEddingtonFractionScaleFactors``
     - float32
     - N
     - :math:`-`
     - Scale-factors at which the black holes last reached an Eddington ratio greater than 0.1. -1 if never reached.
   * - ``LastMajorMergerScaleFactors``
     - float32
     - N
     - :math:`-`
     - Scale-factors at which the black holes last had a major merger.
   * - ``LastMinorMergerScaleFactors``
     - float32
     - N
     - :math:`-`
     - Scale-factors at which the black holes last had a minor merger.
   * - ``NumberOfAGNEvents``
     - int32
     - N
     - :math:`-`
     - Integer number of AGN events the black hole has had so far (the number of times the BH did AGN feedback)
   * - ``NumberOfHeatingEvents``
     - int32
     - N
     - :math:`-`
     - Integer number of (thermal) energy injections the black hole has had so far
   * - ``NumberOfMergers``
     - int32
     - N
     - :math:`-`
     - Number of mergers the black holes went through. This does not include the number of mergers accumulated by any merged black hole.
   * - ``ParticleIDs``
     - int64
     - N
     - :math:`-`
     - Unique ID of the particles
   * - ``SubgridMasses``
     - float32
     - N
     - :math:`10^{10}\mathrm{M}_\odot`
     - Subgrid masses of the black hole particles
   * - ``TotalAccretedMasses``
     - float32
     - N
     - :math:`10^{10}\mathrm{M}_\odot`
     - Total mass accreted onto the particle since its birth
   * - ``Velocities``
     - float32
     - N, 3
     - :math:`\mathrm{km/s}`
     - Peculiar velocities of the particles. This is :math:`a * dx/dt` where :math:`x` is the co-moving position of the particles.

Neutrino particles
------------------

Neutrino particles are stored in the HDF5 group ``/Neutrino`` in the
lightcone particle files. This group contains HDF5 datasets which
store the following particle properties:

.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Type
     - Shape
     - Units
     - Description
   * - ``Coordinates``
     - float64
     - N, 3
     - :math:`a\mathrm{Mpc}`
     - Co-moving position of the particle relative to the observer at the time of lightcone crossing
   * - ``ExpansionFactors``
     - float32
     - N
     - :math:`-`
     - Expansion factor at which this particle crossed the observer's lightcone
   * - ``Masses``
     - float32
     - N
     - :math:`10^{10}\mathrm{M}_\odot`
     - Masses of the particles
   * - ``ParticleIDs``
     - int64
     - N
     - :math:`-`
     - Unique ID of the particles
   * - ``Velocities``
     - float32
     - N, 3
     - :math:`\mathrm{km/s}`
     - Peculiar velocities of the stars. This is :math:`a * dx/dt` where x is the co-moving position of the particles.
