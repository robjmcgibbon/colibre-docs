Web API description
===================

Full file and directory downloads
---------------------------------

Files and directories can be downloaded using a http get request of the form::

  /hdfstream/download/<virtual_path>

Here, if the virtual path refers to a directory the response will be a .tar
file containing the directory and its contents. If the path refers to a file
then the file will be downloaded.

Directory and file listings
---------------------------

A messagepack encoded directory listing can be obtained with a get request
to a URL of the form::

  /hdfstream/msgpack/<virtual_path>?max_depth=...

where the virtual path refers to a directory. The response will be a
:ref:`messagepack encoded directory <encoded_directory>`. The optional
integer max depth parameter determines the maximum recursion depth to
return subdirectories.

If the virtual path specifies a file then the response is a
:ref:`messagepack encoded file <encoded_file>`.

HDF5 groups and datasets
------------------------

HDF5 objects within a file can be requested with a get request to a URL of the form::

  /hdfstream/msgpack/<virtual_path>?object=<object_name>

Here the object name parameter specifies the name of the HDF5 object to download.
The response will be a :ref:`messagepack encoded group <encoded_group>` or
:ref:`dataset <encoded_dataset>`.

Requesting a dataset slice
--------------------------

If the requested object is a dataset then the parameter ``slice``
can be used to specify a range of elements to read in each dimension. The
syntax is similar to numpy slicing. The range of elements to read in each
dimension is specified as ``start:stop``, with commas separating dimensions.

Multiple slices can be requested by separating with semicolons. For example,
to read two slices from an Nx3 array the slice parameter would be:
``slice=0:10,0:3;30:40,0:3``. This would read elements 0-9 and 30-39 inclusive
in the first dimension and all three elements in the second dimension. This
type of request will return all slices concatenated along the first dimension
as a single ndarray.

Recursive group downloads
-------------------------

If the requested object is a group then the following optional parameters may be used:

  * ``max_depth``: the maximum recursion depth for downloading group members
  * ``max_data_size``: when downloading recursively, if the body of a dataset is larger than this size in bytes then only metadata will be downloaded.

These parameters are primarily used to implement lazy loading in the
python client module. In this case the response will be a
:ref:`messagepack encoded group <encoded_group>`.
