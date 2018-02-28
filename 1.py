for x in range(1, 10):
  for y in range(1, 10):
    for z in range(1, 10):
      if ((x*x + y*y + z*z) == 109) & (x > y > z):
        print("x = ", x)
        print("y = ", y)
        print("z = ", z)
        print("(4x + 2y + 2z) =", 4*x+2*y+2*z)