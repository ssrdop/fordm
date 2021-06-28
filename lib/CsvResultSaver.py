# занимается сохранением переданных ему данных из класса FileManager
# по аналогии с данным классом для сохранения, могут быть и другие классы.
# такие как: TxtResultSaver, XlsxResultSaver и т.д. То есть любой другой предполагаемый формат сохранения
class CsvResultSaver:
	ext = '.csv'

	def save(self, result, save_directory, file_name) -> str:
		# приведение результата в необходимый вид
		data = result
		# и другая работа по сохранению
		# ...

		saved_file_path =  save_directory + file_name + self.ext   # путь до сохраненного файла с результатами (для примера)
		return saved_file_path
