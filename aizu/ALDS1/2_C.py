import copy

N = int(input())
*A, = input().split()
B = copy.copy(A)

for i in range(N - 1):
  for j in range(N - i - 1):
    val1 = int(A[j][1])
    val2 = int(A[j + 1][1])
    if ( val1 > val2):
      A[j], A[j + 1] = A[j + 1], A[j]
print(*A)
print("Stable")

res = "Stable"
for i in range(N - 1):
  minj = i
  passed_same_num = False
  for j in range(i, N - 1):
    val1 = int(B[minj][1])
    val2 = int(B[j + 1][1])
    if (int(B[i][1]) == val2):
      passed_same_num = True
    if (val1 > val2):
      minj = j + 1
      if (passed_same_num):
        res = "Not stable"
  B[i], B[minj] = B[minj], B[i]
print(*B)
print(res)
