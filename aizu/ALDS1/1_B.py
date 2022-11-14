l = map(int, input().split())
x, y = sorted(l, reverse=True)

reminder = y
while x % y != 0:
    reminder = x % y
    x, y = y, reminder

print(reminder)