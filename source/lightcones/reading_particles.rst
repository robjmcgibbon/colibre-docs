Reading lightcone particle data
===============================

The `lightcone_io <https://lightconeio.readthedocs.io/en/stable/>`__
python module can be used to read FLAMINGO lightcone particle outputs,
either by reading downloaded HDF5 files directly or by accessing files
stored on `Cosma <https://cosma.readthedocs.io/en/latest/>`__ using
the `hdfstream <https://hdfstream-python.readthedocs.io/en/latest>`__
service. The latter method might be better if you're only interested
in certain quantities or regions on the sky.

Installation
------------

The ``lightcone_io`` module can be installed as follows::

  pip install lightcone_io

For remote access to snapshots we also need the hdfstream module::

  pip install hdfstream

Opening the particle data for a lightcone observer
--------------------------------------------------

The examples below show how to open the lightcone particle data output
for observer 0 in the fiducial ``L1_m9`` simulation.

.. tab-set::

   .. tab-item:: Opening remote files

      .. code-block:: python

         # Connect to the hdfstream service and open the root directory
         import hdfstream
         root_dir = hdfstream.open("cosma", "/", user="my_username") # TODO: update when we remove access restrictions

         # Location of one of the lightcone particle files relative to the remote directory
         filename = "FLAMINGO/L1_m9/L1_m9/particle_lightcones/lightcone0_particles/lightcone0_0000.hdf5"

         # Open the lightcone particle output
         import lightcone_io as lc
         lightcone = lc.ParticleLightcone(filename, remote_dir=root_dir)

   .. tab-item:: Opening local files

      .. code-block:: python

         # Location of one of the lightcone particle files we downloaded
         filename = "./FLAMINGO/L1_m9/L1_m9/particle_lightcones/lightcone0_particles/lightcone0_0000.hdf5"

         # Open the lightcone particle output
         import lightcone_io as lc
         lightcone = lc.ParticleLightcone(filename)

Reading particle information
----------------------------

The commands above return a ``ParticleLightcone`` object which acts
like a dictionary where the particle types are the keys. E.g. to see
which particle types are available::

  print(list(lightcone))

You can use the properties attribute to see what quantities are
available for each particle type. E.g.::

  print(lightcone["Gas"].properties)

The particles in the files are sorted into redshift shells. Within a
shell they are sorted by HEALPix pixel index. If we specify the
redshift range we're interested in and a position on the sky, the
``lightcone_io`` module can locate and read (or download) the
corresponding particles::

  # Quantities we wish to read in
  property_names = ("Coordinates", "ParticleIDs")

  # Line of sight vector specifying the centre of the patch of sky to read in.
  # Here we're looking along the simulation x axis. Set vector=None and
  # radius=None to read the full sky.
  vector = (1., 0., 0.)

  # Angular radius of the patch to read in (5 degrees, here)
  import numpy as np
  radius = np.radians(5.)

  # Redshift range to read in, or None to read all redshifts.
  redshift_range = (0.0, 0.15)

  # Show how many particles will be read
  nr_particles = lightcone["Gas"].count_particles(vector, radius, redshift_range)
  print(f"There are {nr_particles} particles in the specified region")

  # Read or download the particles
  data = lightcone["Gas"].read(property_names, vector, radius, redshift_range)

The result is a dict of `unyt
<https://unyt.readthedocs.io/en/stable/>`__ arrays with the requested
data. In this example we have particle positions and IDs::

  particle_positions = data["Coordinates"]
  particle_ids       = data["ParticleIDs"]

We have read in all particles at redshift :math:`z < 0.15` in a cone
aligned with the x axis. We can illustrate this by plotting the
particles in a slice through the cone::

  import unyt
  in_slice = (particle_positions[:,2] > -1.0*unyt.Mpc) & (particle_positions[:,2] < 1.0*unyt.Mpc)
  plt.plot(particle_positions[in_slice,0], particle_positions[in_slice,1], "k,", alpha=0.1, rasterized=True)
  plt.xlabel("x [cMpc]")
  plt.ylabel("y [cMpc]")
  plt.show()

TODO: add image with result (when disk access is possible again...)
