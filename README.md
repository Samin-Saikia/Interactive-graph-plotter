 # Interactive Graph Plotter
*A simple Python application for plotting mathematical equations interactively*

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Customization & Extensibility](#customization--extensibility)
- [Troubleshooting](#troubleshooting)


## Overview
The Interactive Graph Plotter is a lightweight Python application that allows users to input mathematical equations and visualize them interactively. This project uses `sympy` for symbolic mathematics, `numpy` for numerical computations, and `plotly` for creating interactive graphs.

## Features
| ✅ | Feature |
|---|---------|
| ✅ | Input any valid mathematical expression in terms of `x` |
| ✅ | Interactive Plotly graph (pan, zoom, hover) |
| ✅ | Graph opens automatically in the default browser |
| ✅ | Simple, cross-platform UI (Tkinter) |
| ✅ | Works with Python 3.7.6 (no newer-only syntax) |
| ✅ | Zero external binary dependencies – pure-Python wheels only |

## Demo
To see the Interactive Graph Plotter in action:

1. Clone or download the repository.
2. Run the application using Python 3.7.6 or later.
3. Enter a mathematical expression in the text box (e.g., `x**2 + 3*x - 4`).
4. Click the "Plot" button to visualize the equation.

## Installation

### Prerequisites
- Python 3.7.6 or later
- `sympy`, `numpy`, and `plotly` libraries

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Samin-Saikia/interactive-graph-plotter.git
   cd interactive-graph-plotter
   ```
2. Install the required packages:
   ```bash
   pip install sympy numpy plotly
   ```

## Usage
1. Run the application:
   ```bash
   python plotter.py
   ```
2. Enter a mathematical expression in the text box.
3. Click the "Plot" button to visualize the equation.

## How It Works
The Interactive Graph Plotter uses the following components:

1. **UI (Tkinter)**: A simple window with a text box, a plot button, and a quit button.
2. **Parsing (SymPy)**: Converts user input into a SymPy expression.
3. **Numerical Evaluation (NumPy)**: Evaluates the expression on a default domain.
4. **Graph Generation (Plotly)**: Creates an interactive graph.

## Customization & Extensibility
Future enhancements could include:

* Supporting multiple equations
* Customizable plot ranges
* Additional mathematical functions

## Troubleshooting
If you encounter issues:

* Ensure you have the required libraries installed.
* Check that your Python version is compatible.

