Additional SOAP catalogues
==========================

This page lists additional halo catalogues produced with SOAP. 
These products are intended to supplement analyses and have only been generated for a limited selection of snapshots and simulations.
If you require these catalogues for other runs, then please contact the team.

SubFind SOAP catalogues
-----------------------

To facilitate comparisons with previous work, we have run SubFind (the GADGET-4 public version) for several simulations. 
Note that due to fundamental differences in how halo finders operate, 
any discrepancies between HBT and SubFind catalogues should not be interpreted as an indication of "error" in the halo finding process.
Notes on these differences :ref:`can be found here <subfind_vs_hbt>`.

SubFind has been run for :math:`z=0` for the following simulations:

* L025m5
* L025m6, L100m6
* L025m7, L200m7

We have also produced SOAP catalogues using these SubFind catalogues as input.
The runs listed above include a ``SOAP-Subfind`` directory containing the :math:`z=0` catalogue. 
Additionally, the ``colibre_with_SOAP_membership_0127.hdf5`` file is provided, enabling the use of ``swiftgalaxy`` with these catalogues.

ExSitu fractions
----------------

The directory ``/cosma8/data/dp004/dc-mcgi1/COLIBRE/BirthHaloCatalogueIndex``
contains :math:`z=0` snapshots with extra datasets available for star particles:

* ``BirthHaloCatalogueIndex`` - The ``HaloCatalogueIndex`` of this star particle the snapshot it first appeared.
* ``PreBirthHaloCatalogueIndex`` - The ``HaloCatalogueIndex`` of the star's progenitor gas particle the snapshot before the star first appeared.
* ``FirstSnapshot`` - The snapshot index when this star first appeared.

By comparing the ``BirthHaloCatalogueIndex`` with the current ``HaloCatalogueIndex``, you can determine if a star formed in-situ or ex-situ.

The snapshots are named ``SOAP-ExSitu/birth_0127.hdf5`` and can be opened using ``swiftsimio``.
They contain all the original particle properties.
Each run also includes a SOAP catalogue with the ``ExSituFraction`` computed for each subhalo.

SOAP-EAGLE
----------

The directory ``/cosma8/data/dp004/dc-mcgi1/COLIBRE/soap_eagle`` contains SOAP catalogues generated using the original EAGLE snapshots.
These ensure that galaxy properties are computed using the same methodology as the COLIBRE SOAP catalogues,
enabling a direct comparisons between the two simulations.
We also provide versions of the EAGLE snapshots that can be read with ``swiftsimio``.

There are a number of differences compared with the COLBIRE SOAP catalogues.

* These catalogues depend on the original SubFind subhalo catalogues used for EAGLE (we cannot run HBT-HERONS since there are not enough snapshots).
* A large number of properties (e.g. all dust properties) which we have in the COLIBRE SOAPs are missing.
* There are several HI and H2 properties. These were calculated using the prescriptions in Blitz & Rosolowsky (2006) and Rahmati et al (2013).

SOAP-SmallSphericalOverdensity
------------------------------

For the :math:`z=0` snapshots of the L200m6 and L400m7 simulations (both Thermal and DMO),
we have run soap to compute properties for sphereical overdensity apertures of size :math:`R_{2500c}` & :math:`R_{1000c}`.
The files can be found at ``/cosma8/data/dp004/dc-mcgi1/COLIBRE/inner_spherical_overdensity``
