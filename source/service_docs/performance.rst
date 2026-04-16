Performance tips
================

Reading large sets of files
---------------------------

Opening files stored on a parallel file system is somewhat expensive. This
service caches HDF5 file and dataset objects between requests so if you
need to read datasets from many files then its best to read everything you
need from each file before moving on to the next so that each file only
needs to be opened once.

The same applies when reading multiple dataset slices: it's best to read
everything you need from one dataset before moving on to the next.

Reading multiple slices
-----------------------

If you need to read multiple slices from one dataset, it is much
more efficient to download them all in a single request than to
make multiple requests in a loop. See
the :doc:`python module documentation <python_module>` and
:doc:`API description <api_description>` for details.

Parallel requests for HDF5 data
-------------------------------

The service is capable of handling multiple requests simultaneously using
a pool of reader processes. The number of processes is limited, so if you
submit too many simultaneous requests then some will block until a process
is available to handle them.

It's probably best to limit yourself to no more than 2-4 simultaneous
requests in order to avoid slowing down access for other users. If you're
limited by network bandwidth there may not be any advantage in running
parallel requests anyway.
