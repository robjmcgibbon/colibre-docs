Power spectra
=============

Each simulation directory contains a set of ASCII text files representing various power spectra and cross-spectra. These are available at 123 different redshifts, indexed from ``0000`` to ``0122``. 

.. dropdown:: Table of power spectra output redshifts

   .. list-table::
      :header-rows: 1

      * - Index
        - Redshift
      * - 0
        - 30.00
      * - 1
        - 29.00
      * - 2
        - 28.00
      * - 3
        - 27.00
      * - 4
        - 26.00
      * - 5
        - 25.00
      * - 6
        - 24.00
      * - 7
        - 23.00
      * - 8
        - 22.00
      * - 9
        - 21.00
      * - 10
        - 20.00
      * - 11
        - 19.50
      * - 12
        - 19.00
      * - 13
        - 18.50
      * - 14
        - 18.00
      * - 15
        - 17.50
      * - 16
        - 17.00
      * - 17
        - 16.50
      * - 18
        - 16.00
      * - 19
        - 15.50
      * - 20
        - 15.00
      * - 21
        - 14.50
      * - 22
        - 14.00
      * - 23
        - 13.50
      * - 24
        - 13.00
      * - 25
        - 12.50
      * - 26
        - 12.00
      * - 27
        - 11.75
      * - 28
        - 11.50
      * - 29
        - 11.25
      * - 30
        - 11.00
      * - 31
        - 10.75
      * - 32
        - 10.50
      * - 33
        - 10.25
      * - 34
        - 10.00
      * - 35
        - 9.75
      * - 36
        - 9.50
      * - 37
        - 9.25
      * - 38
        - 9.00
      * - 39
        - 8.75
      * - 40
        - 8.50
      * - 41
        - 8.25
      * - 42
        - 8.00
      * - 43
        - 7.75
      * - 44
        - 7.50
      * - 45
        - 7.25
      * - 46
        - 7.00
      * - 47
        - 6.75
      * - 48
        - 6.50
      * - 49
        - 6.25
      * - 50
        - 6.00
      * - 51
        - 5.75
      * - 52
        - 5.50
      * - 53
        - 5.25
      * - 54
        - 5.00
      * - 55
        - 4.75
      * - 56
        - 4.50
      * - 57
        - 4.25
      * - 58
        - 4.00
      * - 59
        - 3.75
      * - 60
        - 3.50
      * - 61
        - 3.25
      * - 62
        - 3.00
      * - 63
        - 2.95
      * - 64
        - 2.90
      * - 65
        - 2.85
      * - 66
        - 2.80
      * - 67
        - 2.75
      * - 68
        - 2.70
      * - 69
        - 2.65
      * - 70
        - 2.60
      * - 71
        - 2.55
      * - 72
        - 2.50
      * - 73
        - 2.45
      * - 74
        - 2.40
      * - 75
        - 2.35
      * - 76
        - 2.30
      * - 77
        - 2.25
      * - 78
        - 2.20
      * - 79
        - 2.15
      * - 80
        - 2.10
      * - 81
        - 2.05
      * - 82
        - 2.00
      * - 83
        - 1.95
      * - 84
        - 1.90
      * - 85
        - 1.85
      * - 86
        - 1.80
      * - 87
        - 1.75
      * - 88
        - 1.70
      * - 89
        - 1.65
      * - 90
        - 1.60
      * - 91
        - 1.55
      * - 92
        - 1.50
      * - 93
        - 1.45
      * - 94
        - 1.40
      * - 95
        - 1.35
      * - 96
        - 1.30
      * - 97
        - 1.25
      * - 98
        - 1.20
      * - 99
        - 1.15
      * - 100
        - 1.10
      * - 101
        - 1.05
      * - 102
        - 1.00
      * - 103
        - 0.95
      * - 104
        - 0.90
      * - 105
        - 0.85
      * - 106
        - 0.80
      * - 107
        - 0.75
      * - 108
        - 0.70
      * - 109
        - 0.65
      * - 110
        - 0.60
      * - 111
        - 0.55
      * - 112
        - 0.50
      * - 113
        - 0.45
      * - 114
        - 0.40
      * - 115
        - 0.35
      * - 116
        - 0.30
      * - 117
        - 0.25
      * - 118
        - 0.20
      * - 119
        - 0.15
      * - 120
        - 0.10
      * - 121
        - 0.05
      * - 122
        - 0.00

The files follow the naming convention ``power_<type>_<index>.txt``. The following types of auto-spectra and cross-spectra are available:

* **Auto-spectra**:
    * ``matter``: Total matter
    * ``cdm``: Cold Dark Matter (CDM)
    * ``gas``: Gas
    * ``starBH``: Stars and Black Holes
    * ``pressure``: Electron pressure :math:`P_e = n_e k_B T`, where :math:`n_e` is the electron density, :math:`k_B` is the Boltzmann constant, and :math:`T` is the temperature.

* **Cross-spectra**:
    * ``cdm-gas``: CDM and gas
    * ``cdm-neutrino``: CDM and neutrinos
    * ``cdm-starBH``: CDM and stars/Black Holes
    * ``gas-matter``: Gas and total matter
    * ``gas-neutrino``: Gas and neutrinos
    * ``gas-starBH``: Gas and stars/Black Holes
    * ``matter-pressure``: Total matter and electron pressure
    * ``starBH-neutrino``: Stars/Black Holes and neutrinos
    * ``neutrino0-neutrino1``: Cross-correlation between the two neutrino particle realisations (used for shot-noise suppression)

The power spectra do contain some small artifacts (such as the small peak in the middle of the z=2 line if you run the example below for the L1_m9 outputs) which are due to combining foldings, and are not real. An example set of power spectrum files (for the ``L1_m9`` run) can be seen in the directory `L1_m9/L1_m9/power_spectra </flamingo/viewer.html?path=FLAMINGO/L1_m9/L1_m9/power_spectra>`__.

The files are stored as plain text with a descriptive header. The data is organized into three space-separated columns:

  * ``Column (0) - Redshift (z)``: The redshift of the output.
  * ``Column (1) - Wavenumber (k)``: The wavenumber in units of :math:`\mathrm{Mpc}^{-1}` (note that there is **no** factor of :math:`\textit{h}`).
  * ``Column (2) - Power (P(k))``: The shot-noise subtracted power in units of :math:`\mathrm{Mpc}^{3}` (note that there is **no** factor of :math:`\textit{h}^3`).

The example below shows how to load two files and plot the results.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt

   fig, ax = plt.subplots(1)

   # Loading the matter power spectrum at z=2 and z=0
   for filename in ['power_matter_0082.txt', 'power_matter_0122.txt']:

       # Load the data (skipping the header automatically)
       data = np.loadtxt(filename)

       # Extract columns
       z = data[0, 0]   # Redshift is the same for all rows in a single file
       k = data[:, 1]   # Fourier scale k [Mpc^-1]
       pk = data[:, 2]  # Power P(k) [Mpc^3]

       # Plot the power spectrum
       ax.plot(k, pk, label=f'z = {z:.2f}')

   ax.set_xlabel(r'$k$ [$\mathrm{Mpc}^{-1}$]')
   ax.set_ylabel(r'$P(k)$ [$\mathrm{Mpc}^{3}$]')
   ax.loglog()
   ax.legend()

   plt.show()

Baryonic response emulator
--------------------------

A Gaussian process emulator to model the effect of baryons on the matter power spectrum for all the simulations varying feedback in the FLAMINGO suite has been developed as part of `Schaller et al. (2025)
<https://ui.adsabs.harvard.edu/abs/2025MNRAS.539.1337S/abstract>`__. It is available via PyPI index ( ``pip install FlamingoBaryonResponseEmulator`` ) or `from github
<https://github.com/FLAMINGOSIM/FlamingoBaryonResponseEmulator>`__, where examples are also available.

The emulator can be used to predict the deviation of the matter power spectrum for the hydrodynamical simulation from the corresponding dark matter only simulation due to baryon and galaxy formation physics. The response as a function of wavenumber k is returned by the emulator as a function of redshift and three parameters characterizing the galaxy and cluster properties in the simulations. These are (i) the offset in the gas fraction in clusters from the Xray-based data used for the calibration of the simulations, (ii) the offset in the galaxy masses from the stellar mass function data used for the calibration, and (iii) the fraction of the AGN feedback taking place in the form of collimated jets as opposed to thermally-driven winds. The emulator is accurate to better than 1% for redshifts lower than 2 and for comoving scales up to k=10h/Mpc. Evaluation of the response for a given model is fast (1ms on 1 CPU core). 

