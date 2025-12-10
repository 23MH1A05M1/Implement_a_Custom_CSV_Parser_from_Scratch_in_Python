class CustomCsvWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_all(self, rows):
        """
        Writes a list of rows to the CSV file.
        Each row should be a list of string values.
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            for row in rows:
                file.write(",".join(row) + "\n")

    def append_row(self, row):
        """
        Appends a single row to the CSV file.
        'row' should be a list of string values.
        """
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(",".join(row) + "\n")