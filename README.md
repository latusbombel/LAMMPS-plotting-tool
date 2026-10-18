# Materials Data Plotter

A modular command-line tool for visualizing materials science and chemistry simulation data. It supports plotting Radial Distribution Functions (RDF), X-Ray Diffraction (XRD) patterns, and interaction potentials directly from the terminal.

## Features
* **Multi-format Support:** Quickly plot `.rdf`, `.xrd`, and `.pot` files.
* **Modular Architecture:** Built with an Object-Oriented design using an abstract `DataSource` base class (`plot.py`), making it simple to add new file formats without changing the core logic.
* **Customizable Axes:** Clip axes and add custom titles directly via CLI flags.
* **Simultaneous Plotting:** Plot multiple files of the same or different formats on the same axes.

## Requirements
* Python 3.x
* `numpy`
* `matplotlib`

## Installation
The `myplots` executor script is explicitly configured to look for its source modules in a `~/mytools` directory.

1. Clone this repository:
   ```bash
   git clone [https://github.com/latusbombel/LAMMPS-plotting-tool.git](https://github.com/latusbombel/LAMMPS-plotting-tool.git)
   cd YOUR_REPOSITORY_NAME
Install the required Python dependencies:

Bash
pip install numpy matplotlib
Create the tools directory and copy the source modules:

Bash
mkdir -p ~/mytools
cp plot.py plot_potential.py plot_rdf.py plot_xrd.py ~/mytools/
Make the executor script executable and move it to your local binary path:

Bash
chmod +x myplots
mv myplots ~/.local/bin/
(Note: Ensure ~/.local/bin is added to your system's $PATH)

Usage
Run the myplots command followed by the corresponding data format flag and your file paths.

Available Flags
Data Loading:

-rdf FILE [FILE ...]: Load and plot Radial Distribution Function data.

-xrd FILE [FILE ...]: Load and plot X-Ray Diffraction data.

-pot FILE [FILE ...]: Load and plot Interaction Potential data.

Plot Configuration:

-title "TEXT": Set the overall plot title.

-xtitle "TEXT" / -ytitle "TEXT": Set custom axis labels.

-x0 VAL / -xcut VAL: Set the minimum and maximum X-axis limits.

-y0 VAL / -ycut VAL: Set the minimum and maximum Y-axis limits.

Examples
Plot a single XRD file:

Bash
myplots -xrd sample.xrd
Plot multiple RDF files with a custom title:

Bash
myplots -rdf system1.rdf system2.rdf -title "RDF Comparison"
Plot Potential data and restrict the axes:

Bash
myplots -pot interaction.txt -x0 1.0 -xcut 5.0 -y0 -10.0 -ycut 10.0
