Accessing data in python
========================

The hdfstream python module allows remote access to HDF5 datasets
using an interface similar to h5py. The module source code is hosted
`on github <https://github.com/jchelly/hdfstream-python>`__ and full
documentation is available on `Read the Docs
<https://hdfstream-python.readthedocs.io/en/stable/>`__. In case of
problems, please `post an issue
<https://github.com/jchelly/hdfstream-python/issues>`__.

The hdfstream module provides a generic solution for remote access to
HDF5 data. If you're working with :doc:`simulation snapshots
</snapshots/index>` you might prefer to use :doc:`swiftsimio
</snapshots/swiftsimio>`, which can use hdfstream to access snapshots
while providing a more friendly interface. Similarly, the lightcone_io
module can be used to access :doc:`lightcone outputs
</lightcones/index>`.

Installation
------------

The module can be installed using pip::

  pip install hdfstream

Connecting to the server
------------------------

You can connect to the service as follows::

    import hdfstream
    root_dir = hdfstream.open("cosma", "/", user="my_username") # TODO: update when we remove access restrictions

Here, the first parameter is the server name. This can be a full URL or an
alias recognised by the hdfstream module. The second parameter is the name of
the directory to open.

Directory objects
-----------------

The command above returns a RemoteDirectory object. This behaves like a
python dictionary where the keys are the names of files and subdirectories
within the directory. We can list the contents with::

    print(list(root_dir))

A file or subdirectory can be opened by subscripting the
RemoteDirectory. E.g. to open the directory containing the z=0
snapshot of the ``L1_m10/L1_m10_DMO`` simulation::

    # Open a subdirectory
    subdir = root_dir["FLAMINGO/L1_m10/L1_m10_DMO/snapshots/flamingo_0077"]

which returns another RemoteDirectory, or::

    # Open a HDF5 file
    snap_file = root_dir["FLAMINGO/L1_m10/L1_m10_DMO/snapshots/flamingo_0077/flamingo_0077.0.hdf5"]

which opens the specified file and returns a RemoteFile object.

Reading HDF5 groups and datasets
--------------------------------

Files are opened by subscripting the directory object with the path to the file::

    snap_file = root_dir["FLAMINGO/L1_m10/L1_m10_DMO/snapshots/flamingo_0077/flamingo_0077.0.hdf5"]

This returns a RemoteFile object which behaves like a h5py.File.
We can read a dataset with::

    # Read all dark matter particle positions in the file
    dm_pos = snap_file["PartType1/Coordinates"][...]

or if we only want to download part of the dataset::

    # Read the first 100 dark matter particle positions
    dm_pos = snap_file["PartType1/Coordinates"][:100,:]

HDF5 attributes can be accessed using the attrs field of group and dataset objects::

    print(snap_file["Header"].attrs)

And we can list the contents of a group::

    print(list(snap_file["PartType0"]))

Requesting multiple dataset slices
----------------------------------

When working with simulation data it can be useful to be able to
efficiently read multiple non-contiguous chunks of a dataset (e.g.
particles in some region of a SWIFT snapshot). Requesting each chunk
separately can be slow because a round trip to the server is required
for each one.

The python module provides a mechanism to fetch multiple slices with one
http request. Remote datasets have a request_slices() method which takes
a sequence of slice objects as input and returns a single array with the
slices concatenated along the first axis. Slice objects can be created
by indexing numpy's built in `np.s_` object. For example::

    slices = []
    slices.append(np.s_[10:20,:])
    slices.append(np.s_[50:60,:])
    data = dm_pos.request_slices(slices)

This would return the coordinates of particles 10 to 19 and 50 to 59 in a
single array of shape (20,3). There are some restrictions on the slices:

  * Slice starting indexes in the first dimension must be in ascending order
  * Slice indexes in dimensions other than the first must not differ between slices
  * Slices must not overlap
  * Slices can only concatenated along the first dimension

Limitations
-----------

Supported data types
^^^^^^^^^^^^^^^^^^^^

Not all HDF5 data types are supported. In particular, the service
cannot encode structs which contain variable length components.
Other variable length data types are supported but are encoded
as messagepack arrays, which will incur more overhead than the
binary objects used for fixed size types.

Large arrays of variable length types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Datasets containing variable length types are encoded as
messagepack array objects, which have a size limit of about 4
billion elements. Since the encoding scheme for variable length
types is not particularly efficent for huge numbers of small
elements, the service does not attempt to work around this
limitation.

None of the datasets currently available through the service
contain this type of data.

Large arrays of fixed length types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The service is capable of encoding arbitrarily large datasets
containing fixed length types such as ints or floats. In this
case the body of the dataset is encoded as an array of
messagepack binary objects of up to 4GB each. The python module
includes a memory efficient streaming decoder for this type of
dataset.
