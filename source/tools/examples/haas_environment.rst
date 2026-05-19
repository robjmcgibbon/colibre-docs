:orphan:

Computing Haas+ 2012 environmental measure
==========================================

Example code for computing the environmental measure from `Haas et al. 2012 <https://ui.adsabs.harvard.edu/abs/2012MNRAS.419.2133H/>`__. Thanks to Victor for providing this code.

.. code-block:: python

    import matplotlib.pyplot as plt
    from matplotlib.colors import LogNorm
    import numpy as np
    from scipy.spatial import cKDTree
    import swiftsimio as sw

    # ---------------------------------------------------------
    # Load the SOAP catalogue using swiftsimio
    # ---------------------------------------------------------
    base_dir = "/cosma8/data/dp004/colibre/Runs/"
    run = "L0100N1504/Thermal"
    snap_nr = 127 # z=0
    soap_filename = f"{base_dir}/{run}/SOAP-HBT/halo_properties_{snap_nr:04}.hdf5"
    soap = sw.load(soap_filename)

    # ---------------------------------------------------------
    # Convert everything to consistent physical units and extract the raw numpy values
    # ---------------------------------------------------------
    print("Extracting halo properties...")
    boxsize = soap.metadata.boxsize[0].to_comoving_value("Mpc")
    halo_centre = soap.bound_subhalo.centre_of_mass.to_physical_value("Mpc")
    halo_M200c = soap.spherical_overdensity_200_crit.total_mass.to_physical_value("Msun")
    stellar_mass = soap.exclusive_sphere_50kpc.stellar_mass.to_physical_value("Msun")
    halo_R200c = soap.spherical_overdensity_200_crit.soradius.to_comoving_value("Mpc")

    # ---------------------------------------------------------
    # Filter for Central Halos with nonzero stellar mass
    # ---------------------------------------------------------
    # Spherically overdense properties are not computed for satellites (they are 0).
    # We use this to isolate only the central halos for our tree.
    is_central = (halo_M200c > 0) & (stellar_mass > 0)

    central_centres = halo_centre[is_central]
    central_M200c = halo_M200c[is_central]
    central_R200c = halo_R200c[is_central]

    # ---------------------------------------------------------
    # Compute Haas+ 2012 Environmental Measure
    # ---------------------------------------------------------
    print("Building KDTree for centrals...")
    tree_centrals = cKDTree(central_centres, boxsize=boxsize)

    # Initialize the environmental measure array to -1
    environmental_measure = -np.ones(len(central_centres))

    # We set the halo sample we want to measure to 0
    # (Here, we attempt to compute it for all valid centrals)
    environmental_measure[central_M200c > 0] = 0

    # Define the mass ratio we look for
    mass_ratio_threshold = 0.5

    # Parameters for the search
    max_iteration_number = 30
    nearest_neighbour_lookup = 50

    for iteration in range(max_iteration_number):

        # The halos we still need to measure the environment for in this iteration
        halos_left_to_do = np.flatnonzero(environmental_measure == 0)

        if len(halos_left_to_do) == 0:
            print("All done!")
            break

        print(f"Iteration {iteration+1}: There are {len(halos_left_to_do)} halos left to do.")

        # Ensure we don't query for more neighbours than actually exist in the tree
        k_query = min(1 + nearest_neighbour_lookup, len(central_centres))

        # Query the KDTree
        neighbour_distance, neighbour_index = tree_centrals.query(
            central_centres[halos_left_to_do],
            k=k_query,
        )

        # Remove self (the first neighbour found in a KDTree is always the query point itself)
        neighbour_index = neighbour_index[:, 1:]
        neighbour_distance = neighbour_distance[:, 1:]

        # Get the masses of the neighbours
        neighbour_masses = central_M200c[neighbour_index]

        # Get the masses of the host halos and reshape to allow numpy broadcasting (N, 1)
        host_masses = central_M200c[halos_left_to_do][:, None]

        # Identify neighbours that meet the threshold requirement
        mask_above_threshold = (neighbour_masses / host_masses) >= mass_ratio_threshold

        # Find which halos actually found at least one eligible neighbour in this batch
        mask_halo_to_do_current_iteration = np.sum(mask_above_threshold, axis=1) > 0

        # Locate the index of the *first* True entry in each valid row
        halo_index = np.argmax(mask_above_threshold[mask_halo_to_do_current_iteration], axis=1)

        # Extract the distance to that specific valid neighbour
        distance_to_valid_neighbour = neighbour_distance[mask_halo_to_do_current_iteration, halo_index]

        # Apply the measure (Distance / R200c) to the correct indices in the master array
        valid_host_indices = halos_left_to_do[mask_halo_to_do_current_iteration]
        environmental_measure[valid_host_indices] = distance_to_valid_neighbour / central_R200c[valid_host_indices]

        # Double the search radius for the halos that haven't found a neighbour yet
        nearest_neighbour_lookup *= 2

    print("Computation complete. Environmental measures calculated.")

    # ---------------------------------------------------------
    # Plot result
    # ---------------------------------------------------------

    print("Generating 2D histogram...")

    fig, ax = plt.subplots(1)

    x_bins = 10**np.linspace(0, 2, 30)
    y_bins = 10**np.linspace(10, 15, 30)

    h = ax.hist2d(
        environmental_measure, 
        central_M200c, 
        bins=[x_bins, y_bins], 
        cmap='viridis', 
        norm=LogNorm()
    )

    # Format the axes to match the log bins
    ax.set_xscale('log')
    ax.set_yscale('log')

    # Add labels and colorbar
    fig.colorbar(h[3], label='Number of Halos')
    ax.set_xlabel('Environmental Measure (Distance / R200c)')
    ax.set_ylabel('M200c [Msun]')
    ax.set_title('Haas+ 2012 Environmental Measure vs Halo Mass')

    # Save and display
    plt.savefig('environmental_measure_2dhist.png', dpi=200)
    plt.close()

