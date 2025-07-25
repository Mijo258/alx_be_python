size = int(input("Enter the size of the pattern:"))
i = 1
while i > 0 and i <= size: 
    for j in range(1, size + 1):
        print("*", end="")
    print()
    i += 1  