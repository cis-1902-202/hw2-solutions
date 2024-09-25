import os
import unittest

from csv2 import BaseCSV, CSVEditor


class TestBaseCSV(unittest.TestCase):
    def setUp(self):
        self.file = open("tempfile", "w", newline="")
        self.file.write("header1,header2\nvalue1,value2\nvalue3,value4\n")
        self.file.close()

    def tearDown(self):
        os.remove("tempfile")

    def test_initialization(self):
        csv = BaseCSV(self.file.name)
        self.assertEqual(csv.headers, ["header1", "header2"])
        self.assertEqual(csv.rows, [["value1", "value2"], ["value3", "value4"]])

    def test_from_template(self):
        csv = BaseCSV.from_template(
            "tempfile2", ["header1", "header2"], [["value1", "value2"]]
        )
        self.assertEqual(csv.headers, ["header1", "header2"])
        self.assertEqual(csv.rows, [["value1", "value2"]])
        os.remove("tempfile2")

    def test_validate_row(self):
        self.assertTrue(BaseCSV.validate_row(["value1", "value2"], 2))
        self.assertFalse(BaseCSV.validate_row(["value1"], 2))

    def test_get_headers(self):
        csv = BaseCSV(self.file.name)
        self.assertEqual(csv.get_headers(), ["header1", "header2"])

    def test_str(self):
        csv = BaseCSV(self.file.name)
        expected_str = "header1,header2\nvalue1,value2\nvalue3,value4"
        self.assertEqual(str(csv), expected_str)


class TestCSVEditor(unittest.TestCase):
    def setUp(self):
        self.file = open("tempfile", "w", newline="")
        self.file.write("header1,header2\nvalue1,value2\nvalue3,value4\n")
        self.file.close()

    def tearDown(self):
        os.remove("tempfile")

    def test_getitem(self):
        csv_editor = CSVEditor("tempfile")
        self.assertEqual(csv_editor[0], ["value1", "value2"])

    def test_setitem(self):
        csv_editor = CSVEditor("tempfile")
        csv_editor[0] = ["new_value1", "new_value2"]
        self.assertEqual(csv_editor[0], ["new_value1", "new_value2"])

    def test_setitem_invalid(self):
        csv_editor = CSVEditor("tempfile")
        with self.assertRaises(ValueError):
            csv_editor[0] = ["new_value1"]  # Wrong length

    def test_delitem(self):
        csv_editor = CSVEditor("tempfile")
        del csv_editor[1]
        self.assertEqual(len(csv_editor.rows), 1)

    def test_get_column(self):
        csv_editor = CSVEditor("tempfile")
        self.assertEqual(csv_editor.get_column("header1"), ["value1", "value3"])

    def test_get_column_invalid(self):
        csv_editor = CSVEditor("tempfile")
        with self.assertRaises(ValueError):
            csv_editor.get_column("nonexistent_header")

    def test_sort_by_column(self):
        csv_editor = CSVEditor("tempfile")
        csv_editor.sort_by_column("header1")
        self.assertEqual(csv_editor.rows, [["value1", "value2"], ["value3", "value4"]])

    def test_filter_by_value(self):
        csv_editor = CSVEditor("tempfile")
        filtered = csv_editor.filter_by_value("header1", "value1")
        self.assertEqual(filtered, [["value1", "value2"]])

    def test_head(self):
        csv_editor = CSVEditor("tempfile")
        self.assertEqual(csv_editor.head(1), [["value1", "value2"]])

    def test_tail(self):
        csv_editor = CSVEditor("tempfile")
        self.assertEqual(csv_editor.tail(1), [["value3", "value4"]])

    def test_chain_rows(self):
        csv_editor = CSVEditor("tempfile")
        self.assertEqual(
            csv_editor.chain_rows(), ["value1", "value2", "value3", "value4"]
        )

    def test_edit(self):
        csv_editor = CSVEditor("tempfile")
        csv_editor.edit(0, 0, "edited_value")
        self.assertEqual(csv_editor[0], ["edited_value", "value2"])


if __name__ == "__main__":
    unittest.main()
