""" 

This exercise tests out the default values of parameters. Create a program which has a main function and a subfunction called tester. The main function prompts user for an input "Write something (quit ends): " and sends this input to the subfunction as a parameter.

Define the subfunction tester so that it has one parameter called "givenstring", which has the default value "Too short". If the user input is less than 10 characters, the program uses the default value and if 10 or more, it prints the usergiven input. If the user inputs "quit", the program is terminated. When working correctly, the program will print out something like this:
Example output:
Write something (quit ends): test
Too short
Write something (quit ends): second test
second test
Write something (quit ends): quit

"""


def tester(given_string="Too short"):
    # Check the length of given input and print appropriate output
    if len(given_string) < 10:
        print("Too short")
    else:
        print(given_string)


def main():
    while True:
        # Prompt user for input
        user_input = input("Write something (quit ends): ")
        # Check for the quit command
        if user_input == "quit":
            break
        # Call the tester function with the user input
        tester(user_input)


main()
