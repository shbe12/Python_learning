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

# ask user for email.
write_log("App Started")
email = input("Enter your email: ")
is_valid_email(email)
if not is_valid_email(email):
    write_log(f"Invalid Email received:{email}")
else:
    clean_email =clean_and_split_email(email)
    write_log(f"Processed Email:{clean_email}")
write_log("App Stopped")
