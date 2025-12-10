class CustomCsvReader:
    """
    A custom CSV reader that supports:
    - Comma-separated fields
    - Quoted fields
    - Escaped quotes ("")
    - Newlines inside quoted fields
    - Streaming (line-by-line) reading
    """

    def __init__(self, filename, encoding="utf-8"):
        self.filename = filename
        self.file = open(filename, "r", encoding=encoding)
        self.buffer = ""
        self.eof = False

    def __iter__(self):
        """Return iterator (required for for-loops)."""
        return self

    def __next__(self):
        """Return the next parsed row or stop iteration."""
        row = self._read_row()
        if row is None:
            self.file.close()
            raise StopIteration
        return row

    def _read_row(self):
        """Parses a single CSV row and returns a list of fields."""
        row = []
        field = ""
        in_quotes = False

        while True:
            char = self.file.read(1)

            # EOF reached
            if char == "":
                if field or row:
                    row.append(field)
                    return row
                return None

            if char == '"':
                if in_quotes:
                    next_char = self.file.read(1)
                    if next_char == '"':  # Escaped quote
                        field += '"'
                    else:
                        in_quotes = False
                        if next_char:
                            char = next_char
                        else:
                            continue
                else:
                    in_quotes = True
                    continue

            if char == "," and not in_quotes:
                row.append(field)
                field = ""
                continue

            if char == "\n" and not in_quotes:
                row.append(field)
                return row

            field += char

    def close(self):
        self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.file.close()