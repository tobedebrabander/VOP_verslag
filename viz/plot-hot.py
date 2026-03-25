from dip_data import DipData
from plot_stacks import plot_dips
from hottest_dip import n_hottest_dips

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('db_file')
parser.add_argument('-n', '--amount')
parser.add_argument('-t', '--title')

args = parser.parse_args()

data = DipData(args.db_file)
plot_dips(n_hottest_dips(int(args.amount), data), args.title, 'VOP_verslag/viz/out_noop/' + args.title)