def merge_sort(arr, counter):
  if len(arr) == 1:
    return

  arr_l = arr[:(len(arr) // 2)]
  arr_r = arr[(len(arr) // 2):]

  merge_sort(arr_l, counter)
  merge_sort(arr_r, counter)

  arr_l.append(float('inf'))
  arr_r.append(float('inf'))

  i = 0
  j = 0

  for k in range(len(arr)): # infを足した分2引く
    counter[0] += 1
    if arr_l[i] < arr_r[j]:
      arr[k] = arr_l[i]
      i += 1
    else:
      arr[k] = arr_r[j]
      j += 1

n = int(input())
ls = list(map(int, input().split()))

# ls = [6,3,9,2,1,10]
counter = [0]
merge_sort(ls, counter)
print(*ls)
print(counter[0])