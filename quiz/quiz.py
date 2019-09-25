def show_menu():
    print("1. Ask questions")
    print("2. Add question")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option

def ask_questions():
    questions = []
    answers = []
    
    with open("questions.txt", "r") as file:   # a with block is a good method for opening files.it handles a lot of stuff for us. For instance, we don't need to worry about closing the file because at the end of the width block it will be closed.
     lines = file.read().splitlines()  #in the variable lines: read our file in and split the lines.
     
     for i, text in enumerate(lines):   #The enumerate function is going to turn each of these lists into a tuple with a line number stored in 'i' and
         if i%2 == 0:                   #the text in 'text'. So, if 'i' is even - if the line number is even -then we say that that's a question. 
           questions.append(text)       #If it's odd, then that's going to be an answer.
         else:
           answers.append(text)
           
     for question, answer in zip(questions, answers):
         guess = input(question + "> ")
         
def add_question():
    print("")
    question = input("Enter a question\n> ")  #We'll put a new line here, and then a greater-than sign as a prompt, and a space just to make it look nice.
    
    print("")
    print("OK then, tell me the answer")
    answer = input("{0}\n> ".format(question))  #we'll take the question that we'd already asked, do a blank line, a greater-than sign for a prompt and then, 
                                                #using the format method, we'll insert the question there. So, now the user will be asked the question again 
                                                #when they come to put the answer in.
    file = open("questions.txt","a")   #we add this to the file. We'll open our questions.txt file for appending using the 'a' access mode flag.
    file.write(question + "\n")    #we will first add our questions and add a new line
    file.write(answer + "\n")    #The second thing we'll do is write our answer
    file.close()  #and finally, close the file
    
def game_loop():
    while True:   #loop until there is a break
       option = show_menu() 
       if option == "1":  #if our option is equal to 1, print the string.
         print("You selected 'Ask questions'")
       elif option == "2": 
           add_question()  #if the user selects option 2 then the add_question() function will be called and we'll be prompted for a question and an answer.
       elif option == "3":
           break     #if choosing option 3, quit the game
       else:       #In case somebody puts anything other than 1, 2 or 3  we'll print 'Invalid option'. 
           print("Invalid option")
           print("")   #print a blank line after all this, to make it look nicer
           
game_loop()   #call the game loop