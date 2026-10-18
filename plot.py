import argparse
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import itertools
from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def load(self, filepath: str) -> np.array:
        ...

    @abstractmethod
    def get_series(self, data: np.ndarray, filepath: str) -> list[tuple[np.ndarray, np.ndarray, str]]:
        ...

tools_dir = os.path.expanduser("~/mytools")
sys.path.append(tools_dir)

class Plotter():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Plot specific data formats.")
        
        self.register = {}
        self.passed_data = []
        self._files_count = 0

        self._linestyles = itertools.cycle(['solid', 'dashed', 'dotted', 'dashdot'])

        self.fig, self.ax = plt.subplots(figsize = (12,8))

    def _plot_setting(self):
        if self.args.x0 is not None or self.args.xcut is not None:
            self.ax.set_xlim(left=self.args.x0, right=self.args.xcut)
            self.ax.relim()
            self.ax.autoscale_view(scalex=True, scaley=True)
            
        if self.args.y0 is not None or self.args.ycut is not None:
            self.ax.set_ylim(bottom=self.args.y0, top=self.args.ycut)
            self.ax.relim()
            self.ax.autoscale_view(scalex=True, scaley=True)

        if self.args.title is not None:
            self.ax.set_title(self.args.title)
        if self.args.xtitle is not None:
            self.ax.set_xlabel(self.args.xtitle)
        if self.args.ytitle is not None:
            self.ax.set_ylabel(self.args.ytitle)

        self.ax.legend()
        plt.grid(True)

    def parse_args(self, *data_types: DataSource):
        for data_type in data_types:
            self.register[data_type.spec['flag']] = data_type
        for flag, data_type in self.register.items():
                self.parser.add_argument(flag,  
                                        nargs = data_type.spec['nargs'], 
                                        metavar = data_type.spec['metavar'], 
                                        help = data_type.spec['help'])

        self.parser.add_argument("-x0", type=float, help="Sets start of x axis")
        self.parser.add_argument("-xcut", type=float, help="Sets lim of x axis")
        self.parser.add_argument("-y0", type=float, help="Sets start of y axis")
        self.parser.add_argument("-ycut", type=float, help="Sets limit of y axis")

        self.parser.add_argument("-title", type=str, help="Sets title of plot")
        self.parser.add_argument("-xtitle", type=str, help="Sets title of x axis")
        self.parser.add_argument("-ytitle", type=str, help="Sets title of y axis")
        
        self.args = self.parser.parse_args()
        
    def _load_data(self):
        all_data = []
        for flag, data_type in self.register.items():
            attr_name = flag.lstrip('-')
            file_list = getattr(self.args, attr_name)
            if file_list is None:
                continue

            if 'xlabel' in data_type.spec:
                self.ax.set_xlabel(data_type.spec['xlabel'])
            if 'ylabel' in data_type.spec:
                self.ax.set_ylabel(data_type.spec['ylabel'])

            for path in file_list:
                try:
                    self._files_count += 1
                    style = next(self._linestyles)
                    data = data_type.load(path)
                    series_list = data_type.get_series(data, path)
                    all_data.extend(
                        (x, y, label, style) for x, y, label in series_list
                    )
                except Exception as e:
                    print(f"Error in procesing {flag} file: {e}", file=sys.stderr)
                    sys.exit(1)
        return all_data

    def _plot(self):
        all_data = self._load_data()
        for x, y, label, style in all_data:
            self.ax.plot(x, y, label = label, linestyle = style)

        self._plot_setting()
    
    def run(self):
        self._plot()
        plt.show()