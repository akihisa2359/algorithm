n = int(input())
*A, = map(int, input().split())
q = int(input())
*m, = map(int, input().split())

def combo(i, num):
    if num == 0:
        return True
    if sum(A[i:]) < num:
        return False
    if i >= n:
        return False
    
    return True if combo(i+1, num) or combo(i + 1, num - A[i]) else False

for i in range(q):
    res = "yes" if combo(0, m[i]) else "no"
    print(res)