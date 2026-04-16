# Source - https://stackoverflow.com/a
# Posted by Andras Deak -- Слава Україні, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-16, License - CC BY-SA 4.0

import numpy as np
from mayavi import mlab
from tvtk.api import tvtk # python wrappers for the C++ vtk ecosystem

boxsize = 1000.0
shell_radii = np.asarray([ 110.28034967,  323.74707781,  533.47608886,  737.88616873,
                           936.93161437, 1130.5995746 , 1318.90693547, 1501.89694379,
                           1679.63573267, 1852.20889111, 2019.71816755, 2182.27838873,
                           2340.01464167, 2493.05974369, 2641.55200841, 2785.63330491,
                           2925.44739533, 3061.13853317, 3192.85029551, 3320.72462868,
                           3444.90107806, 3565.51618201, 3682.70300628, 3796.59079081,
                           3907.30470367, 4014.9656809 , 4119.6903266 , 4221.59087162,
                           4320.77518663, 4417.34682442, 4511.40509122, 4603.0451394 ,
                           4692.35808217, 4779.43111858, 4864.34766428, 4947.18749134,
                           5028.02686726, 5106.93869772, 5183.99267013, 5259.25539387,
                           5332.79053612, 5404.6589559 , 5474.91883745, 5543.62581158,
                           5610.83307895, 5676.5915288 , 5740.94984538, 5803.95461583,
                           5865.65043506, 5926.08000386, 5985.28421479, 6043.30224357,
                           6100.17163283, 6155.92837429, 6210.60697991, 6264.24055424,
                           6316.86086185, 6368.49839205, 6419.18242355, 6468.94107628])


def draw_cube(offset, scale):

    # Cube vertices
    pts = np.array([
        [0, 0, 0],  # 0
        [1, 0, 0],  # 1
        [1, 1, 0],  # 2
        [0, 1, 0],  # 3
        [0, 0, 1],  # 4
        [1, 0, 1],  # 5
        [1, 1, 1],  # 6
        [0, 1, 1],  # 7
    ], dtype=float)

    pts *= scale
    pts += np.asarray(offset)[None,:]

    # Edges defined by vertex index pairs
    edges = [
        (0,1), (1,2), (2,3), (3,0),   # bottom square
        (4,5), (5,6), (6,7), (7,4),   # top square
        (0,4), (1,5), (2,6), (3,7)    # vertical edges
    ]

    # Draw edges
    for i, j in edges:
        mlab.plot3d(
            [pts[i,0], pts[j,0]],
            [pts[i,1], pts[j,1]],
            [pts[i,2], pts[j,2]],
            tube_radius=None,  # makes it a line instead of a tube
            color=(1,1,1)
        )


def auto_sphere():
    # create a figure window (and scene)
    fig = mlab.figure(size=(600, 600), bgcolor=(1,1,1))

    for shell_nr in range(10):

        radius = shell_radii[shell_nr]

        # load and map the texture
        img = tvtk.PNGReader()
        img.file_name = f'./images/shell_{shell_nr}.png'
        texture = tvtk.Texture(input_connection=img.output_port, interpolate=1)
        # (interpolate for a less raster appearance when zoomed in)

        # use a TexturedSphereSource, a.k.a. getting our hands dirty
        R = 1
        Nrad = 180

        # create the sphere source with a given radius and angular resolution
        sphere = tvtk.TexturedSphereSource(radius=radius, theta_resolution=Nrad,
                                           phi_resolution=Nrad)

        # Clip the sphere
        box = tvtk.Box()
        box.bounds = (0.0, 10000.0,
                      0.0, 10000.0,
                      0.0, 10000.0)

        clipper = tvtk.ClipPolyData(
            input_connection=sphere.output_port,
            clip_function=box,
        )

        # assemble rest of the pipeline, assign texture
        sphere_mapper = tvtk.PolyDataMapper(input_connection=clipper.output_port)
        sphere_actor = tvtk.Actor(mapper=sphere_mapper, texture=texture)

        # Set the tint color (RGB in 0–1 range)
        f = ((shell_nr+1) / 10.0) * 0.9 + 0.1
        sphere_actor.property.color = (f, f, f) # light red tint

        fig.scene.add_actor(sphere_actor)

    # Draw box replications
    #for i in range(0,2):
    #    for j in range(0,2):
    #        for k in range(0,2):
    #            draw_cube((i*1000,j*1000,k*1000), 1000.0)

    return fig


if __name__ == "__main__":
    fig = auto_sphere()
    mlab.view(azimuth=50, elevation=30, roll=0, distance=8000)
    mlab.savefig("sphere.png", figure=fig)
    mlab.show()
