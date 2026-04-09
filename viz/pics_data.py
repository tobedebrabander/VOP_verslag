import sqlite3
import numpy as np

class PicsData:
    def __init__(self, db_filename: str):
        con = sqlite3.connect(db_filename)
        cursor = con.cursor()

        query = 'SELECT * FROM pics_c;'
        data = cursor.execute(query).fetchall()

        self.addr = [t[0] for t in data]
        self.instr_type = [t[1] for t in data]

        self.compute = np.array([t[2] for t in data])
        self.drained= np.array([t[3] for t in data])
        self.stalled = np.array([t[4] for t in data])
        self.flushed = np.array([t[5] for t in data])

class PICS_c:
    def __init__(self, _type, addr,
                 compute, drained, stalled, flushed):
        self.instr = _type + ' | ' + addr[-4:]
        self.compute = float(compute)
        self.drained = float(drained)
        self.stalled = float(stalled)
        self.flushed = float(flushed)

