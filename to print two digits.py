# To print the pattern for digits "1" and "0" in a single line using nested loops in Python.

for i in range(1, 8):
    # Pattern for 1
    for j in range(1, 6):
        if j == 3 or (i == 1 and j == 2) or (i == 2 and j == 1):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    
    # Space between the digits
    print("  ", end="")
    
    # Pattern for 0
    for j in range(1, 6):
        if (i == 1 or i == 7) and (j > 1 and j < 5) or (j == 1 or j == 5) and (i > 1 and i < 7):
            print("+", end="  ")
        else:
            print(" ", end="  ")
    
    # Move to the next line
    print()
