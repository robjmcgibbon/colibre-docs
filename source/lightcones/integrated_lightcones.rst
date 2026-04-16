Integrated lightcones
=====================

This page describes the integrated lightcone HEALPix maps that have
been produced in the analyses of the simulations.

.. _map_rotations:

Rotations
---------

At high redshifts, the the shells used to construct the FLAMINGO
HEALPix maps can be larger than the simulation box. This means that a
photon emitted at high redshift and travelling towards the observer
may pass through multiple periodic replications of the same structure,
introducing spurious correlations in the maps.

In the construction of the integrated maps described here, the
FLAMINGO shells have been rotated whenever the lightcone diameter
exceeds the box size. See section 2.2 of `Upadhye et al (2024)
<https://ui.adsabs.harvard.edu/abs/2024MNRAS.529.1862U/abstract>`__
and appendix A of `Broxterman et al (2024)
<https://ui.adsabs.harvard.edu/abs/2024MNRAS.529.2309B/abstract>`__
for a discussion of the effects of random rotation on CMB lensing and
weak lensing peak statistics, respectively.

The same rotation has been applied to the different observables,
meaning the different integrated maps can be directly compared and
cross correlated. The rotations that have been applied to the 1 cGpc
(``L1``) or 2.8 cGpc (``L2p8``) variations are

.. code-block:: python

    import healpy as hp
    import lightcone_io.healpix_maps as hm
    import numpy as np
    import astropy.units as u

    angles_L1=np.array([[0., 0. ,3.26757547, 3.26757547, 3.26757547, 1.51289711, 1.51289711, 3.13885639, 3.13885639, 3.13885639, 2.17061318, 2.17061318, 2.17061318, 2.17061318, 4.59420579, 4.59420579, 4.59420579, 1.14273623, 1.14273623, 1.14273623, 1.14273623, 2.02717201, 2.02717201, 2.02717201, 2.02717201, 2.77675054, 2.77675054, 2.77675054, 2.77675054, 2.77675054, 0.83245259, 0.83245259, 0.83245259, 0.83245259, 0.83245259, 0.83245259, 4.95779263, 4.95779263, 4.95779263, 4.95779263, 4.95779263, 4.95779263, 4.95779263, 2.52359739, 2.52359739, 2.52359739, 2.52359739, 2.52359739, 2.52359739, 2.52359739, 2.52359739, 2.69301628, 2.69301628, 2.69301628, 2.69301628, 2.69301628, 2.69301628, 2.69301628, 2.69301628, 2.69301628], [0., 0., 1.41518902, 1.41518902,  1.41518902, 0.80580058, 0.80580058, 0.71830831, 0.71830831, 0.71830831, 1.77536892, 1.77536892, 1.77536892, 1.77536892, 0.62434822, 0.62434822, 0.62434822, 2.14076603, 2.14076603, 2.14076603, 2.14076603, 0.49840908, 0.49840908, 0.49840908, 0.49840908, 2.0136344, 2.0136344, 2.0136344 , 2.0136344, 2.0136344,  2.25356928, 2.25356928, 2.25356928 , 2.25356928 , 2.25356928,  2.25356928, 1.85187078, 1.85187078, 1.85187078, 1.85187078, 1.85187078, 1.85187078 , 1.85187078, 1.36014098, 1.36014098, 1.36014098, 1.36014098, 1.36014098, 1.36014098, 1.36014098, 1.36014098, 2.35895331, 2.35895331, 2.35895331, 2.35895331, 2.35895331, 2.35895331, 2.35895331, 2.35895331, 2.35895331]])

    angles_L2p8=np.array(([[0., 0., 0., 0., 0., 0., 0.,  2.11833333, 2.11833333, 2.11833333, 2.11833333, 2.11833333, 2.11833333, 2.11833333, 2.11833333, 2.11833333, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 1.29070838, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 5.69217656, 3.79736641, 3.79736641, 3.79736641, 3.79736641,  3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 3.79736641, 1.32878635, 1.32878635, 1.32878635, 1.32878635, 1.32878635, 1.32878635], [0., 0., 0., 0., 0., 0., 0., 0.96440001, 0.96440001, 0.96440001, 0.96440001, 0.96440001, 0.96440001, 0.96440001, 0.96440001, 0.96440001, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 1.74841793, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 0.56258515, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313,  1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 1.45462313, 2.48706614, 2.48706614, 2.48706614, 2.48706614, 2.48706614, 2.48706614]]))

    path = f"/cosma8/data/dp004/flamingo/Runs/L1000N1800/L1_m9/neutrino_corrected_maps_downsampled_4096/"
    shells = hm.ShellArray(f"{path}", "lightcone0")

    def rotate_map(hmap, rot_theta, rot_phi):
        longitude = rot_phi*180/np.pi * u.deg
        latitude = rot_theta*180/np.pi * u.deg
        rot_custom = hp.Rotator(rot=[longitude.to_value(u.deg), latitude.to_value(u.deg)], inv=True)
        hmap = rot_custom.rotate_map_alms(hmap)
        return hmap

    for i in range(shells.nr_shells):
        total_mass_shell = shells[i]["TotalMass"][:]
        rotated_total_mass_shell = rotate_map(total_mass_shell,angles_L1[0,i],angles_L1[1,i])

Weak lensing convergence maps
-----------------------------

The maps are constructed using the backward ray-tracing methodology
described in `Broxterman et al (2024)
<https://ui.adsabs.harvard.edu/abs/2024MNRAS.529.2309B%2F/abstract>`__,
of which a later version of the code can be found `here
<https://github.com/JegerBroxterman/Lensing_raytrace_FLAMINGO>`__. At
each of the FLAMINGO mass shells, the rays are deflected according to
the gravitational potential. The files correspond to integrated weak
lensing convergence maps (:math:`\kappa`) that assume an
non-tomographic Euclid-like source redshift distribution and are saved
as ring-ordered Healpix maps at :math:`N_\mathrm{side} = 8192`. No
smoothing or noise has been applied to these files.

Each simulation has a subdirectory ``value_add/broxterman24`` which
contains the convergence maps. For example, the maps for ``L1_m9`` are
in `this directory
</flamingo/viewer.html?path=FLAMINGO/L1_m9/L1_m9/value_add/broxterman24>`__. The
files can be accessed using the :doc:`hdfstream
</service_docs/python_module>` module or downloaded and read directly,
as shown below.

.. tab-set::

   .. tab-item:: Remote access

      .. code-block:: python

         import hdfstream
         file_path = 'FLAMINGO/L1_m9/L1_m9/value_add/broxterman24/WL_convergence_Euclid_like_nz_Broxterman24_L1_m9_lc0.hdf5'
         with hdfstream.open("cosma", file_path) as data_file:
           kappa_map = data_file["Convergence"][:]

   .. tab-item:: Reading downloaded files

      .. code-block:: python

         import h5py
         file_path = './FLAMINGO/L1_m9/L1_m9/value_add/broxterman24/WL_convergence_Euclid_like_nz_Broxterman24_L1_m9_lc0.hdf5'
         with h5py.File(f"/{file_path}",'r') as data_file:
           kappa_map = data_file["Convergence"][:]

where the part ``L1_m9_lc0`` changes between the variations and lightcones (lc), for example,
``L2p8_m9_DMO_lc4`` for observer four in the 2800 cGpc dark-matter-only box.



ROSAT convolved X-ray All-Sky maps
----------------------------------

The ROSAT convolved X-ray All-Sky maps are computed as described in
section 3.1 of `McDonald et al (2026)
<https://ui.adsabs.harvard.edu/abs/2026arXiv260202484M/abstract>`__. Briefly,
these HEALPix all-sky maps are computed from the particle lightcones
and present the photon count rate in the soft band (0.5-2.0 keV) from
hot gas on the sky integrated from redshift 0 to 0.5. The X-ray
emission is convolved with the effective area of the ROSAT detector
response matrix. Specifically these ring-ordered HEALPix maps are
constructed at :math:`N_\mathrm{side} = 4096` from the particle
lightcone (of the 0th observer of each ``L1_m9`` simulation
given). When integrating along the line of sight the on-sky
coordinates of the gas particles in each shell are rotated as
described in `Broxterman et al (2024)
<https://ui.adsabs.harvard.edu/abs/2024MNRAS.529.2309B%2F/abstract>`__.

Each simulation has a subdirectory ``value_add/mcdonald26`` which
contains the X-ray maps. For example, the maps for ``L1_m9`` are
in `this directory
</flamingo/viewer.html?path=FLAMINGO/L1_m9/L1_m9/value_add/mcdonald26>`__. The
files can be accessed using the :doc:`hdfstream
</service_docs/python_module>` module or downloaded and read
directly. Below, we show how to read the maps:

.. tab-set::

   .. tab-item:: Remote access

      .. code-block:: python

         import hdfstream

         xray_source="Gas"
         map_name="XrayROSATIntrinsicPhotonsConvolved"
         with hdfstream.open("cosma", "./FLAMINGO/L1_m9/L1_m9/value_add/mcdonald26/ROSAT_convolved_Xray_AllSky_L1_m9.hdf5", "r") as integrated_map:

           # read ROSAT convolved photon flux X-ray map
           ROSAT_Xray_map=integrated_map[xray_source+'/'+map_name][:]

           # print simulations identifier (name) in FLAMINGO papers:
           print("\tFLAMINGO identifier: {label}".format(label=integrated_map[xray_source].attrs['paper_name'][:]))

           # print integrated redshift range:
           lc_zmin=integrated_map[xray_source].attrs['redshift_min'] lc_zmax=integrated_map[xray_source].attrs['redshift_max']
           print("\tredshift range: {zmin:.3f}, {zmax:.3f}".format(zmin=lc_zmin, zmax=lc_zmax))

           # print expression for map units:
           print("\tunit expression: {map_units}".format(map_units=integrated_map[xray_source].attrs['unit_expression']))

   .. tab-item:: Reading local files

      .. code-block:: python

         import h5py

         xray_source="Gas"
         map_name="XrayROSATIntrinsicPhotonsConvolved"
         with h5py.File("./FLAMINGO/L1_m9/L1_m9/value_add/mcdonald26/ROSAT_convolved_Xray_AllSky_L1_m9.hdf5", "r") as integrated_map:

           # read ROSAT convolved photon flux X-ray map
           ROSAT_Xray_map=integrated_map[xray_source+'/'+map_name][:]

           # print simulations identifier (name) in FLAMINGO papers:
           print("\tFLAMINGO identifier: {label}".format(label=integrated_map[xray_source].attrs['paper_name'][:]))

           # print integrated redshift range:
           lc_zmin=integrated_map[xray_source].attrs['redshift_min'] lc_zmax=integrated_map[xray_source].attrs['redshift_max']
           print("\tredshift range: {zmin:.3f}, {zmax:.3f}".format(zmin=lc_zmin, zmax=lc_zmax))

           # print expression for map units:
           print("\tunit expression: {map_units}".format(map_units=integrated_map[xray_source].attrs['unit_expression']))

Note, these maps are given in units of :math:`\mathrm{photon}/
\mathrm{s} / A_\mathrm{pix}` where :math:`A_\mathrm{pix}` is the area
of a pixel in the HEALPix map of a given :math:`N_\mathrm{side}` . See
the example given below for how to convert the map from per pixel area
to per steradian (or square degree.)

.. code-block:: python

    import h5py
    import healpy as hp
    import unyt
    xray_source="Gas"
    map_name="XrayROSATIntrinsicPhotonsConvolved"

    with h5py.File("./FLAMINGO/L1_m9/L1_m9/value_add/mcdonald26/ROSAT_convolved_Xray_AllSky_L1_m9.hdf5", "r") as integrated_map:
        # read map
        ROSAT_Xray_map_per_sr=integrated_map[xray_source+'/'+map_name][:]
        nside = integrated_map[xray_source].attrs['shell_nside'] # can take nside from map attributes, otherwise confirm from the number of pixels in the map
        # apply unit transformation and define map units
        ROSAT_Xray_map_per_sr /= hp.nside2pixarea(nside, degrees=False) * unyt.photon / unyt.s / unyt.radian**2

AGN Point Source Maps
---------------------

These maps will be made available with the publication of `McDonald et
al (2026)
<https://ui.adsabs.harvard.edu/abs/2026arXiv260202484M/abstract>`__.

We include 2 sets of AGN point source maps, 1) a "base" AGN map and 2)
an abundance matched (AM) AGN map.  The base AGN X-ray emission is
estimated from the mass accretion rates of black hole (BH) particles
within the FLAMINGO particle lightcones. The AM AGN maps are
constructed by matching the abundances of BH luminosities to the
observed luminosity functions given by `Shen et al (2020)
<https://ui.adsabs.harvard.edu/abs/2020MNRAS.495.3252S/abstract>`__,
specifically we only use the most massive massive massive BH per
central halo with the abundance matching.  Both sets of maps are
described in sections 3.1 and 3.2 of `McDonald et al (2026)
<https://ui.adsabs.harvard.edu/abs/2026arXiv260202484M/abstract>`__.)

Both of these maps can be accessed as demonstrated:

.. code-block:: python

    with h5py.File("./FLAMINGO/L1_m9/L1_m9/value_add/mcdonald26/ROSAT_convolved_Xray_AllSky_L1_m9.hdf5", "r") as integrated_map:
        AGN_names=["AGN_base", "AGN_AM"]
	ROSAT_point_source_maps={}
        for xray_source in AGN_names:
            ROSAT_point_source_maps[xray_source]=integrated_map[xray_source+'/'+map_name][:]


Integrated Thermal SZ Maps
--------------------------

These maps will be made available with the publication of `Yang et
al. (2026)
<https://ui.adsabs.harvard.edu/abs/2025arXiv251209891Y/abstract>`__.

These are integrated maps constructed by accumulating the Compton-y parameter maps from individual lightcone shells (`Schaye et al., 2023 <https://ui.adsabs.harvard.edu/abs/2023MNRAS.526.4978S/abstract>`__, Appendix A2.3). Lensing effects are included using `pixell <https://pixell.readthedocs.io/en/latest/>`__, applied shell by shell with the integrated convergence map up to the shell of interest. Note that the Compton-y shells exclude contributions from gas particles that have recently been directly heated by AGN feedback. The maps are organised in ring ordering with :math:`N_\mathrm{side} = 4096`. Below, we show how to read the maps and convert them into a :math:`\Delta T_\mathrm{CMB}` map.

.. code-block:: python
    
    import h5py

    ##tSZ SED, assuming no relativistic corrections:
    x = h*freq_test*1e9/(T_cmb*k_B)
    tSZ_freq_dep_func = x*(np.cosh(x/2)/np.sinh(x/2))-4
    
    lensed_tSZ_map = h5py.File(map_save_dir+'lightcone0_shells/lensed_tSZ_rot_same_rot.hdf5', 'r')['data'][...]
    delta_T_tSZ = tSZ_freq_dep_func * lensed_tSZ_map * T_cmb ## in K_CMB

Integrated Kinetic SZ Maps
--------------------------

These maps will be made available with the publication of `Yang et
al. (2026)
<https://ui.adsabs.harvard.edu/abs/2025arXiv251209891Y/abstract>`__.

These are integrated maps constructed by accumulating the Doppler-b parameter maps from individual lightcone shells (`Schaye et al., 2023 <https://ui.adsabs.harvard.edu/abs/2023MNRAS.526.4978S/abstract>`__, Appendix A2.3). Lensing effects are computed using the same procedure as used for lensing of the thermal SZ map. The maps are organised in ring ordering with :math:`N_\mathrm{side} = 4096`. Below, we show how to read the maps and convert them into a :math:`\Delta T_\mathrm{CMB}` map.

.. code-block:: python
    
    import h5py
    
    lensed_kSZ_map = h5py.File(map_save_dir+'lightcone0_shells/lensed_kSZ_rot_same_rot.hdf5', 'r')['data'][...]
    delta_T_kSZ = -lensed_kSZ_map * T_cmb ## in K_CMB 

Integrated Relativistically Corrected Thermal SZ Maps
-----------------------------------------------------

These maps will be made available with the publication of `Yang et
al. (2026)
<https://ui.adsabs.harvard.edu/abs/2025arXiv251209891Y/abstract>`__.

These are the relativistically corrected version of the thermal SZ intensity fluctuation maps, with the correction function computed using
SZpack (`Chluba et al., 2012 <https://ui.adsabs.harvard.edu/abs/2012MNRAS.426..510C/abstract>`__, `2013 <https://ui.adsabs.harvard.edu/abs/2013MNRAS.430.3054C/abstract>`__). For now, only maps under lightcone1_shells for the 2.8 Gpc box run are available. Maps are given in MJy/sr, and are organised in ring ordering with :math:`N_\mathrm{side} = 4096`. To convert intensity maps into :math:`\Delta T_\mathrm{CMB}` maps, a conversion factor is required, computed as:

.. code-block:: python

    import h5py
    import numpy as np
    
    def prefactor(x_freq):

    	exp_x = np.exp(x_freq)
    	prefactor = x_freq**4. * exp_x / (exp_x - 1.)**2.

	return prefactor

    x_CMB = h * freq_test * 1e9 / (T_cmb * k_B)
    pref = prefactor(x_CMB)
    unit_conv = (I_0 / T_cmb) * pref ## where I_0 = 270 MJy/sr.
    
    delta_T_rel_tSZ = h5py.File(map_save_dir + 'L2p8_m9_fid/lightcone1_shells/delta_ItSZ_'+str(freq_test)+'_rot_same_rot_MJy_sr.hdf5', 'r')['data'][...] / unit_conv ## in K_CMB

Integrated Cosmic Infrared Background Maps
------------------------------------------

These maps will be made available with the publication of `Yang et
al. (2026)
<https://ui.adsabs.harvard.edu/abs/2025arXiv251209891Y/abstract>`__.

These are integrated maps generated from the star formation rate lightcone outputs, with the bolometric infrared luminosity assumed to be proportional to the star formation rate (`Kennicutt, 1998 <https://ui.adsabs.harvard.edu/abs/1998ApJ...498..541K/abstract>`__). The luminosity at a given frequency is then computed using a greybody radiation SED for infrared sources (`Planck Collaboration et al., 2016 <https://ui.adsabs.harvard.edu/abs/2016A%26A...594A..15P/abstract>`__), with the SED parameters determined by fitting to the measured 353, 545, and 857 GHz CIB power spectra from `Lenz et al. (2019) <https://ui.adsabs.harvard.edu/abs/2019ApJ...883...75L/abstract>`__. The same procedure as used for lensing of the thermal SZ map is applied here. Only maps at 217, 353, 545, and 857 GHz are provided here, which have been validated against observational CIB power spectra ( `Planck Collaboration et al., 2014 <https://ui.adsabs.harvard.edu/abs/2014A%26A...571A..30P/abstract>`__ and `Lenz et al., 2019 <https://ui.adsabs.harvard.edu/abs/2019ApJ...883...75L/abstract>`__ ). Maps at other frequencies can be generated upon request. Maps are provided in the unit of Jy/sr, and are organised in ring ordering with :math:`N_\mathrm{side} = 4096`. Maps are generated using the default three-parameter model discussed in `Yang et al. (2026) <https://ui.adsabs.harvard.edu/abs/2025arXiv251209891Y/abstract>`__. Below, we show how to read the maps and convert them into a :math:`\Delta T_\mathrm{CMB}` map. Conversion factors from Jy/sr to K_CMB are taken from Table 6 in `Planck Collaboration et al. (2014) <https://ui.adsabs.harvard.edu/abs/2014A%26A...571A...9P/abstract>`__.

.. code-block:: python

    import h5py

    lensed_CIB_map = h5py.File(map_save_dir+'lightcone0_shells/lensed_CIB_rot_BANDPASS_F'+str(freq_test)+'_three_params_same_rot.hdf5', 'r')['data'][...]
    delta_T_CIB = lensed_CIB_map*unit_conv ## in K_CMB. Please see Planck Collaboration et al. (2014) above for the unit conversion at each frequency.

Integrated Radio Point Source Maps
----------------------------------

These maps will be made available with the publication of `Yang et
al. (2026)
<https://ui.adsabs.harvard.edu/abs/2025arXiv251209891Y/abstract>`__.

These are integrated maps constructed from the black hole particle lightcone outputs. Radio luminosities are assigned by abundance matching the bolometric AGN luminosity function to the LOFAR 150 MHz luminosity function up to z = 2.5 (`Kondapally et al., 2022 <https://ui.adsabs.harvard.edu/abs/2022MNRAS.513.3742K/abstract>`__). The lensed source fluxes are extrapolated to higher CMB frequencies using a power-law SED, with the power index fitted to match the measured radio source counts from the SPT survey at 95, 150, and 220 GHz (`Everett et al., 2020 <https://ui.adsabs.harvard.edu/abs/2020ApJ...900...55E/abstract>`__). The procedure is repeated for subsamples selected by black hole accretion state using different Eddington ratio cuts, :math:`\lambda_\mathrm{Edd}< 10^{−2}, 10^{−3}, 10^{−6}`. Maps are provided in the unit of Jy/sr at 150 MHz, and are organised in ring ordering with :math:`N_\mathrm{side} = 4096`. While rescaling radio maps to higher CMB frequencies, each case has its own SED power-law index parameter. Maps are provided without any radio flux-density cuts. 3D radio lightcone catalogues are available upon request. Below, we show how to read the maps and convert them into a :math:`\Delta T_\mathrm{CMB}` map.

.. code-block:: python

    import h5py
    
    ##radio:
    alpha_rad = -0.56
    # alpha_rad = -0.58 ##if reading in lensed_radiops_rot_llim_0.001_MBHcut.hdf5
    # alpha_rad = -0.61 ##if reading in lensed_radiops_rot_llim_1e-06_MBHcut.hdf5
    radio_freq_dep_func = ((freq_test*1e9)/(150e6))**(alpha_rad)

    lensed_radio_map = h5py.File(map_save_dir+'lightcone0_shells/lensed_radiops_rot_llim_0.01_MBHcut_same_rot.hdf5', 'r')['data'][...]
    delta_T_radio = ( lensed_radio_map * radio_freq_dep_func )*unit_conv ## in K_CMB. Please see Planck Collaboration et al. (2014) above for the unit conversion at each frequency.

Integrated Anisotropic Screening (optical depth :math:`\tau`) Maps
------------------------------------------------------------------

These maps will be made available with the publication of `Yang et
al. (2026)
<https://ui.adsabs.harvard.edu/abs/2025arXiv251209891Y/abstract>`__.

These are integrated maps stacked from the dispersion measure maps per individual lightcone shells (`Schaye et al., 2023 <https://ui.adsabs.harvard.edu/abs/2023MNRAS.526.4978S/abstract>`__, Appendix A2.3). The maps are organised in ring ordering with :math:`N_\mathrm{side} = 4096`. Below, we show how to read the maps and convert them into a :math:`\Delta T_\mathrm{CMB}` map.

.. code-block:: python

    import h5py

    lensed_DM_map = h5py.File(map_save_dir+'lightcone0_shells/lensed_DM_rot_same_rot.hdf5', 'r')['data'][...]
    delta_tau_map = (lensed_DM_map - np.mean(lensed_DM_map)) * (3.085677581*1e22)**(-2) * 6.65 * 1e-29 ## convert the Thomson scattering cross-section in m^2 to Mpc^2, so delta_tau is dimensionless
    delta_T_patchy = delta_tau_map * delta_T_CMB_prim ## if want to include the patchy screening effect, with delta_T_CMB_prim from e.g. CAMB in K_CMB.


