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
using the particle property tracking the last time a particle was injected with AGN feedback energy. For some
observables (Gas and Spectroscopic-like temperatures, ComptonY properties, X-ray
properties) the SOAP catalogues provide versions that exclude particles that were subject to direct AGN heating
in the last 15 Myr and whose temperatures are between
:math:`10^{-1}\Delta T_\text{AGN}` and :math:`10^{0.3}\Delta T_\text{AGN}`, where :math:`\Delta T_\text{AGN}` is the AGN heating temperature

