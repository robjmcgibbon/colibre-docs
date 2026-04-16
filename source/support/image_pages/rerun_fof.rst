:orphan:

Rerunning of Friend of Friends
==============================

.. _issues_rerun_fof:


Initially, the Friends of Friends (FoF) algorithm was configured to link all particle species (dark matter and baryons) using a universal linking length.
However, prior to generating the HBT catalogues, the FoF was rerun using dark matter (DM) particles only.
Baryonic particles are attached to FoF groups based on their nearest DM neighbour.
This change results in negligible changes to halo mass and membership.

The final FoF group memberships are stored within the membership chunk files.
