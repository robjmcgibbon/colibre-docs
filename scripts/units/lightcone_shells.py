import numpy as np
import h5py

table_header = """\
.. list-table::
   :header-rows: 1
   :stub-columns: 0

   * - Shell index
     - Inner redshift
     - Outer redshift"""

# f-string to make a row in an RST list table
row_template = """\
   * - {shell_nr}
     - {z_min:.3f}
     - {z_max:.3f}"""


# Read redshifts
redshift_file = "/cosma8/data/dp004/flamingo/Runs/L11200N5040/DMO_FIDUCIAL/shell_redshifts.txt"
redshift_data = np.loadtxt(redshift_file, delimiter=",")
z_min = redshift_data[:,0]
z_max = redshift_data[:,1]

## Read comoving distances
#index_file = "/cosma8/data/dp004/flamingo/Runs/L2800N5040/HYDRO_FIDUCIAL/neutrino_corrected_maps_downsampled_4096/lightcone0_index.hdf5"
#with h5py.File(index_file, "r") as f:
#    r_min = f["Lightcone"].attrs["shell_inner_radii"]
#    r_max = f["Lightcone"].attrs["shell_outer_radii"]


# Make a table
print(table_header)
for i in range(len(z_min)):
    print(row_template.format(shell_nr=i,
                              z_min=z_min[i],
                              z_max=z_max[i]))
