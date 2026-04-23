.. _snapshot_los:

Line-of-sight files
===================

To facilitate the production of mock quasar absorption spectra at
high-cadence without having to read all the data, we frequently save
the SPH particles that overlap with 35 randomly positioned lines
parallel to the :math:`x` axis of the cubic simulation volume and similarly
for the :math:`y` and :math:`z` axes. These "line-of-sight" outputs commence at
expansion factor :math:`a = 0.1` and are produced at 
intervals of :math:`\Delta a = 0.1a`,
yielding 232 output times in total.

Each simulation has a ``los`` directory with one
``los_XXXX.hdf5`` file for each output.
The line-of-sight files can be read with swiftimio, and
contain all the gas fields present in the snapshots.

These files are made to be used with an updated version of the
SpecWizard (`Theuns et al 1998
<https://ui.adsabs.harvard.edu/abs/1998MNRAS.301..478T>`__,  `Schaye et al. 2003
<https://ui.adsabs.harvard.edu/abs/2003ApJ...596..768S>`__) code,
please get in contact if you are interested.
