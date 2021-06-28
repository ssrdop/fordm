import os
import sys
from lib.FileManager import FileManager
from lib.CsvResultSaver import CsvResultSaver


# Клиенстий код , который вызывает обработку файла.
# Именно он будет вызываться сторонней программой для передачи аргументов
# и получения пути сохраненного файла, после обработки данных

def get_filename(file_path):
	return os.path.splitext(os.path.basename(file_path))[0]


# блок считывания параметров переданных из стороннего приложения
file_path = sys.argv[1]
save_directory = sys.argv[2]

# вызов менеджера файлов с указанием пути в качестве параметра.
file_manager = FileManager(file_path)

# возвращает результат, читаемый классом по сохранению результата
result = file_manager.manage()

saved_path = CsvResultSaver().save(result, save_directory, get_filename(file_path))

# обязательный вывод
print(saved_path)
