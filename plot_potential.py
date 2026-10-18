#!/usr/bin/env python3
import sys
import os
import numpy as np
from plot import DataSource

class POT_data(DataSource):
    spec = {
        'flag':"-pot",
        'nargs':"+",
        'metavar': "FILE",
        'help':"Potential file path",
        'xlabel': r'R [$\AA$]',
        'ylabel':"E[eV]"
    }

    def load(self, filepath: str):
        blocks = []
        current_block = None
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                
                # Skip empty lines
                if not line:
                    continue
                    
                # 1. Check for the 'N 123' metadata line
                if line.startswith('N '):
                    if current_block is not None:
                        # Extract the number after 'N '
                        current_block['N'] = int(line.split()[1])
                    continue
                    
                # 2. Check if the line is numeric data
                parts = line.split()
                try:
                    # If the first part is a number, this succeeds
                    float(parts[0]) 
                    
                    # If it succeeds, it's a data row. Save it to the current block.
                    if current_block is not None:
                        # Convert all items in the row to floats
                        row_data = [float(x) for x in parts]
                        current_block['data'].append(row_data)
                        
                except ValueError:
                    # 3. If it's NOT a number and NOT 'N ', it must be a new text header
                    
                    # Save the previous block before starting a new one
                    if current_block is not None:
                        blocks.append(current_block)
                    
                    # Initialize a new block
                    current_block = {
                        'name': line,
                        'N': 0,
                        'data': []
                    }
                    
            # Don't forget to append the very last block after the loop finishes
            if current_block is not None:
                blocks.append(current_block)
    
            # Convert the lists to NumPy arrays to make plotting easier
            for block in blocks:
                block['data'] = np.array(block['data'])
        
        return blocks

    def get_series(self, data: dict, filepath: str):
        x = data[0]['data'][:,1]

        series = []
        for block in data:

            label = f"{block['name']} ({os.path.basename(filepath)})"
            y = block['data'][:,2]

            series.append((x, y, label))

        return series

