# A + B = 10
# A + C = 20
# B + C = 24
## Working
## 2A + 2B + 2C = 54
## A + B + C = 27 

for x in range(1, 54):
  for y in range(1, 54):
    for z in range(1, 54):
      if (x+y==10) & (x+z==20) & (y+z==24):
        print("x = ", x)
        print("y = ", y)
        print("z = ", z)
        print("x+y+z =", x+y+z)