Running on COSMA
================

.. important::
   Basic analysis using a single CPU is permitted on the login node. However, you **must not** use the login node for heavy computation or memory-intensive processing. More significant analysis tasks should always be handled by submitting a job to the queue.

`The COSMA website <https://cosma.readthedocs.io/en/latest/#>`__
contains general information about using the COSMA HPC system.

Jupyter Notebooks
-----------------

Setting up the environment
~~~~~~~~~~~~~~~~~~~~~~~~~~

To run notebooks on COSMA, you must first set up your environment. 
You must logged into cosma8b, as this node hosts the `Jupyter Hub instance <https://cosma.readthedocs.io/en/latest/jupyter.html>`__.
Run the following commands to log in to the node, clone the 
`introduction notebook <https://github.com/robjmcgibbon/COLIBRE_Introduction/tree/main>`__, and execute the setup script:

.. code-block:: bash

   ssh USER@login8b.cosma.dur.ac.uk
   git clone https://github.com/robjmcgibbon/COLIBRE_Introduction.git
   cd COLIBRE_Introduction
   ./cosma_env.sh

.. note::
   You will need to replace ``USER`` with your actual COSMA username.

This process creates a virtual environment containing all required Python packages and registers it with the Jupyter Hub. Once the environment is prepared, log out of COSMA.


Connecting to Jupyter Hub
~~~~~~~~~~~~~~~~~~~~~~~~~

To access the interface, you must reconnect using SSH port forwarding from a terminal on your own computer:

.. code-block:: bash

   ssh -N -L 8443:login8b.cosma.dur.ac.uk:443 USER@login8b.cosma.dur.ac.uk

.. note::
   This command will not produce any output, but you must leave it running for as long as you want to use the Jupyter Hub.

Then do the following:

1. Open https://localhost:8443 in your web browser.
2. Log in with your COSMA username and password.
3. Navigate to the ``COLIBRE_Introduction`` directory and open the notebook.
4. Switch the kernel to ``colibre_workshop`` by clicking the kernel name in the top right and selecting it from the list.

Analysis jobs
-------------

The following python script generates a plot comparing :math:`M_{200c}` to :math:`M_{*}`.
This specific script is a very small job, so there would be no problem running it directly on the login node. We are just using it here as a simple example of how to set up a batch job.

.. dropdown:: Click to view ``plot_stellar_mass.py``

   .. code-block:: python

      import matplotlib.pyplot as plt
      import swiftsimio as sw

      simulation_dir = "/cosma8/data/dp004/colibre/Runs/L0050N0376/Thermal"
      snap_nr = 127   # z=0
      soap_filename = f'{simulation_dir}/SOAP-HBT/halo_properties_{snap_nr:04}.hdf5'
      soap = sw.load(soap_filename)

      stellar_mass = soap.exclusive_sphere_50kpc.stellar_mass.to('Msun')
      total_mass = soap.spherical_overdensity_200_crit.total_mass.to('Msun')
      mask = (stellar_mass != 0) & (total_mass != 0)

      fig, ax = plt.subplots(1)
      ax.loglog(total_mass[mask], stellar_mass[mask], '.')
      ax.set_xlabel(r'$M_{200c}$ [$M_\odot$]')
      ax.set_ylabel(r'$M_{*}$ [$M_\odot$]')
      plt.savefig('smhm.png')
      plt.close()


The following shell script handles the submission to the queue using SLURM.

.. dropdown:: Click to view ``plot_stellar_mass.sh``

   .. code-block:: bash

      #!/bin/bash -l
      #
      #SBATCH --ntasks=1
      #SBATCH --cpus-per-task=1
      #SBATCH --mem=10GB
      #SBATCH -o ./plot_stellar_mass_%j.out
      #SBATCH -J plot_stellar_mass
      #SBATCH -p cosma-analyse
      #SBATCH -A do019
      #SBATCH -t 00:10:00
      #

      # Get venv location
      HOME=`realpath ~`
      APPS=`echo ${HOME} | sed 's/\/cosma\/home/\/cosma\/apps/g'`
      VENV=${APPS}/venvs/colibre

      # Activate the venv
      source "${VENV}"/bin/activate

      # Run the script
      python plot_stellar_mass.py

The job should be submitted using the following command:

.. code-block:: bash

   sbatch plot_stellar_mass.sh

Data storage
------------

You are provided with 10TB of storage at ``/cosma8/data/do019/<your_username>``,
please clean up regularly and do not store data for longer than is necessary.
You should not store data within your home directory.

