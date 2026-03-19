# Viz Python Scripts

## Runnable scripts

### `plot-hot.py`
Plots the top `n` hottest instructions from a DIP database.

Usage:

```bash
python plot-hot.py <db_file> -n <amount> -t <title>
```

Arguments:

- `<db_file>`: path to SQLite database (required)
- `-n, --amount`: number of hottest dips to plot (required in practice)
- `-t, --title`: plot title; also used as output filename in `out/` (required in practice)

Example:

```bash
python plot-hot.py data/dip.db -n 5 -t loopbench
```

Output file:

- `out/<title>`

### `save-dip.py`
Exports the top `n` hottest instructions from the DB to a `;`-separated CSV-like file.

Usage:

```bash
python save-dip.py <db_file> -n <amount> -f <file>
```

Arguments:

- `<db_file>`: path to SQLite database (required)
- `-n, --amount`: number of rows to export (required in practice)
- `-f, --file`: output file path (required in practice)

Example:

```bash
python save-dip.py data/dip.db -n 10 -f csv/MIP.csv
```

### `read-dip.py`
Reads `csv/MIP.csv` and generates a fixed plot.

Usage:

```bash
python read-dip.py
```

Notes:

- Input is currently hardcoded to `csv/MIP.csv`.
- Output is currently hardcoded to `out/MIM_ITER`.

## Library/helper files

### `dip_data.py`
Data model and loader for DIP data.

- `DipData(db_filename)`: reads `dip` table from SQLite DB into arrays.
- `Dip(...)`: single DIP record used by plotting/export.

### `hottest_dip.py`
Selects top entries.

- `n_hottest_dips(n, data)`: returns a list of top `n` `Dip` objects by total stack height.

### `plot_stacks.py`
Stacked bar plotting utility.

- `plot_dips(dip, title, save_file)`: plots list of `Dip` objects and writes image to `save_file`.

### `utils.py`
Small numeric helper.

- `index_nth_largest(a, n)`: index of the `n`th largest value in array `a`.
