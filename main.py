#2
class InvalidPasswordError(Exception):
    def __init__(self, password):
        self.password = password
        super().__init__('Invalid password')

def validate_password(password):
    if len(password) < 8 or not any(char.isdigit() for char in password):
        raise InvalidPasswordError

try:
    password = input('Введіть пароль: ')
    validate_password(password)
    print('Пароль відповідає вимогам.')
except InvalidPasswordError as e:
    print('Пароль не відповідає вимогам.')