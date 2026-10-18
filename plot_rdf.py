#!/usr/bin/env python3
import os
import sys
import numpy as np
from plot import DataSource

class RDF_data(DataSource):
    spec ={
            'flag':"-rdf",
            'nargs':"+",
            'metavar': "FILE",
            'help':"RDF file path",
            'xlabel': r'R [$\AA$]',
            'ylabel':"g(r)"
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
        return np.array(rows)

    def _column_names(self, ncols: int) -> list[str]:
        if ncols == 5:
            return ['AA', 'AB', 'BB']
        elif ncols == 8:
            return ['AA', 'AB', 'AC', 'BB', 'BC', 'CC']
        
        return [f'Col_{j}' for j in range(2, ncols)]

    def get_series(self, data: np.ndarray, filepath: str):
        x = data[:,1]
        names = self._column_names(data.shape[1])
        basename = os.path.basename(filepath)

        series = []
        for i in range(2, data.shape[1]):
            y = data[:, i]
            label = f"{names[i-2]} ({basename})"
            series.append((x, y, label))

        return series