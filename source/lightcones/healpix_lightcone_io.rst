Reading the maps with lightcone_io
==================================

The `lightcone_io <https://lightconeio.readthedocs.io/en/stable/>`__
python module can be used to read FLAMINGO HEALPix maps, either by
reading downloaded HDF5 files directly or by accessing maps stored on
`Cosma <https://cosma.readthedocs.io/en/latest/>`__ using the
`hdfstream <https://hdfstream-python.readthedocs.io/en/latest>`__
service. The latter method might be better if you're only interested
in certain quantities or regions on the sky.

Installation
------------

The ``lightcone_io`` module can be installed as follows::

  pip install lightcone_io

For remote access to snapshots we also need the hdfstream module::

  pip install hdfstream

Opening a set of HEALPix maps
-----------------------------

The examples below show how to access the down-sampled maps for
observer 0 in the fiducial ``L1_m9`` simulation.

.. tab-set::

   .. tab-item:: Opening remote files

      .. code-block:: python

         # Connect to the hdfstream service and open the root directory
         import hdfstream
         root = hdfstream.open("cosma", "/", user="my_username") # TODO: update when we remove access restrictions

         # Location of the lightcone output relative to the directory we opened
         basedir="FLAMINGO/L1_m9/L1_m9/healpix_maps/nside_4096"

         # Specify which observer's lightcone to read
         basename="lightcone0"

         # Open the set of HEALPix maps on the server
         import lightcone_io as lc
         shell = lc.ShellArray(basedir, basename, remote_dir=root)

   .. tab-item:: Opening local files

      .. code-block:: python

         # Location of the lightcone output we downloaded
         basedir="./FLAMINGO/L1_m9/L1_m9/healpix_maps/nside_4096/"

         # Specify which observer's lightcone to read
         basename="lightcone0"

         # Open the set of HEALPix maps
         import lightcone_io as lc
         shell = lc.ShellArray(basedir, basename)

Reading map data
----------------

For each observer we have a number of :doc:`concentric shells
<healpix_shell_redshifts>`, and for each shell we have maps of various
:doc:`physical quantities <healpix_map_descriptions>`. The pixel data
for a particular map can be accessed by specifying a shell index and
the name of the map::

  # Index of the shell we're interested in
  shell_nr = 0

  # Name of the quantity we want to read
  map_name = "TotalMass"

  # Read the data
  map_data = shell[shell_nr][map_name][...]

Here, indexing an individual map with the ellipsis (``[...]``)
triggers the full map to be read in or downloaded. The result is a
`unyt <https://unyt.readthedocs.io/en/stable/>`__ array containing the
pixel values with unit information. See the `lightcone_io
documentation
<https://lightconeio.readthedocs.io/en/stable/healpix_maps.html>`__
for more details.
