f = open('/home/ubuntu/environment/files/relative_data.txt', 'r')  #create a variable to open our txt file for reading.
lines = f.read()  #here we call the readlines method and put that in the variable lines.
f.close()  #We'll close our file handle
print(lines) #and then print the results to the screen.