with open ('newfile.txt', 'a') as file:
    #file.write('This is a new file created by Python!')
    file.writelines(['\nThis is a new file created by Python!\n', 'This is another line to be added'])