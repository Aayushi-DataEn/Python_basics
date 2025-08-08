file = open('python.txt', 'w')

with open('python.txt', 'w') as file:
    file.write('Hello! \n')
    file.write('how are you? \n')
    file.write('where are you? \n')


def add_line_numbers(python):
    """
    Opens a text file, reads each line, adds line numbers to the beginning,
    and writes the result back to the file.
    """
    try:
        # Step 1: Read all lines from the file
        with open('python.txt', 'r') as file:
            lines = file.readlines()

        # Step 2: Add line numbers
        numbered_lines = [f"Line {i + 1}: {line}" for i, line in enumerate(lines)]

        # Step 3: Write the modified lines back to the file
        with open('python.txt', 'w') as file:
            file.writelines(numbered_lines)

        print("Line numbers added successfully!")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




# Example usage
# Replace 'example.txt' with your actual file name
add_line_numbers('python.txt')