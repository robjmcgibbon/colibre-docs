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

* L025m5, L050m5 DMO
* L025m6, L100m6, L100m6 DMO
* L025m7, L200m7, L200m7 DMO

We have also produced SOAP catalogues using these SubFind catalogues as input.
The runs listed above include a ``SOAP-Subfind`` directory containing the
:math:`z=0` catalogue.
Additionally, the ``colibre_with_SOAP_membership_0127.hdf5`` file is provided,
enabling the use of ``swiftgalaxy`` with these catalogues.
The scripts used to run SubFind on COLIBRE
:download:`can be found here <subfind/colibre_subfind.zip>`.

ExSitu fractions
----------------

The directory ``/cosma8/data/dp004/dc-mcgi1/COLIBRE/BirthHaloCatalogueIndex``
contains :math:`z=0` snapshots with extra datasets available for star particles:

* ``BirthHaloCatalogueIndex`` - The ``HaloCatalogueIndex`` of this star particle the snapshot it first appeared.
* ``PreBirthHaloCatalogueIndex`` - The ``HaloCatalogueIndex`` of the star's progenitor gas particle the snapshot before the star first appeared. Particle splits are not accounted for, so this is -99 if the progenitor gas particle cannot be found.
* ``FirstSnapshot`` - The snapshot index when this star first appeared.

By comparing the ``BirthHaloCatalogueIndex`` with the current ``HaloCatalogueIndex``, you can determine if a star formed in-situ or ex-situ.

The snapshots are named ``SOAP-ExSitu/birth_0127.hdf5`` and can be opened using ``swiftsimio``.
They contain all the original particle properties.
Each run also includes a SOAP catalogue with the ``ExSituFraction`` computed for each subhalo.
The ex-situ fractions can be computed for other snapshots by following :ref:`these instructions <soap_exsitu>`.

SOAP-EAGLE
----------

The directory ``/cosma8/data/dp004/dc-mcgi1/COLIBRE/soap_eagle`` contains SOAP catalogues generated using the original EAGLE snapshots.
These ensure that galaxy properties are computed using the same methodology as the COLIBRE SOAP catalogues,
enabling a direct comparisons between the two simulations.
We also provide versions of the EAGLE snapshots that can be read with ``swiftsimio``.

There are a number of differences compared with the COLIBRE SOAP catalogues.

* These catalogues depend on the original SubFind subhalo catalogues used for EAGLE (we cannot run HBT-HERONS since there are not enough snapshots).
* A large number of properties (e.g. all dust properties) which we have in the COLIBRE SOAPs are missing.
* There are several HI and H2 properties. These were calculated using the prescriptions in Blitz & Rosolowsky (2006) and Rahmati et al (2013).

SOAP-SmallSphericalOverdensity
------------------------------

For the :math:`z=0` snapshots of the L200m6 and L400m7 simulations (both Thermal and DMO),
we have run soap to compute properties for spherical overdensity apertures of size :math:`R_{2500c}` & :math:`R_{1000c}`.
The files can be found at ``/cosma8/data/dp004/dc-mcgi1/COLIBRE/inner_spherical_overdensity``

Cosmic web classifications
--------------------------

The DisPerSE and T-web cosmic web finders have been run on COLIBRE.
If you are interested in using these classifications, please contact Jake Howard (Durham).

.. _soap_history:

SOAP-History
------------

We provide catalogues of properties which depend on the history of each subhalo.
These are computed by following the main progenitor branch of each subhalo through all previous SOAP catalogues,
where the main progenitor branch is identified using the HBT-HERONS ``TrackId``.
Note that some history properties are already available in the standard SOAP catalogues,
since they are output directly by HBT-HERONS
(e.g. ``InputHalos/HBTplus/LastMaxMass`` and ``InputHalos/HBTplus/SnapshotOfLastIsolation``).

Black hole maximum
^^^^^^^^^^^^^^^^^^

Black holes can be lost from subhaloes, e.g. satellites can lose their black holes
due to the way they are repositioned (see :ref:`issues_bh_satellites`),
and some centrals (e.g. backsplash galaxies) lose their black hole and then start regrowing a new one.
To help correct for this, the following properties are computed for ``BoundSubhalo`` and each ``ExclusiveSphere`` aperture:

* ``MainBranchMaximumMostMassiveBlackHoleMass`` - The maximum value of ``MostMassiveBlackHoleMass`` along the main progenitor branch (including the current snapshot).
* ``MainBranchMaximumMostMassiveBlackHoleID`` - The ID of the most massive black hole at the snapshot where the maximum was reached.
* ``MainBranchMaximumMostMassiveBlackHoleSnapshot`` - The snapshot number where the maximum was reached.

For subhaloes which have never contained a black hole the mass and ID are zero, and the snapshot is -1.

Stellar mass maximum
^^^^^^^^^^^^^^^^^^^^

The following properties are computed for ``BoundSubhalo`` and each ``ExclusiveSphere`` aperture:

* ``MainBranchMaximumStellarMass`` - The maximum value of ``StellarMass`` along the main progenitor branch (including the current snapshot).
* ``MainBranchMaximumStellarMassSnapshot`` - The snapshot number where the maximum was reached.

For subhaloes which have never contained any stars the mass is zero, and the snapshot is -1.

Formation snapshots
^^^^^^^^^^^^^^^^^^^

The formation snapshot is defined as the first snapshot of the final continuous stretch, ending at the current snapshot,
during which the mass along the main progenitor branch is at least half of its current value.
Snapshots in which the subhalo is not present in the SOAP catalogue are ignored.
The value is -1 if the current mass is zero.

* ``HalfMassFormationSnapshot`` - Computed using ``TotalMass``, for ``BoundSubhalo`` and each ``SO`` definition.
* ``HalfStellarMassFormationSnapshot`` - Computed using ``StellarMass``, for ``BoundSubhalo`` and each ``ExclusiveSphere`` aperture.

There are a number of caveats when using these properties:

* Satellites which have been stripped will have a current mass below their peak mass, and so will appear to have formed earlier.
* ``SO`` properties are only computed for central subhaloes, so the ``SO`` formation snapshot is -1 for satellites. Snapshots where the subhalo was a satellite are ignored when computing the ``SO`` formation snapshot.
* The ``SO`` masses include pseudo-evolution, so the ``SO`` formation snapshots are biased late.
* ``SO/BN98`` properties are only computed for subhaloes with at least 100 bound particles, so ``SO/BN98`` formation snapshots are biased late for subhaloes near this limit.

Catalogues
^^^^^^^^^^

The catalogues can be found in ``/cosma8/data/dp004/dc-mcgi1/COLIBRE/soap_history/<run>/SOAP-History``.
The catalogues are available for :math:`z=0,1,2,3`, and are named ``SOAP-History/history_XXXX.hdf5``.

They have the same ordering as the standard SOAP catalogues, and contain ``InputHalos/HBTplus/TrackId`` and ``InputHalos/HaloCatalogueIndex`` for matching.
They can be opened using ``swiftsimio``.

The script to generate these catalogues `can be found in the SOAP repository <https://github.com/SWIFTSIM/SOAP/blob/master/scripts/COLIBRE/compute_history_properties.sh>`__.

.. _soap_descendant_info:

SOAP-DescendantInfo
-------------------

In the current SOAP catalogues ``soap.descendant_index`` only follows the main progenitor branch
(see :ref:`issues_descendant_merger_info`), and both ``soap.progenitor_index`` and ``soap.descendant_index``
are incorrect for some subhalos in a small number of snapshots (see :ref:`issues_progenitor_descendant_index_order`).
We provide catalogues containing the corrected ``SOAP/ProgenitorIndex``, and the updated ``SOAP/DescendantIndex``
and ``SOAP/DescendantType``, for every snapshot.
``SOAP/ProgenitorIndex`` points to the subhalo with the same ``TrackId`` in the previous snapshot, and is -1 if
that subhalo is not resolved in the previous snapshot.
If a subhalo survives to the next snapshot then ``SOAP/DescendantIndex`` points to the subhalo with the same ``TrackId``.
If it disrupts or sinks then it points to the subhalo which it merged with, as identified by HBT-HERONS.
``SOAP/DescendantType`` indicates what happened to the subhalo between this snapshot and the next:

* 0 - The subhalo survives.
* 1 - The subhalo disrupts.
* 2 - The subhalo sinks.
* 3 - The subhalo disrupts or sinks, but there is no descendant since the majority of its most bound particles are not bound to any subhalo. ``SOAP/DescendantIndex`` is -1.
* -1 - This is the final snapshot. ``SOAP/DescendantIndex`` is -1.

A full description is given in :ref:`footnote 30 <footnote-30>` of the SOAP property table.

The catalogues can be found in ``/cosma8/data/dp004/dc-mcgi1/COLIBRE/SOAP-DescendantInfo``, and are named ``SOAP-DescendantInfo/descendant_info_XXXX.hdf5``.
They have the same ordering as the standard SOAP catalogues, and contain ``InputHalos/HBTplus/TrackId`` and ``InputHalos/HaloCatalogueIndex`` for matching.
They can be opened using ``swiftsimio``.
The script to generate these catalogues `can be found in the SOAP repository <https://github.com/SWIFTSIM/SOAP/blob/master/scripts/COLIBRE/compute_descendant_info.sh>`__.

An example of using ``SOAP/ProgenitorIndex`` to follow the main progenitor branch of a subhalo is given in
:doc:`../tools/examples/mass_evolution`, and an example of using ``SOAP/DescendantIndex`` to count the
mergers of a galaxy is given in :doc:`../tools/examples/merger_history`. An example of following
a population of satellites forward in time to determine their fate is given in :doc:`../tools/examples/descendant_fate`.

