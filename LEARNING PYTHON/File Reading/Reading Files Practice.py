employee_file = open("Reading Files Example.txt", "a")     #'r' allows for reading, 'w' allows for overwriting on txt file, 'a' allows for appending
test_file = open("newFile.html", "w")                      #by writing a random file name in first argument, it auto creates a new file if no existing name is found

test_file.write("<p>This is a testing HTML page</p>")      #writes text into new file we created

#print(employee_file.readable())                            #checks if txt file is readable
#print(employee_file.read())                                #read txt file line by line
#print(employee_file.readlines())                           #read txt file as a list

employee_file.write("\nToby - Human Resources")             #appending text to a existing txt file
employee_file.write("\nKelly - Customer Service")

employee_file.close()                                       #good practice to always close files after use