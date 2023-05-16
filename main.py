#3
class InvalidFileFormatError(Exception):
    def __init__(self, filename):
        self.filename = filename

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print('File contain: ', content)
    except IOError:
        raise InvalidFileFormatError(filename)
try:
    read_file(input('Name of file: '))
except InvalidFileFormatError as e:
    print(f'Wrong format of file {e.filename}, supporting only .txt files')