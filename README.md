# Scientific Data CLI Plotter

A flexible, command-line interface (CLI) tool for visualizing scientific data formats (RDF, XRD, and Potential files). Built with Python, NumPy, and Matplotlib.

This project was designed with extensibility in mind. By utilizing an Object-Oriented approach and Abstract Base Classes (ABC), the tool can easily be extended to support entirely new data formats without modifying the core plotting engine.

## Features
* **Multi-Format Support:** Natively parses and plots Radial Distribution Functions (RDF), X-Ray Diffraction (XRD), and Potential energy files.
* **Extensible Architecture:** Uses a `DataSource` interface. Adding a new file type requires just a few lines of code to define a new class.
* **Dynamic CLI:** Command-line arguments are dynamically generated based on the registered data types.
* **Plot Customization:** Supports custom axis limits, titles, and automatic legend generation from parsed file headers.

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/scientific-cli-plotter.git](https://github.com/yourusername/scientific-cli-plotter.git)
   cd scientific-cli-plotter


# Materials Data Plotting CLI

A modular, command-line interface (CLI) tool built in Python for rapidly visualizing materials science and chemistry simulation data, including Radial Distribution Functions (RDF), X-Ray Diffraction (XRD), and interaction potentials.

## Features
* **Modular Architecture**: Built using Object-Oriented principles. New data formats can be easily added by subclassing the abstract `DataSource` base class.
* **Dynamic Argument Parsing**: Automatically registers CLI flags (`-rdf`, `-xrd`, `-pot`) based on the loaded modules.
* **Customizable Visuals**: Supports on-the-fly axis clipping (`-x0`, `-xcut`, `-y0`, `-ycut`) and custom titling directly from the command line.
* **Multi-File Support**: Capable of parsing and plotting multiple files of varying formats on the same axes simultaneously.

## Dependencies
* `numpy`
* `matplotlib`

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/data-plotter-cli.git](https://github.com/YourUsername/data-plotter-cli.git)
   cd data-plotter-cli
