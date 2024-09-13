def fibonacci(index):
    if index <= 1:
        return index
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)
    
sample = fibonacci(10)

print(sample)

def get_a_factorial(num):
    if num < 2:
        return 1
    return num * get_a_factorial(num - 1)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(20, 12))


# Waterloo Python tutorial
def countup(n):
   if n == 0:
      print('Blastoff!')
   else:
      countup(n - 1)
      print(n)

def countdownBy2(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countdownBy2(n - 2)


def digitalSum(n):
    if n < 10:
        return n
    return n % 10 + digitalSum(n // 10)    


def digitalRoot(num):
   if num < 10:
      return num
   return digitalRoot(digitalSum(num))


def hailstone(n):
   print(n)
   if n == 1:
      return n
   else:
      if n % 2 == 0:
         hailstone(n // 2)
      else:
         hailstone(3 * n + 1)