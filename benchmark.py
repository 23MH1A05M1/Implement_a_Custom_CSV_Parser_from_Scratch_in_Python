"""
Benchmark script comparing custom CSV reader & writer with Python's built-in csv module.

Requirements from assignment:
- Generate a synthetic CSV file with at least 10,000 rows × 5 columns.
- Benchmark read and write speed of:
    * CustomCsvReader vs csv.reader
    * CustomCsvWriter vs csv.writer
- Present clear timing results.
"""

import csv
import random
import string
import timeit

from custom_csv_reader import CustomCsvReader
from custom_csv_writer import CustomCsvWriter


DATASET_FILE = "benchmark_data.csv"
OUTPUT_CUSTOM = "output_custom.csv"
OUTPUT_BUILTIN = "output_builtin.csv"


# ------------------------------------------------------
# Helper: Generate synthetic CSV dataset
# ------------------------------------------------------
def generate_dataset(rows=10000, cols=5):
    """
    Generates a dataset with random strings, commas, quotes, and newlines
    to test edge cases.
    """
    print("Generating synthetic dataset...")

    def random_field():
        text = "".join(
            random.choices(string.ascii_letters + string.digits + " ,\"\n", k=12)
        )
        return text

    with open(DATASET_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for _ in range(rows):
            row = [random_field() for _ in range(cols)]
            writer.writerow(row)

    print(f"Dataset created: {DATASET_FILE} ({rows} rows × {cols} cols)")


# ------------------------------------------------------
# Benchmark: Custom Reader
# ------------------------------------------------------
def benchmark_custom_reader():
    reader = CustomCsvReader(DATASET_FILE)
    for _ in reader:
        pass


# ------------------------------------------------------
# Benchmark: Built-in Reader
# ------------------------------------------------------
def benchmark_builtin_reader():
    with open(DATASET_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for _ in reader:
            pass


# ------------------------------------------------------
# Benchmark: Custom Writer
# ------------------------------------------------------
def benchmark_custom_writer():
    rows = []
    with CustomCsvReader(DATASET_FILE) as reader:
        for row in reader:
            rows.append(row)

    writer = CustomCsvWriter(OUTPUT_CUSTOM)
    writer.write_all(rows)


# ------------------------------------------------------
# Benchmark: Built-in Writer
# ------------------------------------------------------
def benchmark_builtin_writer():
    rows = []
    with CustomCsvReader(DATASET_FILE) as reader:
        for row in reader:
            rows.append(row)

    with open(OUTPUT_BUILTIN, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


# ------------------------------------------------------
# Main benchmark runner
# ------------------------------------------------------
def run_benchmarks():
    # Create dataset once
    generate_dataset()

    print("\nRunning benchmarks...\n")

    # Reader benchmarks
    t_custom_read = timeit.timeit(benchmark_custom_reader, number=1)
    t_builtin_read = timeit.timeit(benchmark_builtin_reader, number=1)

    # Writer benchmarks
    t_custom_write = timeit.timeit(benchmark_custom_writer, number=1)
    t_builtin_write = timeit.timeit(benchmark_builtin_writer, number=1)

    # ------------------------------------------------------
    # Show results
    print("===== CSV READER PERFORMANCE =====")
    print(f"CustomCsvReader: {t_custom_read:.4f} seconds")
    print(f"builtin csv.reader: {t_builtin_read:.4f} seconds")

    print("\n===== CSV WRITER PERFORMANCE =====")
    print(f"CustomCsvWriter: {t_custom_write:.4f} seconds")
    print(f"builtin csv.writer: {t_builtin_write:.4f} seconds")

    print("\nBenchmark complete.\n")
    print("You can now include these numbers in your README.md analysis.")


if __name__ == "__main__":
    run_benchmarks()