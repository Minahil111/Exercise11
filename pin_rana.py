# Set variable for correct pin code
pin = {8888}

# max attempts will restrict pin attempts to three and to end if entered incorrect 3 times

attempts = 0
max_attempts = 3

# Input function to request pin code
# Using "while" function to allow the code to be repeated
# int is makes sure the input is a number
# Getpass used to hide characters typed in the pin get.pass is an imported module
# The "in" function is used to check if the value is present
while attempts < max_attempts:
    supplied_pin = int(input("Enter your pin:"))
    if supplied_pin in pin:
        print("Correct pin")
        break

# Else used to repeat question to allow a further attempt if wrong pin is provided & use "else" to prompt to try again
# "F" is used as a prefix for creating f-strings to format strings with the values of variables inserted in to them
# Used the number of attempts to determine when pin lock message to be returned
# End with a break statement at the end to exit the condition
# Added attempts count at the end to sure it runs in the right order
    else:
        remaining_attempts = max_attempts - (attempts + 1)

        if remaining_attempts > 0:
            print(f"Incorrect PIN. {remaining_attempts} Attempts remaining. Please try again.")
        attempts += 1

        if attempts == max_attempts:
            print("Incorrect pin entered three times, pin locked")
            break

