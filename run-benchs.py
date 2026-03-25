#!/usr/bin/python3
import subprocess
import sys
from pathlib import Path
 
BENCHMARKS = [
    "CCa", "CCe", "CCh", "CCh_st", "CCl", "CCm", "CF1",
    "CRd", "CRf", "CRm", "CS1", "CS3",
    "DP1d", "DP1f", "DPcvt", "DPT", "DPTd",
    "ED1", "EF", "EI", "EM1", "EM5",
    "MC", "MCS", "MD", "M_Dyn", "MI", "MIM", "MIM2", "MIP",
    "ML2", "ML2_BW_ld", "ML2_BW_ldst", "ML2_BW_st", "ML2_st",
    "MM", "MM_st",
    "STc", "STL2", "STL2b",
]
 
DB_DIR = Path("VOP_verslag/db_noop")
PLOT_SCRIPT = "VOP_verslag/viz/plot-hot.py"


def run(cmd, bench_name):
    """Run a shell command, printing it first. Exit on failure."""
    print(f"  $ {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"  [ERROR] Command failed with return code {result.returncode}", file=sys.stderr)
        return False
    return True
 
 
def main():
    DB_DIR.mkdir(parents=True, exist_ok=True)
 
    failed = []
 
    for bench in BENCHMARKS:
        print(f"\n{'='*60}")
        print(f"  Benchmark: {bench}")
        print(f"{'='*60}")
 
        db_path = DB_DIR / f"{bench}.sqlite3"
 
        # Step 1: Run the simulator
        ok = run(["./run-roi.sh", f"microbench/{bench}/bench"], bench)
        if not ok:
            failed.append((bench, "run-roi.sh"))
            continue
 
        # Step 2: Move the output database
        ok = run(["mv", "out/sim.stats.sqlite3", str(db_path)], bench)
        if not ok:
            failed.append((bench, "mv"))
            continue
 
        # Step 3: Generate the heatmap plot
        ok = run(
            ["python3", PLOT_SCRIPT, str(db_path), "-n", "5", "-t", bench],
            bench,
        )
        if not ok:
            failed.append((bench, "plot-hot.py"))
            continue
 
        print(f"  [OK] {bench} done.")
 
    print(f"\n{'='*60}")
    if failed:
        print(f"Finished with {len(failed)} failure(s):")
        for bench, step in failed:
            print(f"  - {bench}: failed at '{step}'")
        sys.exit(1)
    else:
        print(f"All {len(BENCHMARKS)} benchmarks completed successfully.")
 
 
if __name__ == "__main__":
    main()
