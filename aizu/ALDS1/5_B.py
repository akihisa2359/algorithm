def merge_sort(arr, counter):
  if len(arr) == 1:
    return arr
  mid = len(arr) // 2

  arr_l = merge_sort(arr[:mid], counter)
  arr_r = merge_sort(arr[mid:], counter)

  arr_l.append(float('inf'))
  arr_r.append(float('inf'))

  i = 0
  j = 0
  sorted_arr = []

  for k in range(len(arr)): # infを足した分2引く
    counter[0] += 1
    if arr_l[i] < arr_r[j]:
      sorted_arr.append(arr_l[i])
      i += 1
    else:
      sorted_arr.append(arr_r[j])
      j += 1
  
  return sorted_arr

n = int(input())
ls = list(map(int, input().split()))

# ls = [6,3,9,2,1,10]
counter = [0]
res = merge_sort(ls, counter)
print(*res)
print(counter[0])