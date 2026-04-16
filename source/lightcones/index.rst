Lightcone outputs
=================

When we observe the real Universe, the light from distant objects
takes time to reach us. This means we see these objects as they were
when the light was emitted. More distant objects are seen as they were
at earlier times.

The FLAMINGO simulations attempt to replicate this effect for easier
comparison with observations. We place several :doc:`virtual observers
<observers>` in the simulated volume of space at the present day, and
as the simulation evolves we identify and store particles which cross
each observer's lightcone. A particle crosses the lightcone when it
passes exactly the distance at which light emitted from it would
arrive at the observer today.

The FLAMINGO lightcone outputs include particle data, HEALPix maps, and
halo catalogues. These are described in the following sections:

.. toctree::
   :maxdepth: 2

   observers
   particle_lightcones
   healpix_lightcones
   halo_lightcones

