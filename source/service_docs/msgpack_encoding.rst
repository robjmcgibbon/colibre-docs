Messagepack encoding scheme
===========================

This page describes how the service encodes directory information and HDF5
groups, datasets and attributes as a messagepack data stream.
Objects returned by the msgpack endpoint are represented as messagepack maps
where the keys are messagepack strings.

For messagepack implementations in various languages see
`msgpack.org <https://msgpack.org/index.html>`__

.. _encoded_directory:

Directories
-----------

A directory is encoded as a messagepack map with the following entries:

  * ``directories``: a map where the keys are subdirectory names and the values are recursively encoded subdirectories
  * ``files``: a map where the keys are file names and the values contain file metadata (see below)
  * ``size``: the sum of the sizes of the files in this directory and all subdirectories, in bytes

Subdirectories may have a value of nil if they were not loaded because the
recursion limit was reached.

.. _encoded_file:

Files
-----

A file is encoded as a messagepack map with the following entries:

  * ``size``: size of the file in bytes
  * ``last_modified``: last modification time (in millisec)
  * ``media_type``: media type (aka MIME type) of the file

File types currently recognized by the server are listed below:

  * ``application/x-hdf5``: HDF5 files
  * ``application/yaml``: text files containing yaml data
  * ``text/plain``: other types of text files
  * ``application/octet-stream``: other binary data

.. _encoded_group:

HDF5 Groups
-----------

A HDF5 group is encoded as a messagepack map with the following entries:

  * ``hdf5_object``: the string "group", which identifies this object as a group
  * ``attributes``: a map where the keys are attribute names and the values are encoded ndarrays with the attribute values (see below)
  * ``members``: a map where the keys are the names of the objects in this group and the values are recursively encoded HDF5 objects

As with directories, members may have a value of nil if the recursion limit is reached.

.. _encoded_dataset:

HDF5 Datasets
-------------

A HDF5 dataset is encoded as a messagepack map with the following entries:

  * ``hdf5_object``: the string "dataset", which identifies this object as a dataset
  * ``attributes``: a map where the keys are attribute names and the values are encoded ndarrays with the attribute values (see below)
  * ``type``: a numpy style type string which describes the type of this dataset
  * ``shape``: an array of integers with the size of the dataset in each dimension
  * ``data``: a messagepack encoded ndarray with the dataset contents (see below)

The data entry may be nil if it would be larger than the maximum data size
in a recursive group request.

.. _encoded_ndarray:

Encoded arrays
--------------

When the contents of a dataset or attribute are requested the service
returns an encoded array. The encoding scheme depends on whether the
array is of a fixed size type (e.g. an array of ints or floats) or a
varying length type (e.g. an array of strings).

Scalar quantities are treated as zero dimensional arrays.

Arrays of fixed size data types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For fixed size data types the service uses an encoding scheme
inspired by, but not full compatible with,
the `msgpack-numpy <https://github.com/lebedov/msgpack-numpy>`__
python module. The contents of datasets and attributes of fixed
size types are represented as a messagepack map with the
following entries:

  * ``nd`` : true identifies this as an encoded ndarray
  * ``type``: a numpy style type string which describes the type of this array
  * ``kind``: an empty string for scalar elements, or "V" for array or compound types
  * ``shape``: an array of integers with the size of the array in each dimension
  * ``nbytes``: the total number of bytes in the body of the array
  * ``data``: a messagepack array of binary objects with the raw data

The encoding differs from msgpack-numpy in that the map keys are
strings instead of binary objects and the "data" field is an
array of binary objects to allow the encoding of arrays larger
than 4GB.

Arrays of variable length data types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To encode variable length types (such as HDF5 vlen strings) an alternate
encoding is used. Vlen data is represented as a map with the following entries:

  * ``vlen``: true identifies this as an encoded array of vlen data
  * ``shape``: an array of integers with the size of the array in each dimension
  * ``data``: a messagepack array with one entry for each element in the flattened ndarray

The elements in the data array are messagepack strings if this is an array of
vlen strings or encoded ndarrays if this is an array of some other variable
length type.
