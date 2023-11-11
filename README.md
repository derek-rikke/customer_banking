# Savings and CD Account Interest Calculator

This Python program provides a user-friendly interface for determining the interest earned on savings and certificate of deposit (CD) accounts. It utilizes the `create_savings_account` and `create_cd_account` functions from external modules to handle interest calculations.

## Program Overview

### Importing Functions

```python
# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account
```

The program begins by importing functions from separate modules (`savings_account.py` and `cd_account.py`) to handle the calculations for the savings and CD accounts.

### Main Function

```python
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    while True:
        # Validate user input for savings balance
        savings_balance = input("Enter savings balance: ")
        if savings_balance.isdigit():
            savings_balance = float(savings_balance)
            break
        else:
            print("Input not valid. Please enter a non-negative number.")

    # ... (Similar validation for savings interest and maturity)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"The interest earned on your savings account is ${interest_earned:,.2f}")
    print(f"The new savings account balance is ${updated_savings_balance:,.2f}")

    # ... (Similar user input and validation for CD account)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The interest earned on the CD is ${cd_interest_earned:,.2f}")
    print(f"The new account balance of the CD is ${updated_cd_balance:,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()
```

The `main` function serves as the core of the program. It guides the user through the process of entering information about their savings and CD accounts, ensuring valid inputs at each step. The program then calls the appropriate functions to calculate interest and updated balances, displaying the results.

## Running the Program

1. Ensure the `savings_account.py` and `cd_account.py` modules are present in the same directory as your main program.

2. Run the program.

3. Input the requested information for the savings account (balance, interest rate, and months until maturity).

4. View the interest earned and updated balance for the savings account.

5. Input the requested information for the CD account (balance, interest rate, and months until maturity).

6. View the interest earned and updated balance for the CD account.

## Note

The program incorporates input validation to handle potential errors or invalid inputs, providing a more robust and user-friendly experience. If a user enters invalid input, the program prompts them to re-enter the information until valid data is provided.

This readme was written using ChatGPT
