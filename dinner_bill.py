# Programmer: Andrew Dwyer
# Date: 3/3/22
# Program Name: dinner_bill.py

# imports of other modules
import appetizer
import entre
import dessert


def main():
    while True:
        # initialize the cost var to $0
        cost = 0

        # get the information from the user and calculate the price
        # cost += get_appetizer_info()
        # cost += get_entre_info()
        cost += get_dessert_info()

        # display the cost rounded to 2 decimal places
        print(f"\nThe total cost for the meal is: ${cost:,.2f}")

        # Ask the user if they want to repeat the process or quit the program
        choice = input("\nDo you want to calculate the cost of an other meal? (y/anything else to quit) ")

        if choice.lower() != 'y':  # then end the program
            break
        else:
            print("") # print a new line to organize the output better
    print("\nProgram completed.")  # if the user chooses to quit this is displayed


# Asks the user for information on the appetizers
# returns the price from the appetizer module
def get_appetizer_info():
    num_diners = get_num_diners("How many diners are having an appetizer? ")
    cost = get_cost("What is the cost of an one appetizer? $")
    # return appetizer.calc_cost(num_diners, cost)


# Asks the user for information on the entres
# returns the price from the entre module
def get_entre_info():
    num_diners = get_num_diners("How many diners are having an entre? ")
    cost = get_cost("What is the cost of an one entre? $")
    # return entre.calc_cost(num_diners, cost)


# Asks the user for information on the desserts
# returns the price from the dessert module
def get_dessert_info():
    num_diners = get_num_diners("How many diners are having an dessert? ")
    cost = get_cost("What is the cost of an one dessert? $")
    return dessert.calc_cost(num_diners, cost)


# Gets the number of diners from the user and checks if the input is valid
# prompt: the text to display to the user asking for input
def get_num_diners(prompt):
    num_diners = 0
    is_valid = False
    while not is_valid:
        try:
            num_diners = int(input(prompt))
            if num_diners > 0:
                is_valid = True
            else:
                print("Invalid input. The number of diners must be a number greater than 0 and not contain any decimals.")
        except ValueError:
            print("Invalid input. The number of diners must be a number greater than 0 and not contain any decimals.")
        except:  # catch all exception
            print("There was an error with your input. Please try again.")
    return num_diners


# Gets the cost from the user and checks if the input is valid
# prompt: the text to display to the user asking for input
def get_cost(prompt):
    cost = 0
    is_valid = False
    while not is_valid:
        try:
            cost = float(input(prompt))
            if cost > 0:
                is_valid = True
            else:
                print("Invalid input. Cost must be a number greater than $0.00.")
        except ValueError:
            print("Invalid input. Cost must be a number greater than $0.00.")
        except:  # catch all exception
            print("There was an error with your input. Please try again.")
    return cost


# run main if the program is imported as a module
if __name__ == "__main__":
    main()

