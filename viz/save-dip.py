from dip_data import Dip, DipData
from hottest_dip import n_hottest_dips

from csv import writer
import argparse


def save_dip(dip: Dip, file_path: str):
    with open(file_path, 'a') as outfile:
        w = writer(outfile, delimiter=';')
        w.writerow([
            dip.instr,
            dip.base,
            dip.fe_stall,
            dip.be_stall,
            dip.mispred
        ])
        outfile.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('db_file')
    parser.add_argument('-n', '--amount')
    parser.add_argument('-f', '--file')

    args = parser.parse_args()
    data = DipData(args.db_file)

    for dip in n_hottest_dips(int(args.amount), data):
        save_dip(dip, args.file)

