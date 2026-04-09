from pics_data import PicsData
from plot_stacks import plot_dips
from hottest_pics import n_hottest_pics

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('db_file')
parser.add_argument('-n', '--amount')
parser.add_argument('-t', '--title')

args = parser.parse_args()

data = PicsData(args.db_file)
plot_dips(n_hottest_pics(int(args.amount), data), args.title, 'VOP_verslag/viz/out/' + args.title)
