# 540 = X + Y
# 5/7X = 1/4Y
#### Working
## y = 20/7X
## 540 = 20/7x + x = 27/7x
## x = 540/27 * 7 = 140
## x(5/7) = 100
## x = 140, y = 540 - 140
## y = 400
## y(3/4) = 100

for x in range(1, 540):
  for y in range(1, 540):
    if (5/7*x == 1/4*y) & (x + y == 540):
      print("x = ", x)
      print("y = ", y)
      print("x(5/7)=", x*5/7)
      print("y(1/4) =", y*1/4)