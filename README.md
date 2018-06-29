# Complex System Simulations

##### By Mirjam Bruinsma, Maarten van de Ende, Nigel van den Ende and Thomas van der Veen

__[link to private repository](https://github.com/nigelvanherwijnen/complexsystemsimulation)__
__[link to public presentation](https://nigelvanherwijnen.github.io/complexsystemsimulation/)___

This repository is used during the course Complex System Simulations at the University of Amsterdam in June 2018.

All libraries used during this project can be found in `requirements.txt`.

## File structure
The main graph object can be found in `network.py` in the root directory. This object holds all functions to perform all iterations. This is done for a great number of different systems, which are stored as pickle-file in either `pickles_for_animations/` or `pickles_for_plots/`, depending on what the saved object was used for. The files used to create the figures can be found in the `diagrams/` folder.

## Reproduce figures
In order to reproduce the figures used in the presentation, run `main.py`. This will run the functions found in the modules in `diagrams/`, which will then be shown to the user.

Reproducing the figures can be done in a matter of seconds or minutes, depending on how fast the 3D-animation is rendered. Reproducing the graph objects that were computed will take a number of days to compute. Note that this is not necessary for reproducing the figures, because the objects have been included in this repository.

One of the figures updates an online Plotly figure, which can be found __[here](https://plot.ly/~mirbruin/0)__. The only figure not being created by running `main.py` is the interactive Plotly figure of the graph, because this figure is created for use in Jupyter Notebook. The code needed to recreate this figure can be found in `diagrams/draw_nice_graphs.ipynb`.

## Presentation
The presentation as performed during the final lecture can be found in `Presentation.ipynb`. Run `jupyter nbconvert Presentation.ipynb --to slides --post serve` to render the presentation.
