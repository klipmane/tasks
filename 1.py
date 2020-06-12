for i in range(100, 0, -1):
    if i % 3 == 0 and i % 5 == 0:
        print("Testing")
        continue
    elif i % 5 == 0:
        print("Agile")
        continue
    elif i % 3 == 0:
        print("Software")
        continue
    else:
        print(i)
