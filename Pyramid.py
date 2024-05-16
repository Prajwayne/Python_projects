#This program represents a python dict that has numbers as keys and words as values and it basically generates a pyramid of numbers and prints the values of the last number 
def print_pyramid_and_get_last_elements(arr):
    n = len(arr)
    index = 0
    current_row = 1
    last_elements = []

    while index < n:
        # Calculate the number of spaces for the current row
        spaces = (n - current_row) * 1  # Adjust the multiplier for proper alignment

        # Print leading spaces
        print(" " * spaces, end="")

        # Print elements for the current row and track the last element
        for i in range(current_row):
            if index < n:
                print(arr[index], end=" ")
                if i == current_row - 1:
                    last_elements.append(arr[index])
                index += 1

        print()  # Move to the next line
        current_row += 1

    return last_elements

# Define the array
arr = [1, 2, 3, 4, 5, 6]

# Print the pyramid and get the last elements
last_elements = print_pyramid_and_get_last_elements(arr)

# Print the last elements
print("Last elements of each row:", last_elements)