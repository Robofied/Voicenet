# from pathlib import Path
# import os

# BASE_path = os.path.abspath(os.curdir)

def my_func(s, z):
  total = 0
  len_str = len(s)

  for x, y in z:
    if x == 0:
      total += y
    else:
      total -= y
  total = total % len_str
  print(s[total:] + s[:total])


s = 'cutshort'
z = [[0, 3], [1, 11]]

if __name__ == "__main__":
  my_func(s, z)
  
def my_func(nums):
  count = 0
  for i, j in enumerate(nums):
    if i > count:
      return False
    count = max(count, i + j)
  return True


if __name__ == "__main__":
  print(my_func([3, 2, 1, 0, 4]))
  

def oddsums(n):
  total=0
  result=[]
  for i in range(1,n+1):
    odd= 2*i-1
    total=total+odd
    result.append(total)
  return result

print(oddsums(5))

def my_func(num):
  data = [0]
  for i in range(1, num+1):
    data.append(data[i >> 1] + int(i & 1))
  return data


num = 6
print(my_func(num))

t=(1,2,4,3)
print(t[1:-1])

d1 = {"john":40, "peter":45}
d2 = {"john":466, "peter":45}
print(d1 == d2)

x = [34, 56]
print(len(map(str, x)))

t=(1,2,4,3)
print(t[1:3])

values = [[3, 4, 5, 1], [33, 6, 1, 2]]
v = values[0][0]
for lst in values:
    for element in lst:
        if v > element:
            v = element
print(v)
  
def f(i, values = []):
    values.append(i)
    return values

f(1)
f(2)
v = f(3)
print(v)

import math
print(math.fsum([.1 for i in range(20)]))

print(math.fabs(-3.4))

print(sum([.1 for i in range(20)]))

list1 = [11, 2, 23]
list2 = [11, 2, 2]
print(list1 < list2) 