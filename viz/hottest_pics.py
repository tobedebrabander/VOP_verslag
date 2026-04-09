from pics_data import PicsData, PICS_c
from utils import index_nth_largest

def n_hottest_pics(n: int, data: PicsData):

    total = data.compute + data.drained + data.stalled + data.flushed

    # First is index for the highest stack, second for the second highest...
    index = [index_nth_largest(total, 1+i) for i in range(min(n, len(data.instr_type)))]

    top = [
        PICS_c(data.instr_type[i],
         data.addr[i],
         data.compute[i],
         data.drained[i],
         data.stalled[i],
         data.flushed[i]
        )
        for i in index
    ]

    return top



