High cadence runs
=================

The following high cadence runs were used to generate the videos on the COLIBRE website:

* ``/cosma8/data/dp004/colibre/Runs/L0050N0752/Thermal_HighCadence`` - L050m6 run with 2000 outputs
* ``/cosma8/data/dp004/colibre/Runs/L0050N0752/Hybrid_HighCadence`` - L050m6h run with 2000 outputs
* ``/cosma8/data/dp004/colibre/Runs/L0012N0376/Thermal_HighCadence`` - L012m5 run with 10000 outputs

For all these high cadence runs the outputs are evenly spaced in :math:`\log a`.

* :math:`\Delta \log a \approx 0.0075` for the L050m6 runs
* :math:`\Delta \log a \approx 0.00015` for the L012m5 run

They have the same initial conditions and subgrid model parameters as the fiducial runs.
However, due to noise within the simulations, the galaxies that form in these
runs will not be exactly the same as those in the fiducial runs.

There are only a few particle properties saved for these runs,
significantly fewer than in the normal snapshots.
Most of the dark matter particles have been removed,
although 10% of them have been kept for every 10th snapshot.

.. dropdown:: Dark matter particle properties

   .. list-table::
      :header-rows: 1

      * - Name
        - Description
      * - .. dropdown:: ``coordinates``

             * **HDF5 name:** ``Coordinates``
             * **Shape:** 3
             * **Datatype:** float64
             * **Units:** :math:`a \cdot \rm{Mpc}`
             * **Compression:** 1 pc accurate
        - Co-moving position of the particles
      * - .. dropdown:: ``fofgroup_ids``

             * **HDF5 name:** ``FOFGroupIDs``
             * **Shape:** 1
             * **Datatype:** int64
             * **Units:** dimensionless
             * **Compression:** Store less bits
        - Friends-Of-Friends ID of the group the particles belong to
      * - .. dropdown:: ``masses``

             * **HDF5 name:** ``Masses``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`10^{10}\ \rm{M}_\odot`
             * **Compression:** no compression
        - Masses of the particles
      * - .. dropdown:: ``particle_ids``

             * **HDF5 name:** ``ParticleIDs``
             * **Shape:** 1
             * **Datatype:** uint64
             * **Units:** dimensionless
             * **Compression:** Store less bits
        - Unique ID of the particles
      * - .. dropdown:: ``velocities``

             * **HDF5 name:** ``Velocities``
             * **Shape:** 3
             * **Datatype:** float32
             * **Units:** :math:`\rm{km} / \rm{s}`
             * **Compression:** 0.1 km/s accurate
        - Peculiar velocities of the particles. This is :math:`a \frac{dx}{dt}` where :math:`x` is the co-moving position of the particles.

.. dropdown:: Gas particle properties

   .. list-table::
      :header-rows: 1

      * - Name
        - Description
      * - .. dropdown:: ``atomic_hydrogen_masses``

             * **HDF5 name:** ``AtomicHydrogenMasses``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`10^{10}\ \rm{M}_\odot`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Atomic hydrogen masses contained in the particles. This quantity is obtained from the cooling tables and, if the particle is on the entropy floor, by extrapolating to the equilibrium curve assuming constant pressure.
      * - .. dropdown:: ``coordinates``

             * **HDF5 name:** ``Coordinates``
             * **Shape:** 3
             * **Datatype:** float64
             * **Units:** :math:`a \cdot \rm{Mpc}`
             * **Compression:** 1 pc accurate
        - Co-moving positions of the particles
      * - .. dropdown:: ``densities``

             * **HDF5 name:** ``Densities``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`a^{-3.0} \cdot 10^{10}\ \frac{\rm{M}_\odot}{\rm{Mpc}^{3}}`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Co-moving mass densities of the particles
      * - .. dropdown:: ``last_agnfeedback_scale_factors``

             * **HDF5 name:** ``LastAGNFeedbackScaleFactors``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** dimensionless
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
        - Scale-factors at which the particles were last hit by AGN feedback. -1 if a particle has never been hit by feedback
      * - .. dropdown:: ``last_snia_thermal_feedback_scale_factors``

             * **HDF5 name:** ``LastSNIaThermalFeedbackScaleFactors``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** dimensionless
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
        - Scale-factors at which the particles were last hit by SNIa thermal feedback. -1 if a particle has never been hit by feedback
      * - .. dropdown:: ``last_sniithermal_feedback_scale_factors``

             * **HDF5 name:** ``LastSNIIThermalFeedbackScaleFactors``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** dimensionless
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
        - Scale-factors at which the particles were last hit by SNII thermal feedback. -1 if a particle has never been hit by feedback
      * - .. dropdown:: ``masses``

             * **HDF5 name:** ``Masses``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`10^{10}\ \rm{M}_\odot`
             * **Compression:** no compression
        - Masses of the particles
      * - .. dropdown:: ``metal_mass_fractions``

             * **HDF5 name:** ``MetalMassFractions``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** dimensionless
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Fractions of the particles' masses that are in metals (incorporating both depleted and nebular phases)
      * - .. dropdown:: ``molecular_hydrogen_masses``

             * **HDF5 name:** ``MolecularHydrogenMasses``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`10^{10}\ \rm{M}_\odot`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Molecular hydrogen masses contained in the particles. This quantity is obtained from the cooling tables and, if the particle is on the entropy floor, by extrapolating to the equilibrium curve assuming constant pressure.
      * - .. dropdown:: ``particle_ids``

             * **HDF5 name:** ``ParticleIDs``
             * **Shape:** 1
             * **Datatype:** uint64
             * **Units:** dimensionless
             * **Compression:** Store less bits
        - Unique IDs of the particles
      * - .. dropdown:: ``smoothing_lengths``

             * **HDF5 name:** ``SmoothingLengths``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`a \cdot \rm{Mpc}`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Co-moving smoothing lengths (FWHM of the kernel) of the particles
      * - .. dropdown:: ``star_formation_rates``

             * **HDF5 name:** ``StarFormationRates``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}}{\rm{Mpc} \cdot \rm{s}}`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Star formation rates of the particles.
      * - .. dropdown:: ``temperatures``

             * **HDF5 name:** ``Temperatures``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`\rm{K}`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Temperature of the particles
      * - .. dropdown:: ``total_dust_mass_fractions``

             * **HDF5 name:** ``TotalDustMassFractions``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** dimensionless
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Fractions of the particles' masses that are in dust (sum of all grain species)
      * - .. dropdown:: ``velocities``

             * **HDF5 name:** ``Velocities``
             * **Shape:** 3
             * **Datatype:** float32
             * **Units:** :math:`\rm{km} / \rm{s}`
             * **Compression:** 0.1 km/s accurate
        - Peculiar velocities of the particles. This is :math:`a \frac{dx}{dt}` where :math:`x` is the co-moving position of the particles.
      * - .. dropdown:: ``velocity_divergence_time_differentials``

             * **HDF5 name:** ``VelocityDivergenceTimeDifferentials``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`\frac{\rm{km}^{2}}{\rm{Mpc}^{2} \cdot \rm{s}^{2}}`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Time differential (over the previous step) of the velocity divergence field around the particles. Again, provided without cosmology as this includes a Hubble flow term.
      * - .. dropdown:: ``velocity_divergences``

             * **HDF5 name:** ``VelocityDivergences``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`\frac{\rm{km}}{\rm{Mpc} \cdot \rm{s}}`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Local velocity divergence field around the particles. Provided without cosmology, as this includes the Hubble flow.
      * - .. dropdown:: ``xray_luminosities``

             * **HDF5 name:** ``XrayLuminosities``
             * **Shape:** 3
             * **Datatype:** float64
             * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}^{3}}{\rm{Mpc} \cdot \rm{s}^{3}}`
             * **Compression:** :math:`1.3669345{\rm{}e}10 \rightarrow{} 1.36693{\rm{}e}10`
        - Intrinsic X-ray luminosities in various bands. This is 0 for star-forming particles. See :ref:`xray-bands`.

.. dropdown:: Star particle properties

   .. list-table::
      :header-rows: 1

      * - Name
        - Description
      * - .. dropdown:: ``ages``

             * **HDF5 name:** ``Ages``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`\rm{Mpc} \cdot \rm{s} / \rm{km}`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Ages of the stars.
      * - .. dropdown:: ``coordinates``

             * **HDF5 name:** ``Coordinates``
             * **Shape:** 3
             * **Datatype:** float64
             * **Units:** :math:`a \cdot \rm{Mpc}`
             * **Compression:** 1 pc accurate
        - Co-moving position of the particles
      * - .. dropdown:: ``initial_masses``

             * **HDF5 name:** ``InitialMasses``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`10^{10}\ \rm{M}_\odot`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Masses of the star particles at birth time
      * - .. dropdown:: ``masses``

             * **HDF5 name:** ``Masses``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`10^{10}\ \rm{M}_\odot`
             * **Compression:** no compression
        - Masses of the particles at the current point in time (i.e. after stellar losses)
      * - .. dropdown:: ``metal_mass_fractions``

             * **HDF5 name:** ``MetalMassFractions``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** dimensionless
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Fractions of the particles' masses that are in metals
      * - .. dropdown:: ``particle_ids``

             * **HDF5 name:** ``ParticleIDs``
             * **Shape:** 1
             * **Datatype:** uint64
             * **Units:** dimensionless
             * **Compression:** Store less bits
        - Unique ID of the particles
      * - .. dropdown:: ``velocities``

             * **HDF5 name:** ``Velocities``
             * **Shape:** 3
             * **Datatype:** float32
             * **Units:** :math:`\rm{km} / \rm{s}`
             * **Compression:** 0.1 km/s accurate
        - Peculiar velocities of the particles. This is :math:`a \frac{dx}{dt}` where :math:`x` is the co-moving position of the particles.

.. dropdown:: Black hole particle properties

   .. list-table::
      :header-rows: 1

      * - Name
        - Description
      * - .. dropdown:: ``accretion_rates``

             * **HDF5 name:** ``AccretionRates``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`10^{10}\ \frac{\rm{M}_\odot \cdot \rm{km}}{\rm{Mpc} \cdot \rm{s}}`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Physical instantaneous accretion rates of the particles
      * - .. dropdown:: ``coordinates``

             * **HDF5 name:** ``Coordinates``
             * **Shape:** 3
             * **Datatype:** float64
             * **Units:** :math:`a \cdot \rm{Mpc}`
             * **Compression:** 1 pc accurate
        - Co-moving position of the particles
      * - .. dropdown:: ``last_major_merger_scale_factors``

             * **HDF5 name:** ``LastMajorMergerScaleFactors``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** dimensionless
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
        - Scale-factors at which the black holes last had a major merger.
      * - .. dropdown:: ``last_minor_merger_scale_factors``

             * **HDF5 name:** ``LastMinorMergerScaleFactors``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** dimensionless
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.3669{\rm{}e}10`
        - Scale-factors at which the black holes last had a minor merger.
      * - .. dropdown:: ``particle_ids``

             * **HDF5 name:** ``ParticleIDs``
             * **Shape:** 1
             * **Datatype:** uint64
             * **Units:** dimensionless
             * **Compression:** Store less bits
        - Unique ID of the particles
      * - .. dropdown:: ``subgrid_masses``

             * **HDF5 name:** ``SubgridMasses``
             * **Shape:** 1
             * **Datatype:** float32
             * **Units:** :math:`10^{10}\ \rm{M}_\odot`
             * **Compression:** :math:`1.36693{\rm{}e}10 \rightarrow{} 1.367{\rm{}e}10`
        - Subgrid masses of the particles
      * - .. dropdown:: ``velocities``

             * **HDF5 name:** ``Velocities``
             * **Shape:** 3
             * **Datatype:** float32
             * **Units:** :math:`\rm{km} / \rm{s}`
             * **Compression:** 0.1 km/s accurate
        - Peculiar velocities of the particles. This is :math:`a \frac{dx}{dt}` where :math:`x` is the co-moving position of the particles.

HBT catalogues are available, but these came from an old version
of HBT (:ref:`see this issue<issues_hbt_high_cadence>`).
No SOAP catalogues are available.
