import csv

from os import listdir


class FileWorker:

    def __init__(self, folder_path: str, file_headers: list):
        """
        :param folder_path: path to source folder
        :param file_headers: output file headers
        """
        self.__folder_path = folder_path
        self.__file_headers = file_headers

    def get_file_names(self):
        """
        Gets list filenames from source folder
        :return: list of csv filenames
        """
        return listdir(self.__folder_path)

    def csv_reader(self, file: str):
        """
        Gets data from csv file
        :param file: string, filename
        :return: generator of rows in file
        """
        with open(self.__folder_path + '/' + file, newline='') as csvfile:
            return (row for row in list(csv.DictReader(csvfile)))

    def write_headers(self, file_path: str):
        """
        Write headers to output file
        :param file_path: string, path to output file
        :return: None
        """
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, self.__file_headers)
            writer.writeheader()

    def write_data(self, file_path: str, data: list):
        """
        Write data to output file
        :param file_path: output file path
        :param data: list of dicts to write
        :return: None
        """
        with open(file_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, self.__file_headers)
            writer.writerows(data)
