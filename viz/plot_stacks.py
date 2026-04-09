from pics_data import PICS_c

import matplotlib.pyplot as plt
import numpy as np


def plot_dips(pics, title, save_file):
    if type(pics) != list:
        raise ValueError("plot_pics: pics to be plot should be in a Python list")

    fig, ax = plt.subplots()
    width = 0.4

    bottom = np.zeros(len(pics))
    x = np.arange(len(pics))

    instr = tuple(s.instr for s in pics)
    state_counts = {
        'Compute': np.array([s.compute for s in pics]),
        'Drained': np.array([s.drained for s in pics]),
        'Stalled': np.array([s.stalled for s in pics]),
        'Flushed': np.array([s.flushed for s in pics])
    }

    for state, counts in state_counts.items():
        p = ax.bar(x, counts, width, label=state, bottom=bottom)
        bottom += counts

        ax.bar_label(p, label_type='center')

    ax.set_xticks(x, instr)
    ax.set_title(title)
    ax.legend()
    fig.savefig(save_file)


