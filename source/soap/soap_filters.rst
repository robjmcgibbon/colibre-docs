SOAP property filters
---------------------

For certain properties it only makes sense to compute them if a subhalo 
contains sufficient
particles. HBT-HERONS was run with a configuration that requires each
subhalo to have at least 20 particles. However, even for those
particle numbers, a lot of the properties computed by SOAP will be zero
(e.g. the gas mass within a 10 kpc aperture), or have values that are
outliers compared to the full halo population because of undersampling.
To save disk space and reduce the computation time, we filter these 
out by applying appropriate cuts. Filtering means setting the 
value of the property to
zero, and HDF5 file compression then very effectively reduces the data
storage required to store these properties, while the size of the arrays
that the end user sees remains unchanged.

Since different properties can have very different requirements,
filtering is done in categories, where each category corresponds to a
set of quantities that are filtered using the same criterion.

**Basic quantities (basic)** are never filtered out, and hence are calculated for all objects in the
input subhalo catalogue.

**General quantities (general)** use a filter based on the total number of particles bound to the
subhalo.

The criteria defining
the different categories are listed in the table below.

+---------+-----------------------------------------------------------------------+
| Name    | Criterion                                                             |
+=========+=======================================================================+
| basic   | all subhalos                                                          |
+---------+-----------------------------------------------------------------------+
| general | :math:`N_{\rm{}gas}+N_{\rm{}dm}+N_{\rm{}star}+N_{\rm{}BH} \geq{} 100` |
+---------+-----------------------------------------------------------------------+
