import unittest

from app.models.DataWorker import DataWorker
from collections import OrderedDict


class TestDataWorker(unittest.TestCase):

    def setUp(self) -> None:
        self.data_worker = DataWorker()

    def test_transform_data_success(self):
        data = OrderedDict(
            [('timestamp', 'Oct 1 2019'), ('type', 'remove'), ('amount', '99.20'), ('from', '198'), ('to', '182')])
        expected = {'date': '01 Oct 2019', 'type': 'remove', 'amount': 99.2, 'from': '198', 'to': '182'}
        result = self.data_worker.transform_data(data)
        self.assertEqual(result, expected)

    def test_transform_TypeError(self):
        data = OrderedDict(
            [(1, 'Oct 1 2019'), ('type', 'remove'), ('amount', '99.20'), ('from', '198'), ('to', '182')])
        with self.assertRaises(TypeError):
            self.data_worker.transform_data(data)

    def test_transform_result_is_dict(self):
        data = OrderedDict(
            [('timestamp', 'Oct 1 2019'), ('type', 'remove'), ('amount', '99.20'), ('from', '198'), ('to', '182')])
        self.assertIsInstance(self.data_worker.transform_data(data), dict)


if __name__ == '__main__':
    unittest.main()
