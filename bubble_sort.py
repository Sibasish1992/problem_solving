"""Bubble Sort"""


def bubble(a,n):
  for i in range(0,n):
    for j in range(i+1,n):
      if a[i]>a[j]:
        a[i] = a[i]^a[j]
        a[j] = a[i]^a[j]
        a[i] = a[i]^a[j]

  print(a)

bubble([-3,-5,5,2],4)





def bubble(a,n):
  for i in range(0,n):
    for j in range(0,n-i-1):
      if a[j]>a[j+1]:
        a[j] = a[j]^a[j+1]
        a[j+1]=a[j]^a[j+1]
        a[j] = a[j]^a[j+1]
  print(a)
a=[1,3,4,-2,2,-91]
bubble(a,6)

