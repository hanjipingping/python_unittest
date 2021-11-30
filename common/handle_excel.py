import openpyxl
from common.handle_path import Data_path
import os


class Excel():
    def __init__(self, file_name, shell):
        self.file_name = file_name
        self.shell = shell

    def open(self):
        self.file = openpyxl.load_workbook(filename=self.file_name)
        self.sheet = self.file[self.shell]

    def read_data(self):
        self.open()
        all_data = list(self.sheet.rows)

        first_data = [i.value for i in all_data[0]]
        dic_data = []
        for j in all_data[1:]:
            other = [k.value for k in j]
            other_data = dict(zip(first_data, other))
            dic_data.append(other_data)
        return dic_data

    def write_data(self, row, column, value):
        """写数据"""
        self.open()
        self.sheet.cell(row=row, column=column, value=value)
        self.file.save(self.file_name)


if __name__ == '__main__':
    ex = Excel(os.path.join(Data_path, "work1.xlsx"), "Sheet1")
    print(ex.read_data())
