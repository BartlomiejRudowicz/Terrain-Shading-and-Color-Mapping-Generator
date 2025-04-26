# Terrain Shading and Color Mapping Generator

This repository contains a Python script designed to visualize terrain elevation data using shading and color mapping. It creates realistic terrain maps by applying lighting effects to elevation data (DEM files).

## Overview

The script reads elevation data from a Digital Elevation Model (DEM) file, computes surface normals, and applies shading based on a simulated light source. The final visualization uses color mapping, translating elevation values into visually intuitive color gradients.

## Features

- **Shaded Relief**: Simulates realistic lighting conditions, enhancing the terrain's visual clarity.
- **HSV to RGB Conversion**: Applies intuitive color gradients based on elevation.
- **Configurable**: Easily adaptable to various DEM datasets.

## Requirements

- Python 3.x
- Matplotlib

Install required libraries using pip:

```bash
pip install matplotlib
```

## Usage

Place your DEM data in a text file (e.g., `big.dem`). Ensure the first line contains width, height, and distance, followed by elevation values.

Run the script from your terminal:

```bash
python script.py
```

This generates an output image:

- `kolorowanie.pdf`: a shaded and colored terrain visualization.

## Example DEM file format (`big.dem`)

```
100 100 30
123.0 124.5 125.0 ...
122.0 123.4 125.6 ...
...
```

## Customization

You can customize lighting direction, color scales, and shading parameters by editing variables in the script:

- **Light Direction**: Adjust `kierunek_swiatla`.
- **Color Mapping**: Modify the `przelicz_kolor` function.

