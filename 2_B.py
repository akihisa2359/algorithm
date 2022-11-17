N = int(input())
*A, = map(int, input().split())

count = 0
for i in range(N):
  changed = False
  minj = i
  for j in range(i, N):
    if (A[minj] > A[j]):
      minj = j
      changed = True

  A[i], A[minj] = A[minj], A[i]
  count += changed

print(*A)
print(count)