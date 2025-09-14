def print_pattern(rows):
    for i in range(rows):
        print("  " * i, end="")
        pattern = " ".join(["1" if j % 2 == 0 else "0" for j in range(rows - i)])
        print(pattern)

print_pattern(5)
