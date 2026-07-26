# action functions
# action function designed to perform an operation in the system instead of returning values.
# action focus on side effects, change something outside the funcion
#action function- function that is printing something on the screen or function that saves data to a file or to a database,function sending email if something goes wrong,calling externa API
# DO something outside the function as a side effect
# side effect,command,hander,service,different functions for the same idea
# store application log messages in a file whenever an event occurs

def write_log(message): #input parameter
    # since are using a lot of backlashes add r , to show it is a string, not special character
    # how to store info inside our file, we go with the a
    #Append mode "a"- it appends at the end of the file, if the file does not exist it will create it, if it exists it will add to the end of the file, it will not overwrite the existing content
    # dont  go and delete anything or update anything, just add to the end of the file, if you want to update or delete you have to do it manually
    # as file so that we can write to the file
    # inside the statement , write inside the file , it gonna be messages, our parameter
    # to put each message in a new line, we add \n at the end of the message
    # python go create a file called app.log, inside the path C:\Main\Python, if the file does not exist it will create it, if it exists it will add to the end of the file, it will not overwrite the existing content
    # the mode is append, it will not overwrite the existing content, it will add to the end of the file
    # for the action we are writing inside the file by adding the parameter message into a new line
    # when we send it ,if there's no error, that means the action is successful, if there is an error, it will throw an exception, we can handle the exception and log the error message into the file

    with open(r"C:\Main\Python\app.log",  "a") as file: # with open -opens the file safely and closes it automacically when done
        file.write(message + "\n")

# write_log("App Started")
# write_log("user logged in")
write_log("App Stopped")

#transformation function
# transformation function takes raw data as an input, does transformation and data manipulations, and then returns new value with new shape
# not about changing the system or interacting with something outside the function, its all
# its all about changing the shape of your data, can conrains core business logic that can manipulate the data.
# data function, calculation,utility, mapper

# cleans email addresses and splits them into structured data(username and domain name)
def clean_and_split_email(email): #input email parameter
    #clean the email , by putting in local variable,remove extra spaces and put in lower case
    cl_email = email.strip().lower() #local variable
    # split into username and domain, 2 informations 2 variables
    # extract by using method split, split at the @ symbol, store the 2 parts in 2 variables, username and domain
    username, domain = cl_email.split("@") #local variable
    # return username, domain #return value as tuple
    #return as a data structure , since theres two different type of info , we use dictionary,parentheses, key values, username, domain
    return {"username": username,
            "domain": domain} #return value as dictionary

print(clean_and_split_email(" SARA@gmail.com "))

# validation fuction
# validates a condition and returns a boolean result(True or False)
# no action, ask question, function can answer question
# bad data quality , use vlaidation function to protect your system from bad data
# validation function protect your data before entering it

# check whether password meets the minimum requirements of 8 characters
def is_valid_password(password):
    # return condition, returning the result of our check
    return len(password) >= 8

print(is_valid_password("12345678")) #True
print(is_valid_password("1234567")) #False


# check if email adress has a basic valid format

def is_valid_email(email):
   return "@" in email and "." in email

print(is_valid_email("sara@gmail.com")) #True
print(is_valid_email("sara@gmail")) #False

# orchestrator function
# orchestrator function controls program flow by calling other functions in the correct order.
# focus on coordination and not logic or calculating sata or changing anything
# main job to connect everything and decide what is the next step
# process workflow, makes it easy to understand your progam in a high level.
#orchestrator, workflow functions, controller, pipeline, coordinator

#project
# 1. receive an email from user
# 2. validate the email
# 3. if it is invalid, log an error in a file.
# 4. if it is valid, clean and structure the email.
# 5. log each step of the program.

# # exta info- at start log "App Started", at the end log "App Stopped"
# write_log("App Started")
# # ask user for input
# email = input("Enter your email: ")
# # 2 types of function work together, first validate email we are validate function then use transformation
# # check if it a valid email
# # if not valid , then log , write an issue inside  the log,
# #  there is somekind of condition, if fulfilled write a log
# # build condition
# if not is_valid_email(email):
#     write_log(f"Invalid Email received:{email}")
#     #if valid clean and structure info
# else:
#     # process email , clean and split, print inside our log
#     # store the returned value from the function in a global variable
#     clean_email = clean_and_split_email(email)
#     # last step log everything that is happening
#     #if it is valid log
#     # then print it in the logs
#     write_log(f"Processed Email:{clean_email}")
# write_log("App Stopped")

# Orchestrator Function
def process_user_email(email):
    # we can either leave the input empty because we are getting the email from the user inpur
    #or we take only the user input  step outside and we send this
    # lets take the user input step outside the orchstraor function
    # exta info- at start log "App Started", at the end log "App Stopped"
    write_log("App Started")
    # 2 types of function work together, first validate email we are validate function then use transformation
    # check if it a valid email
    # if not valid , then log , write an issue inside  the log,
    #  there is somekind of condition, if fulfilled write a log
    # build condition
    if not is_valid_email(email):
        write_log(f"Invalid Email received:{email}")
        #if valid clean and structure info
    else:
        # process email , clean and split, print inside our log
        # store the returned value from the function in a global variable
        clean_email = clean_and_split_email(email)
        # last step log everything that is happening
        #if it is valid log
        # then print it in the logs
        write_log(f"Processed Email:{clean_email}")
    write_log("App Stopped")

# orchestrator email call other functions in the correct order
# all we have to do in the body of the program is calling this function
# the body of our progam has only two lines of code gice the data and process it
# everything else is actually inside functions
# ask user for input
email = input("Enter your email: ")
# collect email and processuseremail and pass the input from user
process_user_email(email)

# Summary functions by purpose, Function Types Review
#1.Action functions make things happen, interact with things outside your program ,
# your system, printing,saving files, calling an API,
# 2.the transformation function work with your data, take input,change it, return a new value
# 3.Validation function checks the rules, answer your questions with either yes or no
# used to protect your system and to check the quality of your bad data
# 4. The orchestrator function connect everything together by calling other many functions in the correct order
