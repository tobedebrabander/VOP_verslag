from dip_data import Dip

import matplotlib.pyplot as plt
import numpy as np


def plot_dips(dip, title, save_file):
    if type(dip) != list:
        raise ValueError("plot_dips: dips to be plot should be in a Python list")

    fig, ax = plt.subplots()
    width = 0.4

    bottom = np.zeros(len(dip))

    instr = tuple(d.instr for d in dip)
    state_counts = {
        'Base': np.array([d.base for d in dip]),
        'Front end': np.array([d.fe_stall for d in dip]),
        'Back end': np.array([d.be_stall for d in dip]),
        'Misprediction': np.array([d.mispred for d in dip])
    }

    for state, counts in state_counts.items():
        p = ax.bar(instr, counts, width, label=state, bottom=bottom)
        bottom += counts

        labels = [f"{value:g}" if not np.isclose(value, 0.0) else "" for value in counts]
        ax.bar_label(p, labels=labels, label_type='center')

    ax.set_title(title)
    ax.legend()
    fig.savefig(save_file)


