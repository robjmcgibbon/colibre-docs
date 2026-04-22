import re

import h5py
import numpy as np
import unyt

############# Output properties for each run type

corrections = {
    'SpeciesFractions': r'Species fractions array for all ions and molecules in the CHIMES network. The fraction of species i is defined in terms of its number density relative to hydrogen, i.e. :math:`n_i` / :math:`n_{H_{tot}}`. ``ReducedSpeciesFractions`` is available for snipshots. See :ref:`species-names`.',
    'VelocityDivergenceTimeDifferentials': r'Time differential (over the previous step) of the velocity divergence field around the particles. Again, provided without cosmology as this includes a Hubble flow term.',
    'VelocityDivergences': r'Local velocity divergence field around the particles. Provided without cosmology, as this includes the Hubble flow.',
    'KickedByJetFeedback': r'Flags the particles that have been directly kicked by an AGN jet feedback event at some point in the past. If greater than 0, contains the number of individual events',
    'GasVelocityDispersions': r'Velocity dispersion (3D) of the gas particles around the black holes. This is :math:`a \sqrt{<|dx/dt|^2> - <|dx/dt|>^2}` where x is the co-moving position of the particles relative to the black holes.',
    'MinimalSmoothingLengths': 'Minimal smoothing lengths ever reached by the particles',
    'AveragedStarFormationRates': r'Star formation rates of the particles averaged over the period set by the first two snapshot triggers. See :ref:`footnote_averaged`',
    'AveragedAccretionRates': r'Accretion rates of the black holes averaged over the period set by the first two snapshot triggers. See :ref:`footnote_averaged`',
    'Velocities': r'Peculiar velocities of the particles. This is :math:`a \frac{dx}{dt}` where :math:`x` is the co-moving position of the particles.',
    'DustMassFractions': r"Fractions of the particles' masses that are in a given species of dust grain. See :ref:`dust-names`.",
    'ElementMassFractions': r"Fractions of the particles' masses that are in the given element. ``ReducedElementMassFractions`` is available for snipshots. See :ref:`element-names`.",
    'ElementMassFractionsDiffuse': r"Fractions of the particles' masses that are in the given element and in the diffuse (non-dust) phase. See :ref:`element-names`.",
    'Luminosities': r"Rest-frame dust-free AB-luminosities of the star particles in the GAMA bands. See :ref:`luminosities`.",
    'XrayLuminosities': r"Intrinsic X-ray luminosities in various bands. This is 0 for star-forming particles. See :ref:`xray-bands`.",
    'XrayPhotonLuminosities': r"Intrinsic X-ray photon luminosities in various bands. This is 0 for star-forming particles. See :ref:`xray-bands`.",
    'HIIregionsEndTime': r"Time until particle is in HII region. See :ref:`hii_end_time`",
}

colibre_dir = '/cosma8/data/dp004/colibre/Runs/'
snapshots = {
    'snip': f'{colibre_dir}/L100_m7/HYBRID_AGN_m7/snapshots/colibre_0126/colibre_0126.hdf5',
    'thermal': f'{colibre_dir}/L400_m7/Thermal/snapshots/colibre_0127/colibre_0127.hdf5',
    'hybrid': f'{colibre_dir}/L100_m7/HYBRID_AGN_m7/snapshots/colibre_0127/colibre_0127.hdf5',
    'gcs': '/cosma8/data/dp004/jlvc76/COLIBRE/ScienceRuns/L0050N1504/Thermal_Ppivot1p5e4_npivot1p0/snapshots/colibre_0048/colibre_0048.hdf5',
    'gcs_snip': '/cosma8/data/dp004/jlvc76/COLIBRE/ScienceRuns/L0050N1504/Thermal_Ppivot1p5e4_npivot1p0/snapshots/colibre_0047/colibre_0047.hdf5',
}

def get_sw_name(name: str) -> str:
    """
    Convert a CamelCase property name to snake_case, matching the
    convention used by swiftsimio.
    """
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()

compression_description = {
    "FMantissa9": "$1.36693{\\rm{}e}10 \\rightarrow{} 1.367{\\rm{}e}10$",
    "FMantissa13": "$1.36693{\\rm{}e}10 \\rightarrow{} 1.3669{\\rm{}e}10$",
    "DMantissa9": "$1.36693{\\rm{}e}10 \\rightarrow{} 1.367{\\rm{}e}10$",
    "DMantissa21": "$1.3669345{\\rm{}e}10 \\rightarrow{} 1.36693{\\rm{}e}10$",
    "DScale6": "1 pc accurate",
    "DScale5": "10 pc accurate",
    "DScale1": "0.1 km/s accurate",
    "Nbit40": "Store less bits",
    "None": "no compression",
}


def format_units(attrs):
    """
    Return an RST-formatted unit string for the give attributres
    """

    snap_units = {
        "snap_mass":        "(1e10*Msun)",
        "snap_length":      "Mpc",
        "snap_time":        "(s*Mpc/km)",
        "snap_temperature": "K",
    }

    prop_unit = ''

    if attrs["U_M exponent"][0] != 0:
        prop_unit += f'{snap_units["snap_mass"]}**{attrs["U_M exponent"][0]}'
    if attrs["U_L exponent"][0] != 0:
        if prop_unit:
            prop_unit += ' * '
        prop_unit += f'{snap_units["snap_length"]}**{attrs["U_L exponent"][0]}'
    if attrs["U_t exponent"][0] != 0:
        if prop_unit:
            prop_unit += ' * '
        prop_unit += f'{snap_units["snap_time"]}**{attrs["U_t exponent"][0]}'
    if attrs["U_T exponent"][0] != 0:
        if prop_unit:
            prop_unit += ' * '
        prop_unit += f'{snap_units["snap_temperature"]}**{attrs["U_T exponent"][0]}'

    units = unyt.unyt_quantity(1, units=prop_unit)
    latex = (
        units.units.latex_repr
        .replace("\\rm{km} \\cdot \\rm{kpc}", "\\rm{kpc} \\cdot \\rm{km}")
        .replace("\\frac{\\rm{km}^{2}}{\\rm{s}^{2}}", "\\rm{km}^{2} / \\rm{s}^{2}")
        .replace(r"1.0 \times ", "")
        .rstrip()
    )

    output_physical = attrs["Value stored as physical"][0] == 1
    a_exponent = attrs["a-scale exponent"][0]
    if (not output_physical) and a_exponent:
        a_str = "a" if a_exponent == 1 else f"a^{{{a_exponent}}}"
        latex = f"{a_str} \\cdot {latex}" if latex else a_str

    if not latex or (latex == "dimensionless"):
        return "dimensionless"
    return f":math:`{latex}`"

def get_compression(attrs):
    compression_filter = attrs['Lossy compression filter'].decode()
    compression = compression_description[compression_filter]
    if '$' in compression:
        return f":math:`{compression.replace("$", "")}`"
    return compression

def get_desc(name, attrs):
    if name in corrections:
        return corrections[name]
    desc = attrs['Description']
    try:
        desc = desc.decode()
    except:
        pass
    return desc

def get_table_header():
    header = f'.. list-table::\n'
    header += f'   :header-rows: 1\n\n'
    header += '   * - Name\n'
    header += '     - Description\n'
    header += '     - Snipshot\n'
    return header

rst_page = """.. _snapshot_particle_properties:

Particle properties
===================

This page documents all of the properties which are stored for each
type of particle in a COLIBRE snapshot. The first column in each table gives the
name of the property when opened using the swiftsimio library.
Clicking on each property name will open a dropdown box,
which contains information about the dataset within the HDF5 file.
The second column gives a description of the property. Certain
properties also contain a link to a footnote at the bottom of this page
The final column indicates whether the property is present in both
snapshots and snipshots.

.. note:: Units are provided here for information, but it's usually
          better to use the metadata in the files for any unit
          conversions. The `swiftsimio
          <https://swiftsimio.readthedocs.io/en/latest/loading_data/index.html>`__
          python module handles units automatically in snapshots and
          SOAP halo catalogues.

The runs with hybrid AGN feedback and globular clusters contain
additional properties not present the the standard thermal AGN runs.
These properties are listed in a separate tables.

"""


for ptype, ptype_name in [
        (1, 'Dark matter'),
        (0, 'Gas'),
        (4, 'Star'),
        (5, 'Black hole'),
    ]:

    # Add section title 
    title = f'{ptype_name} particles'
    rst_page += f'{title}\n{"-"*len(title)}\n\n'

    prop_info = {}
    # Loop through all properties in snapshot and extract description
    for snap_type, filename in snapshots.items():
        prop_info[snap_type] = {}
        names, descs = [], []
        with h5py.File(filename, 'r') as file:
            for name in file[f'PartType{ptype}'].keys():
                attrs = dict(file[f'PartType{ptype}/{name}'].attrs)
                if len(file[f'PartType{ptype}/{name}'].shape) == 1:
                    shape = 1
                else:
                    shape = file[f'PartType{ptype}/{name}'].shape[1]
                dtype = str(file[f'PartType{ptype}/{name}'].dtype)
                compression = get_compression(attrs)
                units = format_units(attrs)
                prop_info[snap_type][name] = {
                    'desc': get_desc(name, attrs),
                    'compression': compression,
                    'units': units,
                    'shape': shape,
                    'sw_name': get_sw_name(name),
                    'dtype': dtype,
                }

    # Add properties to table (checking if present in snipshot)
    rst_page += get_table_header()
    for name, prop_attrs in prop_info['thermal'].items():
        rst_page += f'   * - .. dropdown:: ``{prop_attrs["sw_name"]}``\n\n'
        rst_page += f'          * **HDF5 name:** ``{name}``\n'
        rst_page += f'          * **Shape:** {prop_attrs["shape"]}\n'
        rst_page += f'          * **Datatype:** {prop_attrs["dtype"]}\n'
        rst_page += f'          * **Units:** {prop_attrs["units"]}\n'
        rst_page += f'          * **Compression:** {prop_attrs["compression"]}\n'
        rst_page += f'     - {prop_attrs["desc"]}\n'
        in_snip = r"✅" if name in prop_info['snip'] else r"❌"
        rst_page += f'     - {in_snip}\n'
    rst_page += '\n\n'

    # Add hybrid properties to table
    if ptype in [0, 4, 5]:
        title = f'Hybrid properties'
        rst_page += f'{title}\n{"~"*len(title)}\n\n'
        rst_page += get_table_header()
        for name, prop_attrs in prop_info['hybrid'].items():
            if name in prop_info['thermal']:
                continue
            rst_page += f'   * - .. dropdown:: ``{prop_attrs["sw_name"]}``\n\n'
            rst_page += f'          * **HDF5 name:** ``{name}``\n'
            rst_page += f'          * **Shape:** {prop_attrs["shape"]}\n'
            rst_page += f'          * **Datatype:** {prop_attrs["dtype"]}\n'
            rst_page += f'          * **Units:** {prop_attrs["units"]}\n'
            rst_page += f'          * **Compression:** {prop_attrs["compression"]}\n'
            rst_page += f'     - {prop_attrs["desc"]}\n'
            in_snip = r"✅" if name in prop_info['snip'] else r"❌"
            rst_page += f'     - {in_snip}\n'
        rst_page += '\n\n'

    # Add globular cluster properties
    if ptype in [4]:
        title = f'Globular cluster properties'
        rst_page += f'{title}\n{"~"*len(title)}\n\n'
        rst_page += get_table_header()
        for name, prop_attrs in prop_info['gcs'].items():
            if name in prop_info['thermal']:
                continue
            rst_page += f'   * - .. dropdown:: ``{prop_attrs["sw_name"]}``\n\n'
            rst_page += f'          * **HDF5 name:** ``{name}``\n'
            rst_page += f'          * **Shape:** {prop_attrs["shape"]}\n'
            rst_page += f'          * **Datatype:** {prop_attrs["dtype"]}\n'
            rst_page += f'          * **Units:** {prop_attrs["units"]}\n'
            rst_page += f'          * **Compression:** {prop_attrs["compression"]}\n'
            rst_page += f'     - {prop_attrs["desc"]}\n'
            in_snip = r"✅" if name in prop_info['gcs_snip'] else r"❌"
            rst_page += f'     - {in_snip}\n'
        rst_page += '\n\n'


# Add section title 
title = f'Footnotes'
rst_page += f'{title}\n{"-"*len(title)}\n\n'

rst_page += r"""
.. _footnote_averaged:

Averaged quantities
~~~~~~~~~~~~~~~~~~~

Averaged quantities are calculated by accumulating 
the quantity over the 10 Myr/100 Myr that precedes the writing of a 
snapshot, and then normalizing. For example, for SFR, we start a clock 
precisely 10 Myr before a snapshot dump, accumulate SFR * dt at each 
step during that window, and then divide by 10 Myr at the point of writing.
AveragedStarFormationRates for star particles should not be used.

.. _dust-names:

Dust fractions
~~~~~~~~~~~~~~

The ``DustMassFractions`` dataset contains the following species.

+-------------+---------------------+
| Array index | Species name        |
+=============+=====================+
| 0           | GraphiteLarge       |
+-------------+---------------------+
| 1           | GraphiteSmall       |
+-------------+---------------------+
| 2           | MgSilicatesLarge    |
+-------------+---------------------+
| 3           | MgSilicatesSmall    |
+-------------+---------------------+
| 4           | FeSilicatesLarge    |
+-------------+---------------------+
| 5           | FeSilicatesSmall    |
+-------------+---------------------+

.. _element-names:

Element fractions
~~~~~~~~~~~~~~~~~

The ``ElementMassFractions`` and ``ElementMassFractionsDiffuse``
datasets contain the following elements.

+-------------+---------------------+
| Array index | Element name        |
+=============+=====================+
| 0           | Hydrogen            |
+-------------+---------------------+
| 1           | Helium              |
+-------------+---------------------+
| 2           | Carbon              |
+-------------+---------------------+
| 3           | Nitrogen            |
+-------------+---------------------+
| 4           | Oxygen              |
+-------------+---------------------+
| 5           | Neon                |
+-------------+---------------------+
| 6           | Magnesium           |
+-------------+---------------------+
| 7           | Silicon             |
+-------------+---------------------+
| 8           | Iron                |
+-------------+---------------------+
| 9           | Strontium           |
+-------------+---------------------+
| 10          | Barium              |
+-------------+---------------------+
| 11          | Europium            |
+-------------+---------------------+

The ``ReducedElementMassFractions`` dataset contains the following elements.

+-------------+---------------------+
| Array index | Element name        |
+=============+=====================+
| 0           | Hydrogen            |
+-------------+---------------------+
| 1           | Helium              |
+-------------+---------------------+

.. _species-names:

Species fractions
~~~~~~~~~~~~~~~~~

The ``SpeciesFractions`` dataset contains the following species.
Note that the fraction of species i in this dataset is defined 
in terms of its number density relative to hydrogen (i.e.
:math:`n_i` / :math:`n_{H_{tot}}`), which is not the same as the mass fraction.

+-------------+---------------------+
| Array index | Species name        |
+=============+=====================+
| 0           | Electron            |
+-------------+---------------------+
| 1           | HI                  |
+-------------+---------------------+
| 2           | HII                 |
+-------------+---------------------+
| 3           | Hm                  |
+-------------+---------------------+
| 4           | HeI                 |
+-------------+---------------------+
| 5           | HeII                |
+-------------+---------------------+
| 6           | HeIII               |
+-------------+---------------------+
| 7           | H2                  |
+-------------+---------------------+
| 8           | H2p                 |
+-------------+---------------------+
| 9           | H3p                 |
+-------------+---------------------+

The ``ReducedSpeciesFractions`` dataset contains the following elements.

+-------------+---------------------+
| Array index | Species name        |
+=============+=====================+
| 0           | HI                  |
+-------------+---------------------+
| 1           | HeI                 |
+-------------+---------------------+
| 2           | HeII                |
+-------------+---------------------+
| 3           | H2                  |
+-------------+---------------------+

.. _xray-bands:

X-ray bands
~~~~~~~~~~~

Gas particles have ``XrayLuminosities`` (energy per unit time) and
``XrayPhotonLuminosities`` (number of photons per unit time) datasets
which contain data for three different observer frame X-ray bands:

+-------------+---------------------+
| Array index | Band                |
+=============+=====================+
| 0           | eROSITA 0.2-2.3keV  |
+-------------+---------------------+
| 1           | eROSITA 2.3-8.0keV  |
+-------------+---------------------+
| 2           | ROSAT 0.5-2.0keV    |
+-------------+---------------------+

.. _luminosities:

Stellar luminosities
~~~~~~~~~~~~~~~~~~~~

.. warning:: Star particle "luminosities" are stored in terms of flux
             and do NOT use the same units as the X-ray luminosity
             datasets described above.

Star particles have a ``Luminosities`` dataset. For each particle and
photometric band this contains the rest frame flux at 10pc, expressed
in maggies. Maggies are a dimensionless measure of flux defined as the
ratio :math:`F/F_0`, where :math:`F_0=3631\mathrm{Jy}` is the flux
corresponding to an AB magnitude of zero. Dust extinction is not
included. These were computed using the `BC03
<https://ui.adsabs.harvard.edu/abs/2003MNRAS.344.1000B/abstract>`_
(GALAXEV) models convolved with the different filter bands, as used in
the dust-free modelling of `Trayford et al. (2015)
<https://ui.adsabs.harvard.edu/abs/2015MNRAS.452.2879T/abstract>`_.

The rest frame, absolute AB-magnitude can be computed as:

  :math:`M = -2.5 \log10(L)`

where ``L`` is the dimensionless number stored in the
dataset. Luminosities for the `GAMA <https://www.gama-survey.org/>`__
bands are stored in the following order:

+-------------+---------------------+
| Array index | Band                |
+=============+=====================+
| 0           | u                   |
+-------------+---------------------+
| 1           | g                   |
+-------------+---------------------+
| 2           | r                   |
+-------------+---------------------+
| 3           | i                   |
+-------------+---------------------+
| 4           | z                   |
+-------------+---------------------+
| 5           | Y                   |
+-------------+---------------------+
| 6           | J                   |
+-------------+---------------------+
| 7           | H                   |
+-------------+---------------------+
| 8           | K                   |
+-------------+---------------------+

.. _hii_end_time:

HII regions end time
~~~~~~~~~~~~~~~~~~~~

This property was originally not enabled to be output, and so is completely missing
from certain runs, is only available for low redshift outputs of other runs.

"""


print(rst_page)

