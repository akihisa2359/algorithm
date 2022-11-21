N = int(input())
*choices, = map(int, input().split())
O = int(input())
*A, = map(int, input().split())

def combo(i, m):
  if (m == 0):
    return True
  if (m < 0 or i == N or sum(choices[i:]) < m):
    return False
  
  return combo(i + 1, m) or combo(i + 1, m - choices[i])

for i in range(O):
  if combo(0, A[i]):
    print("yes")
  else:
    print('no')
