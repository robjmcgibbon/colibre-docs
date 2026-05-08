Known issues
============

This page tracks known technical issues related to the data products.
It will be updated as new issues are discovered.

.. contents::
   :local:
   :backlinks: none

Simulation
----------

.. _issues_bh_satellites:

Black holes in satellite galaxies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For computational efficiency reasons, black hole particles are only repositioned (i.e. moved by hand down the potential gradient to compensate for unresolved dynamical friction) onto gas particles. For gas-poor galaxies, such as low-mass satellites, this can have the consequence that black holes leave their host galaxy, either temporarily or permanently. Care should therefore be taken when studying black holes and/or AGN feedback in satellite galaxies.

.. _issues_agn_heating:

AGN heating
~~~~~~~~~~~

AGN feedback is implemented by heating/kicking particles to very high temperatures/velocities, 
which is necessary to overcome numerical overcooling. Because the gas particles subject to energy injection by feedback are selected from the
SPH neighbours of black holes/young stars, they tend to be
part of the dense interstellar medium. This implies that for
a few time steps following energy injection, i.e. until the
particles have responded hydrodynamically to the energy
injection, such dense and hot gas can artificially distort the
observational properties of galaxies, such as their X-ray
emission. We therefore advise to test the effect of excluding recently heated/kicked particles, which can be done
using the particle property tracking the last time a particle was injected with AGN feedback energy.

.. _issues_snia_normalisation:

SNIa normalisation
~~~~~~~~~~~~~~~~~~

In the code that implemented 
equation of the SNIa rate (equation 13 of the overview paper)
the sign of :math:`t_{delay}` in the exponent was incorrect
(it was added rather than subtracted).
This effects the normalisation of the DTD relation by ~4%.
Runs affected:

* ``L0100N0752/Thermal``
* ``L0100N0752/Hybrid``
* ``L0200N1504/Thermal``
* ``L0200N1504/Hybrid``
* ``L0050N0752/Thermal``
* ``L0050N0752/Hybrid``
* ``L0100N1504/Thermal``

.. Also the old variation runs?

Snapshots
---------

.. _issues_overflow_progenitor_id:

Overflow in progenitor IDs
~~~~~~~~~~~~~~~~~~~~~~~~~~

The field ``ProgenitorParticleIDs`` was initialised with values that overflowed for some particles.
Runs affected:

* ``L0100N0752/Thermal``
* ``L0100N0752/Hybrid``
* ``L0200N1504/Thermal``
* ``L0050N0752/Thermal``
* ``L0050N0752/Hybrid``
* ``L0100N1504/Thermal``

.. Also the old variation runs?

.. _issues_untrackable_splits:

Untrackable splits
~~~~~~~~~~~~~~~~~~

The information that is used to track particle splits can accomodate up to 64 splits. A very small number of particles have > 64.

Runs affected:

* ``L0050N0752/Thermal``
* ``L0050N0752/Hybrid``
* ``L0100N1504/Thermal``

.. Also the old variation runs?

.. _issues_kicked_particles_tracer:

Kicked particles tracer
~~~~~~~~~~~~~~~~~~~~~~~

The jet-related tracer recording BH IDs that kicked particles had a max value of 127

Runs affected:

* ``L0100N0752/Hybrid``
* ``L0200N1504/Hybrid``
* ``L0050N0752/Hybrid``

.. Also the old variation runs?

.. _issues_z0_averaged:

No z=0 averaged quantities
~~~~~~~~~~~~~~~~~~~~~~~~~~

Averaged quantities (SFR, BH accretion) are missing for the z=0 snapshot

* ``L0100N0752/Thermal``
* ``L0100N0752/Hybrid``
* ``L0200N1504/Thermal``
* ``L0200N1504/Hybrid``
* ``L0050N0752/Hybrid``


.. Also the old variation runs?

.. _issues_z0_negative:

Negative averaged quantities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A small number of particles have averaged quantities (SFR, BH accretion) which are negative

* ``L0100N0752/Thermal``
* ``L0100N0752/Hybrid``
* ``L0200N1504/Thermal``
* ``L0200N1504/Hybrid``
* ``L0050N0752/Hybrid``

.. Also the old variation runs?

SOAP
----

Missing hybrid quantities
~~~~~~~~~~~~~~~~~~~~~~~~~

The SOAP catalogues for runs with hybrid AGN feedback
:ref:`have some additional properties <soap_hybrid_properties>` not present in
the thermal AGN runs. However, some hybrid SOAPs were run using
the wrong paramter file, and so are missing the additional properties. These
will be added in the future. Runs affected:

* ``L01000N1504/Hybrid``: snapshots 110-118, 120-122, 124

Missing descendant track id
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SOAP catalogues contain the property ``soap.descendant_index`` which gives
the index for the descendant of each subhalo. For some SOAP catalogues these
values are missing. These will be added in the future.

Incorrect Hubble parameter for flow rate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :math:`z=0` value of the Hubble parameter was used when computing
:ref:`the flow rates <footnote-7>` for all redshifts.
