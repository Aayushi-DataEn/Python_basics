file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()





with open('youtube.txt',  'w') as file:
    file.write('chai aur code')
    # 12 this syntax handle closing  the file and other things itself without further writing close etc


# file = open('python.txt', 'w')

# with open('python.txt', 'w') as file:
#     file.write('Hello! \n')
#     file.write('how are you? \n')
#     file.write('where are you? \n')