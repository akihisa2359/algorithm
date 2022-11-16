import math

def isPrime(v):
  if v == 2: return True

  square_root = math.ceil(v ** 0.5)
  for i in range(2, square_root + 1):
      if v % i == 0:
          return False
    
  return True

N = int(input())
primeCount = 0

for i in range(N):
    v = int(input())
    primeCount += isPrime(v)
    
print(primeCount)