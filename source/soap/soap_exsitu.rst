:orphan:

.. _soap_exsitu:

Computing ex-situ fractions
===========================

The ``BirthHaloCatalogueIndex`` files described in :doc:`the additional SOAP catalogues <soap_additional>`
are only provided for the :math:`z=0` snapshot.
However, the values for a star particle are fixed once it forms,
and star particles are never removed from the simulation.
This means the values for any earlier snapshot can be obtained by reordering the :math:`z=0` files
to match the star particles present in that snapshot,
without having to reprocess all the earlier snapshots.

This page describes how to do this, and how to then run a minimal version of
`SOAP <https://github.com/SWIFTSIM/SOAP>`__ to compute the ``ExSituFraction``
of each subhalo at the snapshot you are interested in.

Setup
-----

Follow :doc:`the SOAP instructions <../tools/soap>` to clone the repository and
install SOAP by running ``./scripts/cosma_python_env.sh``.
Then install ``swiftsimio`` into the same environment, as it is used to select subhalos:

.. code-block:: bash

   cd SOAP
   source openmpi-5.0.3-hdf5-1.12.3-env/bin/activate
   pip install swiftsimio

Selecting subhalos (optional)
-----------------------------

By default SOAP will compute the ex-situ fraction for all subhalos.
If you are only interested in a subset you can pass SOAP a list of subhalos to process,
which reduces the runtime.
The following script uses the existing SOAP catalogue to select all subhalos with
a stellar mass (within a 50kpc exclusive sphere) above :math:`10^9 \, M_\odot`,
and writes their ``HaloCatalogueIndex`` to a text file.
This is a light task, so it can be run on the login node (with the environment above activated).

.. dropdown:: Click to view ``select_halos.py``

   .. code-block:: python

      import numpy as np
      import swiftsimio as sw

      simulation_dir = "/cosma8/data/dp004/colibre/Runs/L0025N0188/Thermal"
      snap_nr = 92  # z=1
      output_filename = f"halo_indices_{snap_nr:04d}.txt"

      soap = sw.load(f"{simulation_dir}/SOAP-HBT/halo_properties_{snap_nr:04d}.hdf5")
      stellar_mass = soap.exclusive_sphere_50kpc.stellar_mass.to_physical_value("Msun")
      halo_index = soap.input_halos.halo_catalogue_index.to_physical_value()

      mask = stellar_mass > 1e9
      print(f"Selected {np.sum(mask)} subhalos")
      np.savetxt(output_filename, halo_index[mask], fmt="%d")

Parameter file
--------------

The following parameter file configures SOAP to only compute the ``ExSituFraction``
for the bound subhalo and for a 50kpc exclusive sphere.
The ``ExtraInput`` section tells SOAP to load the reordered ``BirthHaloCatalogueIndex`` files.
You will need to set ``output_dir`` and ``scratch_dir``.
``output_dir`` must match the value used in the job script below.

.. dropdown:: Click to view ``exsitu_params.yml``

   .. code-block:: yaml

      # Values in this section are substituted into the other sections
      Parameters:
        sim_dir: /cosma8/data/dp004/colibre/Runs
        output_dir: /cosma8/data/do019/USER/exsitu
        scratch_dir: /cosma8/data/do019/USER/exsitu

      # Location of the Swift snapshots:
      Snapshots:
        # Use {snap_nr:04d} for the snapshot number and {file_nr} for the file number.
        filename: "{sim_dir}/{sim_name}/snapshots/colibre_{snap_nr:04d}/colibre_{snap_nr:04d}.{file_nr}.hdf5"

      # Which halo finder we're using, and base name for halo finder output files
      HaloFinder:
        type: HBTplus
        filename: "{sim_dir}/{sim_name}/HBT-HERONS/sorted_catalogues/OrderedSubSnap_{snap_nr:03d}.hdf5"

      # Existing group membership files
      GroupMembership:
        filename: "{sim_dir}/{sim_name}/SOAP-HBT/membership_{snap_nr:04d}/membership_{snap_nr:04d}.{file_nr}.hdf5"

      # The reordered BirthHaloCatalogueIndex files
      ExtraInput:
        birth_filename: "{output_dir}/{sim_name}/birth_{snap_nr:04d}/birth_{snap_nr:04d}.{file_nr}.hdf5"

      HaloProperties:
        # Where to write the halo properties file
        filename: "{output_dir}/{sim_name}/halo_properties_{snap_nr:04d}.hdf5"
        # Where to write temporary chunk output
        chunk_dir: "{scratch_dir}/{sim_name}/SOAP-tmp/"

      SubhaloProperties:
        properties:
          ExSituFraction: true
          NumberOfBlackHoleParticles: true
          NumberOfDarkMatterParticles: true
          NumberOfGasParticles: true
          NumberOfStarParticles: true

      ApertureProperties:
        properties:
          ExSituFraction: true
        variations:
          exclusive_50_kpc:
            inclusive: false
            radius_in_kpc: 50.0

      aliases:
        PartType0/LastSNIIKineticFeedbackDensities: PartType0/DensitiesAtLastSupernovaEvent
        PartType0/LastSNIIThermalFeedbackDensities: PartType0/DensitiesAtLastSupernovaEvent
        snipshot:
          PartType0/SpeciesFractions: PartType0/ReducedSpeciesFractions
          PartType0/ElementMassFractions: PartType0/ReducedElementMassFractions
          PartType0/LastSNIIKineticFeedbackDensities: PartType0/DensitiesAtLastSupernovaEvent
          PartType0/LastSNIIThermalFeedbackDensities: PartType0/DensitiesAtLastSupernovaEvent
      filters:
        general:
          limit: 100
          properties:
            - BoundSubhalo/NumberOfGasParticles
            - BoundSubhalo/NumberOfDarkMatterParticles
            - BoundSubhalo/NumberOfStarParticles
            - BoundSubhalo/NumberOfBlackHoleParticles
          combine_properties: sum
      defined_constants:
        O_H_sun: 4.9e-4
        Fe_H_sun: 3.16e-5
        N_O_sun: 0.138
        C_O_sun: 0.549
        Mg_H_sun: 3.98e-5
      calculations:
        calculate_missing_properties: false
        strict_halo_copy: false
        recently_heated_gas_filter:
          delta_time_myr: 15
          use_AGN_delta_T: false
        cold_dense_gas_filter:
          maximum_temperature_K: 3.16e4
          minimum_hydrogen_number_density_cm3: 0.1

Job script
----------

The following script carries out two steps:

1. Reorder the :math:`z=0` ``BirthHaloCatalogueIndex`` files to match the star particles
   at the snapshot of interest. The reordered files are written to your output directory.
2. Run SOAP to compute the ex-situ fractions.

Set the values at the top of the script, then submit it from the SOAP directory
using ``sbatch compute_exsitu.sh``.
If you did not select a subset of subhalos, remove the ``--halo-indices-file`` argument.
The default resources are suitable for the smaller boxes.
The larger boxes will require more memory and cores.

.. dropdown:: Click to view ``compute_exsitu.sh``

   .. code-block:: bash

      #!/bin/bash -l
      #
      #SBATCH --ntasks=8
      #SBATCH --cpus-per-task=1
      #SBATCH --mem=50GB
      #SBATCH -o ./compute_exsitu_%j.out
      #SBATCH -J compute_exsitu
      #SBATCH -p cosma-analyse
      #SBATCH -A do019
      #SBATCH -t 01:00:00
      #

      set -e

      # Simulation and snapshot to process
      sim="L0025N0188/Thermal"
      snap_nr=92  # z=1
      # Must match output_dir in the parameter file
      output_dir="/cosma8/data/do019/USER/exsitu"
      # Parameter file and (optional) list of subhalos to process
      param_file="exsitu_params.yml"
      halo_indices_file="halo_indices_$(printf '%04d' ${snap_nr}).txt"

      # Load the modules and the SOAP environment
      module purge
      module load python/3.12.4 gnu_comp/14.1.0 openmpi/5.0.3 parallel_hdf5/1.12.3
      source openmpi-5.0.3-hdf5-1.12.3-env/bin/activate

      sim_dir="/cosma8/data/dp004/colibre/Runs"
      birth_dir="/cosma8/data/dp004/dc-mcgi1/COLIBRE/BirthHaloCatalogueIndex"

      # Step 1: Reorder the z=0 BirthHaloCatalogueIndex files
      mpirun -- python misc/resort_BirthHaloCatalogueIndex.py \
        --snap-basename "${sim_dir}/${sim}/snapshots/colibre_{snap_nr:04d}/colibre_{snap_nr:04d}" \
        --input-basename "${birth_dir}/${sim}/SOAP-ExSitu/birth_{snap_nr:04d}/birth_{snap_nr:04d}" \
        --output-basename "${output_dir}/${sim}/birth_{snap_nr:04d}/birth_{snap_nr:04d}" \
        --input-snap-nr 127 \
        --output-snap-nr ${snap_nr}

      # Step 2: Run SOAP
      mpirun -- python SOAP/compute_halo_properties.py \
        "${param_file}" \
        --sim-name "${sim}" \
        --snap-nr ${snap_nr} \
        --chunks 1 \
        --halo-indices-file "${halo_indices_file}"

      echo "Job complete!"

Using the output
----------------

The output catalogue only contains the subhalos that were processed.
It can be matched to the full SOAP catalogue using ``HaloCatalogueIndex``.

.. code-block:: python

   import numpy as np
   import swiftsimio as sw

   simulation_dir = "/cosma8/data/dp004/colibre/Runs/L0025N0188/Thermal"
   output_dir = "/cosma8/data/do019/USER/exsitu/L0025N0188/Thermal"
   snap_nr = 92

   soap = sw.load(f"{simulation_dir}/SOAP-HBT/halo_properties_{snap_nr:04d}.hdf5")
   exsitu = sw.load(f"{output_dir}/halo_properties_{snap_nr:04d}.hdf5")

   # Find the position of each processed subhalo in the full catalogue
   soap_index = soap.input_halos.halo_catalogue_index.to_physical_value()
   exsitu_index = exsitu.input_halos.halo_catalogue_index.to_physical_value()
   order = np.argsort(soap_index)
   idx = order[np.searchsorted(soap_index, exsitu_index, sorter=order)]
   assert np.all(soap_index[idx] == exsitu_index)

   stellar_mass = soap.exclusive_sphere_50kpc.stellar_mass.to_physical_value("Msun")[idx]
   exsitu_fraction = exsitu.exclusive_sphere_50kpc.ex_situ_fraction.to_physical_value()
