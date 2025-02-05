def myAddUniversal(*args):
    s = 0
    for i in range(len(args)):
        s += args[i]
    return s
  print(myAddUniversal(4,6,7,8,9))
