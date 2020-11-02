from app.models.FileWorker import FileWorker
from app.models.DataWorker import DataWorker
from config import *


def main():
    file_worker = FileWorker(SOURCE_FOLDER_PATH, OUTPUT_FILE_HEADERS)
    data_worker = DataWorker()
    file_worker.write_headers(OUTPUT_FILE_PATH)
    files = file_worker.get_file_names()
    new_file = []

    for file in files:
        row_generator = file_worker.csv_reader(file)
        while True:
            try:
                row = data_worker.transform_data(next(row_generator))
                new_file.append(row)
            except StopIteration as e:
                break

            if len(new_file) >= MAX_WRITE_BUFFER:
                file_worker.write_data(OUTPUT_FILE_PATH, new_file)
                new_file = []

    if len(new_file) > 0:
        file_worker.write_data(OUTPUT_FILE_PATH, new_file)


if __name__ == '__main__':
    main()
