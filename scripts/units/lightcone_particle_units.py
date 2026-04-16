#!/bin/env python

import h5py

table_header = """\
.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Name
     - Type
     - Shape
     - Units
     - Description"""

# f-string to make a row in an RST list table
row_template = """\
   * - ``{name}``
     - {dtype}
     - {shape}
     - :math:`{units}`
     - {description}"""


def describe_units(group, ref):

    print(table_header)
    for name in group:

        dset = group[name]
        dtype = dset.dtype
        shape = dset.shape
        description = "" #dset.attrs["Description"]
        exponents = {
            "length"      : dset.attrs["U_L exponent"][0],
            "mass"        : dset.attrs["U_M exponent"][0],
            "time"        : dset.attrs["U_t exponent"][0],
            "temperature" : dset.attrs["U_T exponent"][0],
            "current"     : dset.attrs["U_I exponent"][0],
            "a"           : dset.attrs["a-scale exponent"][0],
        }

        # Construct shape string
        if len(shape) == 1:
            shape = "N"
        else:
            shape = "N, "+str(shape[1:]).strip("()").rstrip(",")

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

        # Try to find description
        if ref is not None:
            if name in ref and "Description" in ref[name].attrs:
                description = ref[name].attrs["Description"].decode()

        row = row_template.format(name=name, dtype=str(dtype), shape=shape, units=units, description=description)
        print(row)


if __name__ == "__main__":

    import sys
    filename = sys.argv[1]
    group = sys.argv[2]
    if len(sys.argv) > 3:
        ref = sys.argv[3]
    else:
        ref = None

    if ref is not None:
        ref = h5py.File(ref, "r")[group+"Particles"]

    with h5py.File(filename, "r") as f:
        describe_units(f[group], ref)
