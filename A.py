for row in range(8):
    for col in range(7):
        if row+col==3 or row==5 or col-row==3 or (col==0 and row>2)or (col==6 and row>2 ):
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()  