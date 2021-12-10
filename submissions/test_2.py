def Sum(*args):
   sum = 0
   for arg in args:
       sum += arg
   return sum
def Multiply(*args):
   result = 1
   for arg in args:
       result *= arg
   return result
def fibonacci(n):
   if n in (1, 2):
       return 1
   return fibonacci(n - 1) + fibonacci(n - 2)