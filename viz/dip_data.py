import sqlite3
import numpy as np

class DipData:
    def __init__(self, db_filename: str):
        con = sqlite3.connect(db_filename)
        cursor = con.cursor()

        query = 'SELECT * FROM dip;'
        data = cursor.execute(query).fetchall()

        self.addr = [t[0] for t in data]
        self.instr_type = [t[1] for t in data]

        self.base = np.array([t[2] for t in data])
        self.fe_stall = np.array([t[3] for t in data])
        self.be_stall = np.array([t[4] for t in data])
        self.mispred = np.array([t[5] for t in data])

class Dip:
    def __init__(self, _type, addr,
                 base, fe_stall, be_stall, mispred):
        self.instr = _type + ' | ' + addr[-2:]
        self.base = float(base)
        self.fe_stall = float(fe_stall)
        self.be_stall = float(be_stall)
        self.mispred = float(mispred)
