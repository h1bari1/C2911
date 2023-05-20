import warnings

# print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")

# try:
#     try:
#         print('start')
#         print(error)
#         print('No errors')
#     except SyntaxError:
#         print("Wrong errors")
# except (NameError, ZeroDivisionError) as error:
#     print(error)


# except NameError:
#     print("We have an NameError")
# except ZeroDivisionError:
#     print("We have an ZeroDivisionError")

# try:
#     print('start')
#
# except NameError as error:
#     print(error)
# else:
#     print('no problems')
#
# finally:
#     print('Finally code')
#
# print("Next code")

# def checker(a):
#     if type(a) != str:
#         raise TypeError(f"Sorry, we can't work with {type(a)}," f"we need class str")
#     else:
#         return a
#
#
# var = 10
# checker(var)


# class BuildingError(Exception):
#     def __str__(self):
#         return f"With so much material the house cannot be built"
#
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material >= limit_value:
#         return 'enough material'
#     else:
#         raise BuildingError(amount_of_material)
#
#
# materials = 1320
# print(check_material(materials, 300))


# warnings.simplefilter('ignore', SyntaxWarning)
# warnings.simplefilter('error', ImportWarning)
#
# warnings.warn('Warning, no code here', SyntaxWarning)
# try:
#     warnings.warn('Warning, module not import', ImportWarning)
# except:
#     print("warning processed")


