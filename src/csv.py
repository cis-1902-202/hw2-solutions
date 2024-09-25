# PART 2 (Part 1 is the `calculator` module)


class BaseCSV:
    default_delimiter = ","  # Class variable

    def __init__(self, filepath, mode="r", delimiter=None):
        """
        Sets up object and actually reads the content of the CSV file.
        """
        # TODO: (5 pts)
        # make sure to check if filepath actually exists (look at `os` module)
        # you also probably want to keep headers and content separate
        ...
        self._read_file()

    def _read_file(self):
        """
        Helper method to read the content of the CSV file.
        """
        # TODO: (5 pts)
        pass

    @classmethod
    def from_template(cls, filepath, headers, data):
        """
        Create a new CSV file from a template. (This should depend
        on your `__init__` method.)
        """
        # TODO: (5 pts)
        ...
        return cls(filepath)

    @staticmethod
    def validate_row(row, headers_length):
        """
        What makes a row valid?
        """
        # TODO: (5 pts)
        pass

    def get_headers(self):
        """
        Retrieves the headers of the CSV file.
        """
        # TODO: fairly simple method, but I want it to be cached
        # so that it doesn't have to be recalculated every time
        # HINT: check out the `functools` module
        # (5 pts)
        pass

    def __str__(self):
        """
        Returns a string representation of the CSV file.
        """
        # TODO: (5 pts)
        pass


class CSVEditor(BaseCSV):
    def __getitem__(self, index):
        """
        Retrieves a row from the CSV file.
        """
        # TODO: (2 pts)
        pass

    def __setitem__(self, index, value):
        """
        Sets a row in the CSV file. (remember to validate!)
        """
        # TODO: (5 pts)
        pass

    def __delitem__(self, index):
        """
        Deletes a row from the CSV file.
        """
        # TODO: (2 pts)
        pass

    def get_column(self, column_name):
        """
        Retrieves all values from a column.
        """
        # TODO: (5 pts)
        pass

    def sort_by_column(self, column_name, func=None, reverse=False):
        """
        Sorts the CSV rows based off its column data.

        The `func` argument should be the lambda func used to sort the data.
        """
        # TODO: (5 pts)
        pass

    def filter_by_value(self, column_name, value):
        """
        Retrieves all rows that have a specific value in a column.
        """
        # TODO: (5 pts)
        pass

    def head(self, n=5):
        """
        Retrieves the first `n` rows of the CSV file.
        """
        # TODO: (2 pts)
        pass

    def tail(self, n=5):
        """
        Retrieves the last `n` rows of the CSV file.
        """
        # TODO: (2 pts)
        pass

    def chain_rows(self):
        """
        Chains all rows together into a single list.
        """
        # TODO: (5 pts)
        # HINT: check out the `itertools` module
        pass

    def save(self, output_filepath=None):
        """
        Saves the CSV file to a new location. If no location is provided,
        uses the original file.
        """
        # TODO: (5 pts)
        # again, make sure to validate the filepath
        ...

    def edit(self, row_index, col_index, value):
        """
        Edits a specific cell in the CSV file.
        """
        # TODO: (5 pts)
        pass
