#!/bin/env python

row_template = """\
   * - {name}
     - `FLAMINGO/L1_m9/{name} </flamingo/viewer.html?path=/FLAMINGO/L1_m9/{name}>`__
     -"""

sims = [
    "fgas+2sigma",
    "fgas-2sigma",
    "fgas-4sigma",
    "fgas-8sigma",
    "Mstar-1sigma",
    "Mstar-1sigma_fgas-4sigma",
    "Jet",
    "Jet_fgas-4sigma",
    "Planck",
    "PlanckNu0p24Var",
    "PlanckNu0p24Fix",
    "PlanckNu0p48Fix",
    "LS8",
    "PlanckDCDM12",
    "PlanckDCDM24",
    "LS8_fgas-8sigma",
    "NoCooling",
]

for name in sims:
    print(row_template.format(name=name))
