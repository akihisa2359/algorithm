N = int(input())
*A, = map(int, input().split())

count = 0
for i in range(N - 1):
  minj = i
  hasChanged = False
  for j in range(i, N):
    if A[j] < A[minj]:
      minj = j
      hasChanged = True
  count += hasChanged
  A[i], A[minj] = A[minj], A[i]

print(*A)
print(count)