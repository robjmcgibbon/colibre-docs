#!/bin/env python

import hdfstream
import numpy as np

table_header = """\
.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Name
     - Lightcone nr.
     - All gas max :math:`z`
     - Filtered gas max :math:`z`
     - DM max :math:`z`
     - stars max :math:`z`
     - BH max :math:`z`
     - Neutrino max :math:`z`"""

row_template = """\
   * - ``{name}``
     - {lightcone_nr}
     - {max_z_all_gas}
     - {max_z_filtered_gas}
     - {max_z_dm}
     - {max_z_stars}
     - {max_z_bh}
     - {max_z_nu}"""

root = hdfstream.open("flamingo","/")

print(table_header)

# All fiducial models at different resolutions and boxsize
for res_name in ["L1_m8", "L1_m9", "L2p8_m9", "L1_m10"]:
    for name in root["FLAMINGO/{res_name}".format(res_name=res_name)]:

        # Skip metadata files
        if name in ("description.md", "labels.msgpack"):
            continue
        if res_name not in name:
            continue

        # Skip DMOs for now
        if name.endswith("_DMO"):
            continue

        # Read parameters from one of the files
        attrs = {}
        nr_lightcones = 0
        for lightcone_nr in range(8):
            try:
                # Determine what particle types exist for this lightcone
                index = root[f"FLAMINGO/{res_name}/{name}/particle_lightcones/lightcone{lightcone_nr}_particles/lightcone{lightcone_nr}_0000.0.hdf5"]
                attrs[lightcone_nr] = dict(index["Lightcone"].attrs)
                max_z = {}
                for ptype in ("Gas", "DM", "Stars", "BH", "Neutrino"):
                    if ptype in index:
                        max_z[ptype] = float(attrs[lightcone_nr][f"maximum_redshift_{ptype}"][0])
                    else:
                        max_z[ptype] = "-"

                # Determine maximum redshift for all gas
                if max_z["Gas"] != "-":
                    max_z_all_gas = 0.78 if res_name == "L2p8_m9" else 0.25
                else:
                    max_z_all_gas = "-"

                print(row_template.format(name=name,
                                          lightcone_nr=lightcone_nr,
                                          max_z_all_gas = max_z_all_gas,
                                          max_z_filtered_gas=max_z["Gas"],
                                          max_z_dm=max_z["DM"],
                                          max_z_stars=max_z["Stars"],
                                          max_z_bh=max_z["BH"],
                                          max_z_nu=max_z["Neutrino"],))
                nr_lightcones = lightcone_nr+1
            except KeyError:
                continue


# Repeat for all L1_m9 variations
for name in root["FLAMINGO/L1_m9"]:

    # Skip metadata files
    if name in ("description.md", "labels.msgpack"):
        continue
    # Skip fiducial model
    if "L1_m9" in name :
        continue
    # Skip DMOs for now
    if name.endswith("_DMO"):
        continue

    # Read parameters from one of the files
    attrs = {}
    nr_lightcones = 0
    for lightcone_nr in range(8):
        try:
            # Determine what particle types exist for this lightcone
            index = root[f"FLAMINGO/L1_m9/{name}/particle_lightcones/lightcone{lightcone_nr}_particles/lightcone{lightcone_nr}_0000.0.hdf5"]
            attrs[lightcone_nr] = dict(index["Lightcone"].attrs)
            max_z = {}
            for ptype in ("Gas", "DM", "Stars", "BH", "Neutrino"):
                if ptype in index:
                    max_z[ptype] = float(attrs[lightcone_nr][f"maximum_redshift_{ptype}"][0])
                else:
                    max_z[ptype] = "-"

            # Determine maximum redshift for all gas
            if max_z["Gas"] != "-":
                max_z_all_gas = 0.78 if res_name == "L2p8_m9" else 0.25
            else:
                max_z_all_gas = "-"

            print(row_template.format(name=name,
                                      lightcone_nr=lightcone_nr,
                                      max_z_all_gas = max_z_all_gas,
                                      max_z_filtered_gas=max_z["Gas"],
                                      max_z_dm=max_z["DM"],
                                      max_z_stars=max_z["Stars"],
                                      max_z_bh=max_z["BH"],
                                      max_z_nu=max_z["Neutrino"],))
            nr_lightcones = lightcone_nr+1
        except KeyError:
            continue
