import utility
import exponents.pow_of
from utility1 import *
# old way
# import exponents.extra_function.modulo_fun
# new way
from exponents.extra_function import modulo_fun

# use alias
import unnecessary_long_module_name as long_module

num1 = 21
num2 = 3

print(utility.sum_fun(num1, num2))
print(utility.divide_fun(num1, num2))

print(divide_fun1(num1, num2))

print(exponents.extra_function.modulo_fun.modulo_fn(num1, num2))

print(long_module.greet('ValMar'))