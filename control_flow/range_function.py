# range(10) generates 10 values, the legal indices for items of a sequence of length 10
for i in range(10):
  print(i)


# to specify a different increment (even negative; sometimes this is called the ‘step’):
"""
range(5, 10)
   5, 6, 7, 8, 9

range(0, 10, 3)
   0, 3, 6, 9

range(-10, -100, -30)
  -10, -40, -70
"""

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
  print(i, a[i])