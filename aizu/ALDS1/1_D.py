N = int(input())

lowestPrice = float('inf')
maxProfit = -float('inf')
for i in range(N):
  v = int(input())
  maxProfit = max(maxProfit, v - lowestPrice)
  lowestPrice = min(lowestPrice, v)

print(maxProfit)