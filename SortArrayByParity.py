from collections import deque

def sortArrayByParity(A):
  newlist = deque()
  for a in A:
      if a % 2 == 0:
          newlist.appendleft(a)
      else:
          newlist.append(a)
  return newlist

A = [1,2,3,4,5,6,7,8]
print(f"(TEST)\n\tList: {A}\n\tResult: {sortArrayByParity(A)}")
