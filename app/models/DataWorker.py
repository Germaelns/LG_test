from datetime import datetime
from config import SUPPORTED_DATE_TYPES
from collections import OrderedDict


class DataWorker:

    def __change_date_format(self, date):
        """
        Convert data to valid format
        :param date: date string to convert
        :return: converted date string
        """
        for date_type in SUPPORTED_DATE_TYPES:
            try:
                return datetime.strptime(date, date_type).strftime('%d %b %Y')
            except Exception as e:
                pass

        return None

    def __check_date(self, data, key, result):
        """
        Check if field is date
        :param data: OrderedDict, data from one row of csv file
        :param key: name of current column
        :param result: list with results transformation
        :return: None
        """
        if any(value in key for value in ['time', 'date']):
            result['date'] = self.__change_date_format(data[key])

    def __check_amount(self, data, key, result):
        """
        Check if field is amount
        :param data: OrderedDict, data from one row of csv file
        :param key: name of current column
        :param result: list with results transformation
        :return: None
        """
        if any(value in key for value in ['amount', 'euro']):
            result['amount'] = float(data[key])

    def __check_type(self, data, key, result):
        """
        Check if field is type of transaction
        :param data: OrderedDict, data from one row of csv file
        :param key: name of current column
        :param result: list with results transformation
        :return: None
        """
        if any(value in key for value in ['type', 'transaction']):
            result['type'] = data[key]

    def __check_cent(self, data, key, result):
        """
        Check if field is cents
        :param data: OrderedDict, data from one row of csv file
        :param key: name of current column
        :param result: list with results transformation
        :return: None
        """

        if 'cent' in key:
            result['amount'] = result['amount'] + float(data[key]) / 100 if result.get('amount') else float(
                data[key]) / 100

    def __check_other(self, data, key, result, other_fields):
        """
        Check if field in other fields
        :param data: OrderedDict, data from one row of csv file
        :param key: name of current column
        :param result: list with results transformation
        :param other_fields: list of other fields
        :return: None
        """
        if any(value in key for value in other_fields):
            result[key] = data[key]

    def transform_data(self, data: OrderedDict):
        """
        Write data to new format
        :param data: OrderedDict, data from one row of csv file
        :return: new dict of given dict
        """
        result = {}
        for key in data.keys():
            self.__check_date(data, key, result)
            self.__check_amount(data, key, result)
            self.__check_cent(data, key, result)
            self.__check_type(data, key, result)
            self.__check_other(data, key, result, ['from', 'to'])
        return result
