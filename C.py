for row in range(6):
    for col in range(6):
        if (col==0 and (row!=0 and row!=5)) or ((row==0 or row==5) and (col>0)):
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()