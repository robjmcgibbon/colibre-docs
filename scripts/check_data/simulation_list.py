#!/bin/env/python

L1_m9 = [
    "L1_m9",
    "fgas+2σ",
    "fgas-2σ",
    "fgas-4σ",
    "fgas-8σ",
    "M*-1σ",
    "M*-1σ_fgas-4σ",
    "Jet",
    "Jet_fgas-4σ",
    "Planck",
    "PlanckNu0p24Var",
    "PlanckNu0p24Fix",
    "PlanckNu0p48Fix",
    "LS8",
    "PlanckDCDM12",
    "PlanckDCDM24",
    "LS8_fgas-8σ",
    "NoCooling",
]

L1_m9_DMO = [
    "L1_m9_DMO",
    "Planck_DMO",
    "PlanckNu0p12Var_DMO",
    "PlanckNu0p24Var_DMO",
    "PlanckNu0p24Fix_DMO",
    "PlanckNu0p48Fix_DMO",
    "LS8_DMO",
    "PlanckDCDM12_DMO",
    "PlanckDCDM24_DMO",
]

# Snapshots where we expect to have full particle data
L1_m9_snapshots = {
  9  : 5.00,
  13 : 4.00,
  17 : 3.00,
  37 : 2.00,
  47 : 1.50,
  57 : 1.00,
  62 : 0.75,
  67 : 0.50,
  69 : 0.40,
  71 : 0.30,
  73 : 0.20,
  75 : 0.10,
  77 : 0.00,
}

# Snapshots where we expect to have full particle data
L1_m8_snapshots = {
  10  : 5.00,
  14 : 4.00,
  18 : 3.00,
  38 : 2.00,
  48 : 1.50,
  58 : 1.00,
  63 : 0.75,
  68 : 0.50,
  70 : 0.40,
  72 : 0.30,
  74 : 0.20,
  76 : 0.10,
  78 : 0.00,
}


sim_params = [
    # L1_m8 runs
    {
        "box"            : "L1_m8",
        "names"          : ["L1_m8", "L1_m8_DMO"],
        "nr_snaps"       : 79,
        "expected_snaps" : L1_m8_snapshots
    },
    # L1_m10 runs
    {
       "box"            : "L1_m10",
       "names"          : ["L1_m10", "L1_m10_DMO"],
       "nr_snaps"       : 78,
       "expected_snaps" : L1_m9_snapshots
    },
    # L2p8_m9 runs
    {
        "box"            : "L2p8_m9",
        "names"          : ["L2p8_m9", "L2p8_m9_DMO"],
        "nr_snaps"       : 79,
        "expected_snaps" : L1_m8_snapshots
    },
    # L1_m9 hydro runs
    {
        "box"            : "L1_m9",
        "names"          : L1_m9,
        "nr_snaps"       : 78,
        "expected_snaps" : L1_m9_snapshots
    },
    # L1_m9 DMO runs
    {
        "box"            : "L1_m9",
        "names"          : L1_m9_DMO,
        "nr_snaps"       : 78,
        "expected_snaps" : L1_m9_snapshots
    },
    # L5p6_m10 runs
    {
        "box"            : "L5p6_m10",
        "names"          : ["L5p6_m10_DMO"],
        "nr_snaps"       : 79,
        "expected_snaps" : L1_m8_snapshots
    },
    # L11p2_m11 runs
    {
        "box"            : "L11p2_m11",
        "names"          : ["L11p2_m11_DMO"],
        "nr_snaps"       : 79,
        "expected_snaps" : L1_m8_snapshots
    },
]
