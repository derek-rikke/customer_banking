# Savings and CD Account Interest Calculator

This Python program provides a simple interface for users to input information about their savings and certificate of deposit (CD) accounts. It calculates the interest earned on both accounts based on user-provided parameters such as balance, interest rate, and the number of months until maturity.

## Program Structure

The program consists of two parts:

### 1. Importing Functions

The program imports two functions, `create_savings_account` and `create_cd_account`, from separate modules (`savings_account.py` and `cd_account.py`). These functions handle the calculations for interest earned and updated balances for the savings and CD accounts, respectively.

```python
# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account
```

### 2. Main Function

The `main` function serves as the core of the program. It prompts the user to enter information about their savings and CD accounts, such as balance, interest rate, and the number of months until maturity. It then calls the respective account functions, updates the balances, and prints out the interest earned along with the new balances.

```python
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """

    # ... (User input for savings account)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # ... (Print out results for savings account)

    # ... (User input for CD account)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # ... (Print out results for CD account)

# ...

if __name__ == "__main__":
    # Call the main function.
    main()
```

## Running the Program

To use the program, follow these steps:

1. Ensure you have the `savings_account.py` and `cd_account.py` modules in the same directory as your main program.
2. Run the program.
3. Input the requested information for the savings account (balance, interest rate, and months until maturity).
4. View the interest earned and updated balance for the savings account.
5. Input the requested information for the CD account (balance, interest rate, and months until maturity).
6. View the interest earned and updated balance for the CD account.

## Note

Make sure to handle exceptions appropriately, such as invalid user inputs, to enhance the robustness of the program.

Written with ChatGPT
