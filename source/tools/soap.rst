SOAP
====

If you need to compute properties for all subhalos in a simulation,
it can be useful to use `SOAP <https://github.com/SWIFTSIM/SOAP>`__.
The standard SOAP catalogues include a large number of precomputed properties,
but SOAP can also be configured to compute only a selected subset, which significantly reduces runtime.

To get started, clone the repository and run ``./scripts/cosma_python_env.sh`` to install an editable version of SOAP.
You can then execute ``./tests/COLIBRE/run_L0025N0188_Thermal.sh`` to process a small set of halos as a test case.

Further details on running SOAP are available `in the repository documentation <https://github.com/SWIFTSIM/SOAP#computing-halo-properties>`__.
The repository also includes `guidance on adding new properties <https://github.com/SWIFTSIM/SOAP?tab=readme-ov-file#modifying-the-code>`__.

Running SOAP
------------

Below is a minimal parameter file required to run SOAP.
To run it you will need to change ``output_dir`` and ``scratch_dir`` to point to your own directories.
You can extend it with additional apertures or properties as needed by comparing it
with `the full COLIBRE parameter file <https://github.com/SWIFTSIM/SOAP/blob/master/parameter_files/COLIBRE_THERMAL.yml>`__.

.. code-block:: yaml

   # Values in this section are substituted into the other sections
   Parameters:
     sim_dir: /cosma8/data/dp004/colibre/Runs
     output_dir: /snap8/scratch/dp004/dc-mcgi1/soap_example
     scratch_dir: /snap8/scratch/dp004/dc-mcgi1/soap_example

   # Location of the Swift snapshots:
   Snapshots:
     # Use {snap_nr:04d} for the snapshot number and {file_nr} for the file number.
     filename: "{sim_dir}/{sim_name}/snapshots/colibre_{snap_nr:04d}/colibre_{snap_nr:04d}.{file_nr}.hdf5"

   # Which halo finder we're using, and base name for halo finder output files
   HaloFinder:
     type: HBTplus
     filename: "{sim_dir}/{sim_name}/HBT-HERONS/sorted_catalogues/OrderedSubSnap_{snap_nr:03d}.hdf5"

   GroupMembership:
     # Location of the group membership files. These already exist for the
     # COLIBRE runs, so they are reused rather than recomputed
     filename: "{sim_dir}/{sim_name}/SOAP-HBT/membership_{snap_nr:04d}/membership_{snap_nr:04d}.{file_nr}.hdf5"
     # Virtual snapshot linking the snapshot and membership files
     virtual_snapshot_filename: "{sim_dir}/{sim_name}/SOAP-HBT/colibre_with_SOAP_membership_{snap_nr:04d}.hdf5"

   HaloProperties:
     # Where to write the halo properties file
     filename: "{output_dir}/{sim_name}/SOAP/halo_properties_{snap_nr:04d}.hdf5"
     # Where to write temporary chunk output
     chunk_dir: "{scratch_dir}/{sim_name}/SOAP-tmp/"

   SubhaloProperties:
     properties:
       EncloseRadius: true
       NumberOfBlackHoleParticles: true
       NumberOfDarkMatterParticles: true
       NumberOfGasParticles: true
       NumberOfStarParticles: true
       TotalMass: true

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

All the steps of SOAP can then be run with a single command, from the SOAP source directory.
For example, to process snapshot 127 of ``L0025N0188/Thermal`` on 4 cores:

.. code-block:: bash

   module purge
   module load python/3.12.4 gnu_comp/14.1.0 openmpi/5.0.3 parallel_hdf5/1.12.3
   source openmpi-5.0.3-hdf5-1.12.3-env/bin/activate
   mpirun -np 4 python -u SOAP/run_soap.py \
       --sim-name=L0025N0188/Thermal --snap-nr=127 --chunks=1 \
       parameters.yml

This computes the halo properties and compresses the output catalogue,
which is written to the location given by ``HaloProperties/filename``, and should takes about 2 minutes.
Don't run with many more than 4 cores on the cosma login nodes, since they are shared with other users.
For larger simulations you may need to run on more cores (within a batch job) and increase ``--chunks``.
This splits the volume into chunks which are processed one at a time, reducing the memory required.

Processing a selection of subhalos
----------------------------------

If you only need properties for some of the subhalos, SOAP can be restricted to process only those.
Passing ``--centrals-only`` skips all satellite subhalos.
Individual subhalos can be selected by listing their indices in a text file, one index per line,
which is passed with ``--halo-indices-file``.
The output catalogue will then only contain the selected subhalos.

The index of each subhalo is stored as ``InputHalos/HaloCatalogueIndex`` in the existing SOAP catalogues.
For example, to select all central subhalos with :math:`M_{200c} > 10^{12} M_\odot`:

.. code-block:: python

   import numpy as np
   import swiftsimio as sw

   cat = sw.load("/cosma8/data/dp004/colibre/Runs/L0025N0188/Thermal/SOAP-HBT/halo_properties_0127.hdf5")
   m200 = cat.spherical_overdensity_200_crit.total_mass.to_physical_value("Msun")
   is_central = cat.input_halos.is_central.to_physical_value("dimensionless")
   index = cat.input_halos.halo_catalogue_index.to_physical_value("dimensionless")

   selected = (m200 > 1e12) & (is_central == 1)
   np.savetxt("halo_indices_0127.txt", index[selected], fmt="%d")

SOAP can then be run on just these subhalos:

.. code-block:: bash

   mpirun -np 4 python -u SOAP/run_soap.py \
       --sim-name=L0025N0188/Thermal --snap-nr=127 --chunks=1 \
       --halo-indices-file=halo_indices_0127.txt \
       parameters.yml

The snapshot number is substituted into the filename passed to ``--halo-indices-file``,
so when processing several snapshots you can pass e.g. ``halo_indices_{snap_nr:04d}.txt``.

