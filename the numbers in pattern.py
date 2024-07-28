                #  THE PYTHON PROGRAM TO PRINT THE NUMBERS IN PATTERN USING NESTED LOOP.
#the logic for print the number 0 using the nested loop.
for i in range(1, 8):
    for j in range(1, 6):
        if (i == 1 or i == 7) and (j > 1 and j < 5) or (j == 1 or j == 5) and (i > 1 and i < 7):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()

# the logic for print the number 1 using the nested loop.
for i in range(1, 9):
    for j in range(1, 7):
        if i == 5 - j or j == 4 or i == 8:
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()
    
# the logic for print the number 2 using the nested loop.
for i in range(1, 8):
    for j in range(1, 6):
        if (i == 1) or (i == 4) or (i == 7) or (i < 4 and j == 5) or (i > 4 and j == 1):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()
    
# the logic for print the number 3 using the nested loop.
for i in range(1, 8):
    for j in range(1, 6):
        if (i == 1) or (i == 4) or (i == 7) or (j == 5) or (i < 4 and j == 0):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()
    
# the logic for print the number 4 using the nested loop.
for i in range(1, 8):
    for j in range(1, 6):
        if (j == 1 and i < 4) or (i == 4) or (j == 4):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()
    
 # the logic for print the number 5 using the nested loop.  
for i in range(1, 8):
    for j in range(1, 6):
        if (i == 1) or (i == 4) or (i == 7) or (i < 4 and j == 1) or (i > 4 and j == 5):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()
    
# the logic for print the number 6 using the nested loop.    
for i in range(1, 8):
    for j in range(1, 6):
        if (i == 1 and j > 1) or (i == 4) or (i == 7) or (j == 1) or (i > 4 and j == 5):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()
    
# the logic for print the number 7 using the nested loop.
for i in range(1, 8):
    for j in range(1, 6):
        if (i == 1) or (i + j == 7):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()

# the logic for print the number 8 using the nested loop.
for i in range(1, 8):
    for j in range(1, 6):
        if (i == 1) or (i == 4) or (i == 7) or (j == 1) or (j == 5):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()

# the logic for print the number 9 using the nested loop.
for i in range(1, 8):
    for j in range(1, 6):
        if (i == 1) or (i == 4) or (i == 7 and j < 5) or (j == 5) or (i < 4 and j == 1):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()
    


