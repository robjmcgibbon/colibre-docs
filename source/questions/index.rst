Common Questions
================

This page provides answers to common questions regarding the simulations
and the data products.
It will be updated to reflect new user inquiries and technical developments.

If you this page does not contain an answer to your question
(or if you have any suggestions for improvements to the documentation),
then please message us on slack!

.. contents::
   :local:
   :backlinks: none

Simulation
----------

.. _faq_bh_satellites:

Why are many satellite galaxies missing a black hole?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :ref:`issues_bh_satellites`.

Snapshots
---------

.. _faq_compression:

What are the compression filters associated with the datasets?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We apply lossy compression filters to the data in the snapshots and SOAP catalogues to reduce the disk footprint. For floating-point values, this involves reducing precision (effectively rounding the values) to save space.

A list of the various filters can be found in the `Swift documentation <https://swift.strw.leidenuniv.nl/docs/ParameterFiles/lossy_filters.html>`__. The specific filter used for each dataset is stored in its HDF5 attributes.

SOAP
----

.. _faq_backsplash:

How do I identify a backsplash galaxy?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Backsplash galaxies are galaxies which fell into a more massive halo,
temporarily becoming a satellite, but had enough energy to move back
outside of their host, and are therefore centrals once again.
The field ``soap.input_halos_hbtplus.snapshot_of_last_isolation`` records
the most recent snapshot at which an object was a central (see
:ref:`issues_overflow_snapshotindexoflastisolation`). It is most useful
for ruling objects *out*: since ``snapshot_of_last_isolation == -1`` means
the object has always been a central, such an object cannot be a
backsplash galaxy.

The converse is not true: ``snapshot_of_last_isolation != -1`` does not
guarantee that an object is a true backsplash galaxy. This is because it
cannot distinguish a genuine backsplash galaxy from a false positive
caused by the central/satellite label switching between two subhaloes of
comparable mass during a merger, which happens most often at early times
when both haloes are poorly resolved. To identify genuine backsplash
galaxies, therefore, start by selecting candidates with
``snapshot_of_last_isolation`` equal to the current snapshot, then trace
each one back through the earlier catalogues (see
:ref:`this example <hbt_evolution_example>`) to find the last snapshot at
which it was a satellite. This lets you identify the object's host at
that time, and hence obtain the host's :math:`R_{200c}`.

Whether an object is labelled a satellite depends on its
membership of a Friends-of-Friends group, not on a distance criterion
such as having crossed within :math:`R_{200c}` of the host. A galaxy can
therefore pass through the outskirts of a more massive halo without ever
being labelled a satellite. Conversely, FoF groups can extend well beyond
:math:`R_{200c}` (e.g. along filaments), and so an object can be labelled
a satellite without ever having entered :math:`R_{200c}` of its host.

