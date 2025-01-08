for row in range(4):
    for col in range(7):
        if row-col==0 or col+row==6:
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()