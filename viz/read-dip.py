from plot_stacks import plot_dips
from dip_data import Dip

from csv import reader

def read_and_plot(filepath: str):
    dips = []

    with open(filepath, 'r') as infile:
        r = reader(infile, delimiter=';')
        for row in r:
            dips.append(Dip("", "    ", row[1], row[2], row[3], row[4]))
            dips[-1].instr = row[0]

    plot_dips(dips, "MIM: 2, 4, 8 ITER", 'out/MIM_ITER')


if __name__ == '__main__':
    read_and_plot('csv/MIP.csv')
