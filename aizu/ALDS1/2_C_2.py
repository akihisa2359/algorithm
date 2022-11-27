import copy
N = int(input())
*cards, = input().split()
cards2 = copy.copy(cards)

for i in range(N - 1):
  for j in range(N - i - 1):
    v1 = int(cards[j][1])
    v2 = int(cards[j + 1][1])
    if (v1 > v2):
      cards[j], cards[j + 1] = cards[j + 1], cards[j]
print(*cards)
print("Stable")

for i in range(N - 1):
  minj = i
  for j in range(i + 1, N):
    if (int(cards2[minj][1]) > int(cards2[j][1])):
      minj = j
  cards2[i], cards2[minj] = cards2[minj], cards2[i]

print(*cards2)
res = "Stable" if (cards == cards2) else "Not stable"
print(res)