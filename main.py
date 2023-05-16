class InvalidUsernameError(Exception):
    def __init__(self, username):
        self.username = username
        super().__init__('Invalid username')

#InvalidLengthError
#InvalidCharacterError
#DublicateUsernameError

def register_user(username):
    if len(username) < 5:
        raise InvalidUsernameError(username)

try:
    username = input("Введіть ім'я користувача: ")
    register_user(username)
    print('Реєстрація успішна')
except InvalidUsernameError as e:
    print('Помилка.')
