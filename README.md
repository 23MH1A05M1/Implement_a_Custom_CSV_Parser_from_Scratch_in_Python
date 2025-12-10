# Custom CSV Parser and Generator in Python

This project includes a minimal CSV parser and writer created entirely with Python, without using the built-in `csv` module.  
A benchmarking script is also provided to measure the performance of this custom approach compared to Python’s standard CSV tools.

## Repository Structure

- `custom_csv_reader.py` — Implements the class responsible for manually reading CSV files  
- `custom_csv_writer.py` — Implements the class used to write CSV files  
- `benchmark.py` — Runs performance tests against Python’s built-in CSV reader and writer  
- `README.md` — Documentation  
- `requirements.txt` — Uses only Python’s standard library  

## Overview of Components

### CustomCsvReader
- Processes CSV files row by row  
- Supports:
  - Quoted fields  
  - Escaped quotes  
  - Multi-line entries  
- Implements Python’s iterator protocol using `__iter__` and `__next__`

### CustomCsvWriter
- Converts lists of values into a valid CSV line  
- Automatically adds quotes for fields containing:
  - Commas  
  - Quotes  
  - Newline characters  
- Escapes internal quotation marks correctly

## Usage Examples

### Reading a CSV File
```python
from custom_csv_reader import CustomCsvReader

reader = CustomCsvReader("data.csv")
for row in reader:
    print(row)
```

### Writing a CSV File
```python
from custom_csv_writer import CustomCsvWriter

rows = [
    ["Name", "Age"],
    ["Alice", "30"],
    ["Bob", "25"]
]

writer = CustomCsvWriter("output.csv")
writer.write_all(rows)
```

## Benchmarking

Run the benchmark script with:

```bash
python benchmark.py
```

### Sample Output (10,000 rows × 5 columns)

Reader:
- CustomCsvReader: 0.3032 seconds  
- Built-in csv.reader: 0.0224 seconds  

Writer:
- CustomCsvWriter: 0.2455 seconds  
- Built-in csv.writer: 0.2823 seconds  

## Interpretation of Results

- The built-in CSV reader performs much faster because it is implemented in C.  
- The custom reader is slower but correctly handles complex CSV features such as multi-line and quoted fields.  
- The custom writer shows competitive performance and was slightly faster in the benchmark dataset.

## Summary

This project demonstrates how CSV parsing and writing can be implemented manually using basic Python.  
It highlights low-level CSV handling, escaping rules, file operations, and includes a performance comparison with standard library tools.  
You can modify or extend the reader and writer depending on your project requirements.
