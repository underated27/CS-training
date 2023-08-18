input_str = input("Enter a string: ")
reversed_str = input_str[::-1]
output_str = ""
for char in reversed_str:
    if char not in output_str:
        output_str += char
print(output_str)
