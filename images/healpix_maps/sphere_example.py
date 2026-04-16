# Source - https://stackoverflow.com/a
# Posted by Andras Deak -- Слава Україні, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-16, License - CC BY-SA 4.0

from mayavi import mlab
from tvtk.api import tvtk # python wrappers for the C++ vtk ecosystem

def auto_sphere(image_file):
    # create a figure window (and scene)
    fig = mlab.figure(size=(600, 600))

    # load and map the texture
    img = tvtk.PNGReader()
    img.file_name = image_file
    texture = tvtk.Texture(input_connection=img.output_port, interpolate=1)
    # (interpolate for a less raster appearance when zoomed in)

    # use a TexturedSphereSource, a.k.a. getting our hands dirty
    R = 1
    Nrad = 180

    # create the sphere source with a given radius and angular resolution
    sphere = tvtk.TexturedSphereSource(radius=R, theta_resolution=Nrad,
                                       phi_resolution=Nrad)

    # Clip the sphere
    clipper = tvtk.ClipPolyData(
        input_connection=sphere.output_port,
        clip_function=tvtk.Plane(normal=(1, 0, 0), origin=(0, 0, 0)),
    )

    # assemble rest of the pipeline, assign texture
    sphere_mapper = tvtk.PolyDataMapper(input_connection=clipper.output_port)
    sphere_actor = tvtk.Actor(mapper=sphere_mapper, texture=texture)
    fig.scene.add_actor(sphere_actor)


if __name__ == "__main__":
    image_file = './images/shell_0.png'
    auto_sphere(image_file)
    mlab.show()
