Initial conditions
==================

The initial conditions for all simulations are available ``/cosma8/data/dp004/colibre/InitialConditions``. These files are not compatible with swiftsimio, and so the HDF5 files must be opened directly.

Initial snapshot
----------------

For a number of runs we have produced an "initial snapshot". This was created by running the simulation for a single timestep, and then dumping a snapshot. These files can therefore be opened using swiftsimio. They contain the following datasets for gas and dark matter particles:

* ``Coordinates``
* ``Densities`` (Gas only)
* ``Masses``
* ``ParticleIDs``
* ``Potentials``
* ``SmoothingLengths`` (Gas only)
* ``Velocities``

The initial snapshots can be found within the ``initial_snapshot/`` directory of the following runs:

* L400m7/Thermal
* L200m6/Thermal

