#!/bin/env python

import h5py

table_header = """\
.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Units
     - Smoothed
     - Description"""

# f-string to make a row in an RST list table
row_template = """\
   * - ``{name}``
     - :math:`{units}`
     - No
     - ?"""


def describe_units(group):

    print(table_header)
    for name in group:

        dset = group[name]
        if not isinstance(dset, h5py.Dataset):
            continue

        exponents = {
            "length"      : dset.attrs["U_L exponent"][0],
            "mass"        : dset.attrs["U_M exponent"][0],
            "time"        : dset.attrs["U_t exponent"][0],
            "temperature" : dset.attrs["U_T exponent"][0],
            "current"     : dset.attrs["U_I exponent"][0],
            "a"           : dset.attrs["a-scale exponent"][0],
        }

        # Construct unit string
        units = ""
        mpc_exponent = exponents["length"] + exponents["time"]
        ttmsun_exponent = exponents["mass"]
        kms_exponent = -exponents["time"]
        k_exponent = exponents["temperature"]
        assert exponents["current"] == 0

        units = ""

        # a
        a_exponent = exponents["a"]
        if a_exponent == 1:
            units += "a"
        elif a_exponent != 0:
            units += "a^{"+f"{a_exponent:g}"+"}"

        # 10^10Msolar
        if ttmsun_exponent == 1:
            units += "10^{10}\mathrm{M}_\odot"
        elif ttmsun_exponent != 0:
            units += "(10^{10}\mathrm{M}_\odot)^{" + f"{ttmsun_exponent:g}" +"}"

        # Megaparsecs
        if mpc_exponent == 1:
            units += "\mathrm{Mpc}"
        elif mpc_exponent != 0:
            units += "\mathrm{Mpc}^{"+f"{mpc_exponent:g}"+"}"

        # km/s
        if kms_exponent == 1:
            units += "\mathrm{km/s}"
        elif kms_exponent != 0:
            units += "\mathrm{(km/s)}^{"+f"{kms_exponent:g}"+"}"

        # K
        if k_exponent == 1:
            units += "\mathrm{K}"
        elif k_exponent != 0:
            units += "\mathrm{K}^{"+f"{k_exponent:g}"+"}"

        if units == "":
            units = "-"

        row = row_template.format(name=name, units=units)
        print(row)


if __name__ == "__main__":

    import sys
    filename = sys.argv[1]

    with h5py.File(filename, "r") as f:
        describe_units(f)
