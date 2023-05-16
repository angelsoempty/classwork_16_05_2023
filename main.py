try:
    print('start code')
    print(error)
    print('end')
except:
    print('no problems')
print('any code...')

def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f'Sorry, we cant work with {type(var_1)}, we need class str')
    else:
        return var_1
a = '123'
checker(a)