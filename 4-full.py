for a in range(1,360):
  for b in range(1,360):
    for c in range(1,360):
      if (a+b+c==360) & (a%6==0) & (b%3==0) & (c%5==0) :
        print("a=",a," b=",b," c=",c)
        print("1/5*",c,"=",(1/5*c))
        print("5/6*",a,"=",(5/6*a))
        print("1/6*",a,"=",(1/6*a))
        print("2/3*",b,"=",(2/3*b))
        print("1/3*",b,"=",(1/3*b))
        print("4/5*",c,"=",(4/5*c))
        print("a+b+c=",(a+b+c))

## Test 108 sets

# a = 108
# b = 162
# c = 90

# 1/5*90 = 18
# 5/6*108 = 90 
# 108

# 1/6*108 = 18
# 2/3*162 = 108
# 126

# 1/3*162 = 54
# 4/5*90 = 72
# 126

## Test 288 sets

# a = 288
# b = 57
# c = 15

# 1/5*15 = 3
# 5/6*288 = 240
# 108

# 1/6*288 = 48
# 2/3*57 = 38
# 126

# 1/3*57 = 19 
# 4/5*15 = 12
# 126

# a = 342
# b = 3
# c = 15

### Test last sets

# 1/5*15 = 3
# 5/6*342 = 285
# 108

# 1/6*342 = 57
# 2/3*3 = 2
# 126

# 1/3*3 = 1
# 4/5*15 = 12
# 126