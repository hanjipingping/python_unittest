from configparser import ConfigParser
from common.handle_path import Con_path
import os


class Conf(ConfigParser):
    def __init__(self, file_name, encoding='utf-8'):
        super().__init__()
        self.file_name = file_name
        self.encoding = encoding
        self.read(file_name, encoding=encoding)

    def write_data(self, section, option, value):
        self.set(section, option, value)
        self.write(fp=open(self.file_name, "w", encoding=self.encoding))


if __name__ == '__main__':
    cs = Conf(os.path.join(Con_path, "con.ini"))
    print(cs.sections())
    cs.write_data("other", "age", "18")
