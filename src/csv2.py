# PART 2 (Part 1 is the `calculator` module)

import itertools
import os
from functools import lru_cache


class BaseCSV:
    default_delimiter = ","  # Class variable

    def __init__(self, filepath, mode="r", delimiter=None):
        # check filepath exists
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        self.filepath = filepath
        self.mode = mode
        self.delimiter = delimiter if delimiter else self.default_delimiter
        self.headers = []
        self.rows = []
        self._read_file()

    def _read_file(self):
        with open(self.filepath, self.mode) as f:
            content = f.read().splitlines()

        if content:
            self.headers = content[0].split(self.delimiter)
            self.rows = [line.split(self.delimiter) for line in content[1:]]

    @classmethod
    def from_template(cls, filepath, headers, data):
        with open(filepath, "w") as f:
            f.write(cls.default_delimiter.join(headers) + "\n")
            for row in data:
                f.write(cls.default_delimiter.join(row) + "\n")
        return cls(filepath)

    @staticmethod
    def validate_row(row, headers_length):
        return len(row) == headers_length

    # this @lru_cache is fairly useless right here
    @lru_cache
    def get_headers(self):
        return self.headers

    # if you took this last approach, this is where you would put the @lru_cache
    # @lru_cache
    # def get_headers(self):
    #   with open(self.filepath, self.mode) as f:
    #       content = f.read().splitlines()
    #   if content:
    #       return content[0].split(self.delimiter)
    #  return []

    def __str__(self):
        csv_content = [self.delimiter.join(self.headers)]
        csv_content.extend([self.delimiter.join(row) for row in self.rows])
        return "\n".join(csv_content)


class CSVEditor(BaseCSV):
    def __getitem__(self, index):
        return self.rows[index]

    def __setitem__(self, index, value):
        if isinstance(value, list) and BaseCSV.validate_row(value, len(self.headers)):
            self.rows[index] = value
        else:
            raise ValueError("Value must be a list matching the number of headers")

    def __delitem__(self, index):
        del self.rows[index]

    def get_column(self, column_name):
        if column_name not in self.headers:
            raise ValueError(f"Column {column_name} not found.")
        col_index = self.headers.index(column_name)
        return [row[col_index] for row in self.rows]

    def sort_by_column(self, column_name, reverse=False):
        if column_name not in self.headers:
            raise ValueError(f"Column {column_name} not found.")
        col_index = self.headers.index(column_name)
        self.rows.sort(key=lambda row: row[col_index], reverse=reverse)

    def filter_by_value(self, column_name, value):
        if column_name not in self.headers:
            raise ValueError(f"Column {column_name} not found.")
        col_index = self.headers.index(column_name)
        return [row for row in self.rows if row[col_index] == value]

    def head(self, n=5):
        return self.rows[:n]

    def tail(self, n=5):
        return self.rows[-n:]

    def chain_rows(self):
        return list(itertools.chain.from_iterable(self.rows))

    def save(self, output_filepath=None):
        if output_filepath is None:
            output_filepath = self.filepath

        # ensure the output directory exists
        output_dir = os.path.dirname(output_filepath)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        content = [self.delimiter.join(self.headers)]
        content.extend([self.delimiter.join(row) for row in self.rows])
        content_str = "\n".join(content)

        with open(output_filepath, "w") as f:
            f.write(content_str)

    def edit(self, row_index, col_index, value):
        if row_index >= len(self.rows) or col_index >= len(self.headers):
            raise IndexError("Row or column index out of range")
        self.rows[row_index][col_index] = value
