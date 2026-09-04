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

For computational efficiency reasons, black hole particles are only repositioned (i.e. moved by hand down the potential gradient to compensate for unresolved dynamical friction) onto gas particles. For gas-poor galaxies, such as low-mass satellites, this can have the consequence that black holes leave their host galaxy, either temporarily or permanently. Care should therefore be taken when studying black holes and/or AGN feedback in satellite galaxies (see :ref:`extra_info_bh_occupation_fraction`).

.. _issues_agn_heating:

Heating by feedback
~~~~~~~~~~~~~~~~~~~

AGN and SN feedback is implemented by heating/kicking particles to very high temperatures/velocities,
which is necessary to overcome numerical overcooling. Because the gas particles subject
to energy injection by feedback are selected from the
SPH neighbours of black holes/young stars, they tend to be
part of the dense interstellar medium. This implies that for
a few time steps following energy injection, i.e. until the
particles have responded hydrodynamically to the energy
injection, such dense and hot gas can artificially distort the
observational properties of galaxies, such as their X-ray
emission. We therefore advise to test the effect of excluding recently heated/kicked particles, which can be done
using the particle property tracking the last time a particle was injected with feedback energy.

.. _issues_spurious_bh_seeding:

Spurious black hole seeding
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the L200m6 simulation a single friends-of-friends black hole seeding pass
at :math:`a = 0.820801` (:math:`z \approx 0.218`) produced roughly
780,000 black holes in one step, about 45 times more than a normal seeding
pass at this redshift (typically 16,000-17,000).

These particles first appear in snapshot 114
and can be identified with ``FormationScaleFactors == 0.82080078125``.
At snapshot 114 about 77% of them are not in any FoF group
(``FOFGroupIDs == 2147483647``), with the remaining 23% assigned to a FoF group.
99% of these spurious black holes persist to :math:`z = 0`,
but the majority remain at their seed mass and do not grow
through accretion or mergers.
As a result global black hole scaling relations for this run
(e.g. the black hole mass - stellar mass relation) are unaffected.

Run restarted from snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The L200m6 DMO run experienced a disc failure at (:math:`z \approx 0.22`) and was
restarted from the most recent snapshot. This restart introduced minor
discontinuities in the time integration of some particle trajectories.
To quantify the effect of the restart, the L100m6 DMO run was restarted from the same
snapshot and compared with the uninterrupted run, with negligible differences
found between the two.

Snapshots
---------

.. _issues_overflow_progenitor_id:

Overflow in progenitor IDs
~~~~~~~~~~~~~~~~~~~~~~~~~~

For some runs the field ``ProgenitorParticleIDs`` was initialised with values that overflowed for some particles.

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

For some runs the information that is used to track particle splits
could only accommodate up to 64 splits.
This limit was due to the format of the ``SplitTrees`` dataset.
A very small number of particles in these runs have > 64 splits.

Runs affected:

* ``L0050N0752/Thermal``
* ``L0050N0752/Hybrid``
* ``L0100N1504/Thermal``

The updated version of the code can correctly track particle splits up to 255 splits,
as the ``SplitCounts`` dataset has datatype ``uint8``.
The following runs have a small number of particles with > 255 splits:

* ``L0050N1504/Thermal``

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

Time averaged quantities (SFRs and BH accretion rates) are missing for the z=0 snapshot

* ``L0100N0752/Thermal``
* ``L0100N0752/Hybrid``
* ``L0200N1504/Thermal``
* ``L0200N1504/Hybrid``
* ``L0050N0752/Hybrid``


.. Also the old variation runs?

.. _issues_z0_negative:

Negative time averaged quantities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The time averaged SFRs and BH accretion rates can be negative for a small number of particles.
This was due to a bug in how the averaging variable was initialised for timesteps straddling the start of the recording window.
If such a particle was hit by feedback before its timestep ends,
a correction term was left uncompensated, which produces a negative value in the snapshot.
Any negative values should be set to zero.

.. _issues_averaged_window:

Averaging window for closely spaced snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The time averaged SFRs and BH accretion rates are normally averaged over the
100 Myr (index 0) and 10 Myr (index 1) windows preceding each snapshot.
If the time between two consecutive snapshots is shorter than one of these windows,
the averaging window is instead set equal to that shorter interval.
Note this is not a bug. The accumulated quantity is normalised over the actual window
used, so the output is still a correctly averaged rate. For example, if two
snapshots are only 25 Myr apart, the value stored in index 0 is a rate averaged
over 25 Myr rather than 100 Myr.

.. _issues_hii_regions:

HII region flag
~~~~~~~~~~~~~~~

Gas particles have a property called ``HIIregionsEndTime``.
This value can be useful since if it is equal -1 the particle is currently deemed to be in an HII region.
Note however that some particles with ``HIIregionsEndTime == -1`` will have recently been hit by feedback,
and these should probably not be counted as HII regions (depending on your analysis).

This property was originally not enabled to be output, and so is completely missing
from certain runs, and is only available for low redshift outputs of other runs.
However, selecting particles with ``HI/H == 0`` and ``density/m_h > 10**-5``
will return the particles that are in HII regions (see :ref:`extra_info_hii_regions`).

HBT-HERONS
----------

.. _issues_hbt_high_cadence:

High cadence runs
~~~~~~~~~~~~~~~~~

The HBT catalogues for the high cadence runs were created using an older version
of the HBT code. This is because we needed to delete the snapshots of the runs as
they progressed due to the large data volume, which prevented us from rerunning the
new version of HBT-HERONS. This has the following minor effects:

* In HBT-HERONS we allow gas particles to be "reattached" to
  satellites, which allows for gas accretion onto satellite subhalos that otherwise
  would not occur. Some of this accreted gas does form stars within the satellites,
  and so without the reattachment step the stars are assigned to the central subhalo
  instead of the satellites. The high cadence runs do not have gas reattachment.
* In the high-cadence HBT-HERONS catalogues, a bug caused :math:`H(z)/h` to be
  used as the Hubble parameter instead of :math:`H(z)`. This affects the
  snapshots at which HBT restarted.
  The masses in the catalogues are always stored in units of :math:`10^{10}\,M_\odot`,
  so that value should be used directly instead of reading ``Cosmology/HubbleParam``
  to determine the mass units.

SOAP
----

Missing hybrid AGN feedback quantities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SOAP catalogues for runs with hybrid AGN feedback
:ref:`have some additional properties <soap_hybrid_properties>` not present in
the thermal AGN runs. However, some hybrid SOAPs were run using
the wrong parameter file, and so are missing the additional properties. These
will be added in the future. Runs affected:

* ``L0100N1504/Hybrid``: snapshots 110-118, 120-122, 124

Missing descendant track id
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SOAP catalogues contain the property ``soap.descendant_index`` which gives
the index for the descendant of each subhalo. For some SOAP catalogues these
values are missing. These will be added in the future.

Incorrect Hubble parameter for flow rate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :math:`z=0` value of the Hubble parameter was used when computing
:ref:`the flow rates <footnote-7>` for all redshifts.

.. _issues_overflow_snapshotindexoflastisolation:

Overflow in SnapshotIndexOfLastIsolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The field ``soap.input_halos_hbtplus.snapshot_of_last_isolation`` gives the
latest snapshot when this subhalo was a central. It should be -1 if the subhalo
has always been a central. However, the array was set to have an unsigned integer
datatype, meaning that it could only contain positive values. When the value
should have been -1 it wrapped around and was set as 18446744073709551615 instead
(:math:`2^{64} - 1`, the maximum possible value for unsigned int64).
