import math

N = int(input())

prime_count = N

for i in range(N):
  v = int(input())

  if v == 2:
    continue

  square_root = math.ceil(v ** 0.5)
  for j in range(2, square_root + 1):
    if (v % j) == 0:
      prime_count -= 1
      break


print(prime_count)