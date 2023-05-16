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

class BuildingHouseError(Exception):
    def __str__(self):
        return 'щось не те, дуже багато і дорого'

def check_material_build(amount, limit):
    if amount > limit:
        return 'Достатньо матеріалів!'
    else:
        raise BuildingHouseError()
print(check_material_build(9,10))
