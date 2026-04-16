#!/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_observers(L, vertices):

    # Cube centre
    centre = np.array([L/2, L/2, L/2])

    # Observers halfway to each vertex
    observers = (centre + vertices) / 2

    # ---- Plot ----
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')

    # Draw cube edges
    for v in vertices:
        # draw line from centre to vertex
        ax.plot([centre[0], v[0]],
                [centre[1], v[1]],
                [centre[2], v[2]],
                color='gray', linestyle='--', linewidth=0.8)

    # Scatter cube vertices
    #ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2],
    #           s=40, c='black', label="Vertices")

    # Centre point
    ax.scatter(centre[0], centre[1], centre[2],
               s=80, c='red', label="Box centre")

    # Observers
    ax.scatter(observers[:,0], observers[:,1], observers[:,2],
               s=100, c='blue', marker='o', label="Observers")


    # --- Add observer labels ---
    for i, (x, y, z) in enumerate(observers):
        ax.text(x, y, z, f"  {i}", color="black", fontsize=12)

    # Cube bounding box
    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_zlim(0, L)

    ax.set_xlabel('x [Gpc]')
    ax.set_ylabel('y [Gpc]')
    ax.set_zlabel('z [Gpc]')

    ax.legend()


    cube_edges = [
        # bottom face
        [(0,0,0), (L,0,0)],
        [(L,0,0), (L,L,0)],
        [(L,L,0), (0,L,0)],
        [(0,L,0), (0,0,0)],

        # top face
        [(0,0,L), (L,0,L)],
        [(L,0,L), (L,L,L)],
        [(L,L,L), (0,L,L)],
        [(0,L,L), (0,0,L)],

        # vertical lines
        [(0,0,0), (0,0,L)],
        [(L,0,0), (L,0,L)],
        [(L,L,0), (L,L,L)],
        [(0,L,0), (0,L,L)],
    ]

    for (x1,y1,z1), (x2,y2,z2) in cube_edges:
        ax.plot([x1,x2], [y1,y2], [z1,z2],
                color="black", linewidth=1.0)

    ax.view_init(elev=23, azim=280)
    ax.set_aspect("equal")
    plt.tight_layout()

if __name__ == "__main__":

    L = 2.8
    vertices = np.array([[0,0,0],
                         [0,0,L],
                         [0,L,0],
                         [0,L,L],
                         [L,0,0],
                         [L,0,L],
                         [L,L,0],
                         [L,L,L]])
    plot_observers(L, vertices)
    #plt.show()

    plt.savefig("observers_L2p8.png")

    L = 1.0
    vertices = np.array([[L,L,L],
                         [0,0,0]])
    plot_observers(L, vertices)
    plt.savefig("observers_L1.png")
