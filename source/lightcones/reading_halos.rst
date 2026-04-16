Reading lightcone halo data
===========================

The `lightcone_io <https://lightconeio.readthedocs.io/en/stable/>`__
python module can be used to read FLAMINGO lightcone halo outputs,
either by reading downloaded HDF5 files directly or by accessing files
stored on `Cosma <https://cosma.readthedocs.io/en/latest/>`__ using
the `hdfstream <https://hdfstream-python.readthedocs.io/en/latest>`__
service.

Installation
------------

The ``lightcone_io`` module can be installed as follows::

  pip install lightcone_io

For remote access to snapshots we also need the hdfstream module::

  pip install hdfstream

Reading a lightcone halo catalogue file
---------------------------------------

TODO: test this and update paths in the SOAP example below

Each file contains all of the halos in a spherical shell corresponding
to a single simulation snapshot. The example below reads the halos
drawn from snapshot 70 of the L1_m10 simulation for lightcone observer
0:

.. tab-set::

   .. tab-item:: Opening remote files

      .. code-block:: python

         # Connect to the hdfstream service and open the root directory
         import hdfstream
         root_dir = hdfstream.open("cosma", "/", user="my_username") # TODO: update when we remove access restrictions

         # Name of the lightcone halo catalogue file to read
         filename = "FLAMINGO/L1_m10/L1_m10/halo_lightcones/lightcone0/lightcone_halos_0070.hdf5"

         # Open the lightcone particle output
         import lightcone_io as lc
         halos = lc.HaloLightconeFile(filename, remote_dir=root)

   .. tab-item:: Opening local files

      .. code-block:: python

         # Name of the lightcone halo catalogue file to read
         filename = "FLAMINGO/L1_m10/L1_m10/halo_lightcones/lightcone0/lightcone_halos_0070.hdf5"

         # Open the lightcone particle output
         import lightcone_io as lc
         halos = lc.HaloLightconeFile(filename)

Accessing halo lightcone data
-----------------------------

We can get a list of the available halo properties with::

  print(halos.properties)

To read positions and bound masses for all halos in the catalogue, for
example, we can do this::

  # List of halo properties to read
  properties = ("Lightcone/HaloCentre", "BoundSubhalo/TotalMass")

  # Read the data
  halo_props = halos.read_halos(properties)

This returns a dict of unyt arrays, which are the halo properties with
unit information attached. Since the halos are sorted by HEALPix
pixel, it's possible to extract halos close to a specified position on
the sky::

  # Line of sight vector specifying a point on the sky
  vector = (1.0, 0.0, 0.0)

  # Angular radius around this point (in radians)
  import numpy as np
  radius = np.radians(10.0)

  # List of halo properties to read
  properties = ("Lightcone/HaloCentre", "BoundSubhalo/TotalMass")

  # Read the data
  halo_props = halos.read_halos_in_radius(vector, radius, properties)

Again, this returns a dict of unyt arrays with the halo properties,
but only halos in the specified patch of sky are included.

Reading SOAP properties for lightcone halos
-------------------------------------------

Not all SOAP halo properties are copied into the lightcone halo
catalogue because it would make the files unreasonably large. However,
for each halo in the halo lightcone we store the index in the
corresponding SOAP output as ``InputHalos/SOAPIndex``. It is therefore
possible to look up a wide range of SOAP properties for halos in the
lightcone catalogue.

The ``lightcone_io.HaloLightconeFile`` class has an optional parameter
``soap_filename`` which can be used to do this. For example::

      import lightcone_io as lc
      halos = lc.HaloLightconeFile(filename="hbt_lightcone_halos/lightcone0/lightcone_halos_0070.hdf5",
                                   soap_filename="SOAP-HBT/halo_properties_0070.hdf5")

This opens one of the halo lightcone files AND the corresponding SOAP
output which the halos were taken from. We can then select a patch of
sky to read in, as above::

      # Line of sight vector specifying a point on the sky
      vector = (1.0, 0.0, 0.0)

      # Angular radius around this point (in radians)
      import numpy as np
      radius = np.radians(10.0)

and read in some halo properties::

    # List of halo properties to read
    properties = ("Lightcone/HaloCentre", "SO/200_crit/TotalMass")

    # Read the data
    halo_props = halos.read_halos(properties)

As before, this returns a dictionary of unyt arrays with the halo
properties but any properties which do not exist in the halo lightcone
file will be read in from SOAP instead. In this case the quantity
``SO/200_crit/TotalMass`` is read from the SOAP file and reordered to
match the lightcone halo catalogue.
