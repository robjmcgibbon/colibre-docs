High cadence runs
=================

There are which were used to generate the videos on the colibre website. There are 3 runs:

* ``/cosma8/data/dp004/colibre/Runs/L0050N0752/Thermal_HighCadence`` - L050m6 run with 2000 outputs
* ``/cosma8/data/dp004/colibre/Runs/L0050N0752/Hybrid_HighCadence`` - L050m6h run with 2000 outputs
* ``/cosma8/data/dp004/colibre/Runs/L0012N0376/Thermal_HighCadence`` - L012m5 run with 10000 outputs


For all these high cadence runs the outputs are evenly spaced in :math:`\log a`.
They have the same initial conditions and subgrid model parameters as the fiducial runs.
However, due to noise within the simulations, the galaxies that form in these runs will not be exactly the same as those in the fiducial runs. 
There are only a few particle properties saved for these runs, significantly less than in the normal snapshots.
Most of the dark matter particles have been removed, although 10% of it has been kept for every 10th snapshot.
HBT catalogues are available, but these came from an old version of HBT (no gas reattachment).
No SOAP catalogues are available.
