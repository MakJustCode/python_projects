'''Makenson Noel
Reverse Array'''

A = ['M', 'I', 'A', 'M', 'I']

length = len(A)
i = length - 1


def reverse():
  i = 0
  j = length - 1
  temp = 0

  for i in range (length):
    temp = i
    i = j 
    j = temp 

    print("Reversed Array: ", A[temp])


print("Array :", A)

reverse() 




