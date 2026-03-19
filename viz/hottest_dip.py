from dip_data import DipData, Dip
from utils import index_nth_largest

import numpy as np

def n_hottest_dips(n: int, data: DipData):

    total = data.base + data.fe_stall + data.be_stall + data.mispred

    # First is index for the highest stack, second for the second highest...
    index = [index_nth_largest(total, 1+i) for i in range(min(n, len(data.instr_type)))]

    top = [
        Dip(data.instr_type[i],
         data.addr[i],
         data.base[i],
         data.fe_stall[i],
         data.be_stall[i],
         data.mispred[i]
        )
        for i in index
    ]

    return top



