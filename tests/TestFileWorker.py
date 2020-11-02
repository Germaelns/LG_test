import unittest

from app.models.FileWorker import FileWorker


class TestFileWorker(unittest.TestCase):

    def setUp(self) -> None:
        self.file_worker = FileWorker('../files', ['date', 'type', 'amount', 'from', 'to'])

    def test_get_filenames_success(self):
        self.assertEqual(self.file_worker.get_file_names(), ['bank1.csv', 'bank2.csv', 'bank3.csv'])

    def test_get_filenames_is_list(self):
        self.assertIsInstance(self.file_worker.get_file_names(), list)

    def test_csv_reader_not_found(self):
        with self.assertRaises(FileNotFoundError):
            self.file_worker.csv_reader('bank.csv')

    def test_write_headers_success(self):
        with self.assertRaises(FileNotFoundError):
            self.file_worker.csv_reader('bank.csv')


if __name__ == '__main__':
    unittest.main()
