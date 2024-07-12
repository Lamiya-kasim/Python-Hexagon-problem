def print_hex_pattern(rows, cols):
    hex_row_odd = "  ___   " * cols
    hex_row_even = " /   \\_/ " * cols
    hex_row_fill = "/       \\" * cols

    for r in range(rows):
        print(hex_row_odd)
        print(hex_row_even)
        print(hex_row_fill)
        print(hex_row_even)
print("inputs :- 4 7")
print_hex_pattern(4, 7)
print("\ninputs :- 3 5")
print_hex_pattern(3, 5)
