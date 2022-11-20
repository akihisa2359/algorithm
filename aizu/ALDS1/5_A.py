n = int(input())
*q, = map(int, input().split())
A = int(input())
*m, = map(int, input().split())

def combo(i, num):
  if (num == 0):
    return True
  if (i >= n or num < 0):
    return False
  
  return combo(i + 1, num) or combo(i + 1, num - q[i])

for i in range(A):
  res = "yes" if combo(0, m[i]) else "no"
  print(res)
  