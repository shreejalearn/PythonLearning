# 0, 1, 1, 2, 3, 5, 8, 13, 21... Fibonnaci Numbers

def fib(total):
  num1 = 0
  num2 = 1
  for i in range(total):
    yield num1
    placeholder = num1
    num1 = num2
    num2 = placeholder + num1
    yield num2

for x in fib(20):
  print(x)
