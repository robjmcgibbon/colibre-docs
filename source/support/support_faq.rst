Frequently Asked Questions
==========================

This page provides answers to common questions regarding the simulations and the data products.
It will be updated to reflect new user inquiries and technical developments.

.. contents::
   :local:
   :backlinks: none

Data
----

.. _faq_compression:

What are the compression filters associated with the datasets?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We apply lossy compression filters to the data in the snapshots and SOAP catalogues to reduce the disk footprint. For floating-point values, this involves reducing precision (effectively rounding the values) to save space.

A list of the various filters can be found in the `Swift documentation <https://swift.strw.leidenuniv.nl/docs/ParameterFiles/lossy_filters.html>`__. The specific filter used for each dataset is stored in its HDF5 attributes.

