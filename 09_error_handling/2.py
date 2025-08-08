file = open('project.txt', 'w')

with open('project.txt', 'w')as file:
    file.write('Hey! \n')
    file.write('How are you? \n')
    file.write('Where are you? \n')



def new_line_file(project):
    try:
        with open('project.txt', 'r') as file:
            lines = file.readlines()

        numbered_lines = [f"Line (i + 1): (line)" for i, line in enumerate(lines)]

        with open('project.txt', 'w') as file:
            file.writelines(numbered_lines)

        print("Line numbers added successfully.")

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Unexpected error occured: {e}")

new_line_file('project.txt')


            
            
