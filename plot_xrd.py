#!/usr/bin/env python3
import os
import sys
import numpy as np
from plot import DataSource

def plot_xrd(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            # Skip comments and empty lines
            line = line.strip()
            if line.startswith('#') or not line: 
                continue

class XRD_data(DataSource):
    spec = {
        'flag':"-xrd",
        'nargs':"+",
        'metavar': "FILE",
        'help': "XRD file path",
        'xlabel': r'2$\theta$ [degrees]',
        'ylabel':"Intensity"
    }

    def load(self, filepath: str) -> np.ndarray:
        rows = []
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#') or not line:
                    continue
                parts = line.split()
                if len(parts) > 2:
                    rows.append([float(v) for v in parts])
        rows = np.array(rows)
        rows = rows[rows[:, 1].argsort()]
        return np.array(rows)

    def get_series(self, data, filepath):
        series = []
        x = data[:, 1]
        y = data[:, 2]
        basename = os.path.basename(filepath)
        label = f"{basename}"
        series.append((x, y, label))
        return series