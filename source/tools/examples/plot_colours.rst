:orphan:

COLIBRE colour scheme
=====================

The following are the colours that are used for each resolution for the plots in the COLIBRE overview and calibration papers.
You can use them if you would like to be consistent, but also feel free to pick your own colours.

When comparing thermal and hybrid AGN models at multiple resolutions, we typically use colour to indicate the resolution level
and linestyle to distinguish between models (thermal or hybrid) at fixed resolution.

.. code-block:: python

    import matplotlib.pyplot as plt
    import matplotlib.patheffects as pe

    COLIBRE_COLORS = [
        ('m5', '#C4E8FF'),
        ('m6', '#FF9F6E'),
        ('m7', '#D12424'),
    ]
    PATH_EFFECTS = [pe.Stroke(linewidth=5, foreground="k"), pe.Normal()]
    LINE_WIDTH = 3.5

    fig, ax = plt.subplots(1, figsize=(8, 4))
    for i, (resolution, color_code) in enumerate(COLIBRE_COLORS):
        ax.plot(
            [0, 1],
            [i, i],
            label=resolution,
            color=color_code,
            lw=LINE_WIDTH,
            path_effects=PATH_EFFECTS
        )
    ax.set_ylim(-0.3, 2.5)
    ax.legend(ncol=3, loc='upper center')
    ax.axis('off')
    plt.savefig('colibre_colors.pdf')
    plt.close()

