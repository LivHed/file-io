def show_menu():
    print("1. Ask questions")
    print("2. Add question")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option
    
def game_loop():
    while True:   #loop until there is a break
       option = show_menu() 
       if option == "1":  #if our option is equal to 1, print the string.
         print("You selected 'Ask questions'")
       elif option == "2": 
           print("You selected 'Add a question'")
       elif option == "3":
           break     #if choosing option 3, quit the game
       else:       #In case somebody puts anything other than 1, 2 or 3  we'll print 'Invalid option'. 
           print("Invalid option")
           print("")   #print a blank line after all this, to make it look nicer
           
game_loop()   #call the game loop