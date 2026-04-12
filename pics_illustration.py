import argparse
import sqlite3

import matplotlib.pyplot as plt
import numpy as np


def fetch_instruction_rows(db_path: str, count: int = 4):
	"""Fetch instructions present in both pics_d and pics_c."""
	conn = sqlite3.connect(db_path)
	conn.row_factory = sqlite3.Row
	try:
		query = """
			SELECT
				d.addr,
				d.instr_type,
				d.base,
				d.fe_stall,
				d.be_stall,
				d.mispred,
				c.compute,
				c.drained,
				c.stalled,
				c.flushed,
				(d.base + d.fe_stall + d.be_stall + d.mispred) AS total_dispatch
			FROM pics_d d
			INNER JOIN pics_c c
				ON d.addr = c.addr AND d.instr_type = c.instr_type
			WHERE (d.base + d.fe_stall + d.be_stall + d.mispred) > 0
			ORDER BY total_dispatch DESC, d.addr ASC
			LIMIT ?
		"""
		rows = conn.execute(query, (count,)).fetchall()
		if len(rows) < count:
			raise RuntimeError(
				f"Requested {count} instructions, found only {len(rows)} in joined pics_d/pics_c"
			)
		return rows
	finally:
		conn.close()


def plot_pics(rows):
	labels = [f"{row['instr_type']}\n{row['addr']}" for row in rows]
	x = np.arange(len(rows))
	width = 0.5

	dispatch_series = {
		"base": [row["base"] for row in rows],
		"front-end stall": [row["fe_stall"] for row in rows],
		"back-end stall": [row["be_stall"] for row in rows],
		"misprediction": [row["mispred"] for row in rows],
	}

	commit_series = {
		"compute": [row["compute"] for row in rows],
		"drained": [row["drained"] for row in rows],
		"stalled": [row["stalled"] for row in rows],
		"flushed": [row["flushed"] for row in rows],
	}

	fig, (ax_d, ax_c) = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

	bottom = np.zeros(len(rows))
	for name, values in dispatch_series.items():
		vals = np.array(values, dtype=float)
		ax_d.bar(x, vals, width=width, bottom=bottom, label=name)
		for i, v in enumerate(vals):
			if v > 0:
				y = bottom[i] + (v / 2.0)
				ax_d.text(x[i], y, f"{v:.2f}", ha="center", va="center", fontsize=8)
		bottom += vals

	ax_d.set_title("PICS @ dispatch")
	ax_d.set_xticks(x)
	ax_d.set_xticklabels(labels, rotation=20, ha="right")
	ax_d.set_ylabel("Cycles")
	ax_d.legend()
	dispatch_totals = bottom.copy()
	d_max = float(np.max(dispatch_totals)) if len(dispatch_totals) else 0.0
	ax_d.set_ylim(0, d_max * 1.12 if d_max > 0 else 1.0)

	bottom = np.zeros(len(rows))
	for name, values in commit_series.items():
		vals = np.array(values, dtype=float)
		ax_c.bar(x, vals, width=width, bottom=bottom, label=name)
		for i, v in enumerate(vals):
			if v > 0:
				y = bottom[i] + (v / 2.0)
				ax_c.text(x[i], y, f"{v:.2f}", ha="center", va="center", fontsize=8)
		bottom += vals

	ax_c.set_title("PICS @ commit")
	ax_c.set_xticks(x)
	ax_c.set_xticklabels(labels, rotation=20, ha="right")
	ax_c.set_ylabel("Cycles")
	ax_c.legend()
	commit_totals = bottom.copy()
	c_max = float(np.max(commit_totals)) if len(commit_totals) else 0.0
	ax_c.set_ylim(0, c_max * 1.12 if c_max > 0 else 1.0)

	plt.show()


if __name__ == "__main__":
	rows = fetch_instruction_rows('db_tea/CCa.sqlite3', 4)
	plot_pics(rows)
