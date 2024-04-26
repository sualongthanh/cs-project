#----------------------------------------------
#Functions
#----------------------------------------------
#def function_name(parameters):
    # statements

def double_number(number):
    total = 2 * number
    print("The double of "+str(number)+ " is: "+ str(total))

def greetings():
    print("welcome to Killarney")
def greeting_name(name):
    print("Hello"+str(name))
#will return a value
def triple_me(number):
    return 3 * number
#----------------------------------------------
#Main Section
#----------------------------------------------
#----------------------------------------------
greetings() #calls the function

greeting_name("Shauna")
firstname = "Jeff"
greeting_name(firstname)
#The double of ____ is: ___
double_number(10)
print(triple_me(20))#nothing displays because there are no prit stmts
stuff = triple_me(40) + 100

print("stuff is"+ str(stuff))
#update your hangman program so that it uses functions to display
#the hangman, instead of print statements within your main
#part of your code
#call the functions to display it
#all your catiables have to be within the function