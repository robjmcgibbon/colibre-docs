#!/bin/env python

row_template = """\
   * - {name}
     - `FLAMINGO/L1_m9/{name} </flamingo/viewer.html?path=/FLAMINGO/L1_m9/{name}>`__
     -"""

sims = [
    "Planck_DMO",
    "PlanckNu0p12Var_DMO",
    "PlanckNu0p24Var_DMO",
    "PlanckNu0p24Fix_DMO",
    "PlanckNu0p48Fix_DMO",
    "LS8_DMO",
    "PlanckDCDM12_DMO",
    "PlanckDCDM24_DMO",
]

for name in sims:
    print(row_template.format(name=name))
