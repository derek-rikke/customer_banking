# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance interest rate, and months for the savings account.
    while True:
        savings_balance = input("Enter savings balance: ")
        if savings_balance.isdigit():
            savings_balance = float(savings_balance)
            break
        else:
            print("Input not valid. Please enter a non-negative number.")
    
    while True:
        savings_interest = input("Enter savings interest: ")
        if savings_interest.isdigit():
            savings_interest = float(savings_interest)
            break
        else:
            print("Input not valid. Please enter a non-negative number.")
            
    while True:
        savings_maturity = input("Enter the number of months until maturity: ")
        if savings_maturity.isdigit():
            savings_maturity = int(savings_maturity)
            break
        else:
            print("Input not valid. Please enter a non-negative number.")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"The interest earned on your savings account is ${interest_earned:,.2f}")
    print(f"The new savings account balance is ${updated_savings_balance:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    while True:
        cd_balance = input("Enter CD balance: ")
        if cd_balance.isdigit():
            cd_balance = float(cd_balance)
            break
        else:
            print("Input not valid. Please enter a non-negative number.")
    
    while True:
        cd_interest = input("Enter CD interest: ")
        if cd_interest.isdigit():
            cd_interest = float(cd_interest)
            break
        else:
            print("Input not valid. Please enter a non-negative number.")
    
    while True:
        cd_maturity = input("Enter the number of months until CD maturity: ")
        if cd_maturity.isdigit():
            cd_maturity = int(cd_maturity)
            break
        else:
            print("Input not valid. Please enter a non-negative number.")
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The interest earned on the CD is ${cd_interest_earned:,.2f}")
    print(f"The new account balance of the CD is ${updated_cd_balance:,.2f}")

if __name__ == "__main__":
# Call the main function.
    main()