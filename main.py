#python
from database import create_connection


def create_account():
    connection = create_connection()
    if connection is None:
        return

    cursor = None

    try:
        account_number = input("Enter account number: ").strip()
        customer_name = input("Enter customer name: ").strip()
        phone = input("Enter phone number: ").strip()
        account_type = input(
            "Enter account type (Savings/Current): "
        ).strip().capitalize()

        if not account_number or not customer_name or not phone:
            print("Account number, name, and phone cannot be empty.")
            return

        if account_type not in ("Savings", "Current"):
            print("Account type must be Savings or Current.")
            return

        balance = float(input("Enter initial balance: "))

        if balance <= 0:
            print("Initial balance must be greater than zero.")
            return

        cursor = connection.cursor()

        query = """
        INSERT INTO accounts
        (account_number, customer_name, phone, account_type, balance)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            account_number,
            customer_name,
            phone,
            account_type,
            balance
        )

        cursor.execute(query, values)
        connection.commit()

        print("Account created successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except Exception as e:
        connection.rollback()
        print("Error creating account:", e)

    finally:
        if cursor:
            cursor.close()
        connection.close()


def check_balance():
    connection = create_connection()
    if connection is None:
        return

    cursor = None

    try:
        account_number = input("Enter account number: ").strip()

        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT customer_name, balance
            FROM accounts
            WHERE account_number = %s
            """,
            (account_number,)
        )

        account = cursor.fetchone()

        if account:
            print("Customer:", account[0])
            print("Current balance: ₹", account[1])
        else:
            print("Account not found.")

    except Exception as e:
        print("Error checking balance:", e)

    finally:
        if cursor:
            cursor.close()
        connection.close()


def deposit():
    connection = create_connection()
    if connection is None:
        return

    cursor = None

    try:
        account_number = input("Enter account number: ").strip()
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        cursor = connection.cursor()

        cursor.execute(
            "SELECT account_number FROM accounts WHERE account_number = %s",
            (account_number,)
        )

        if cursor.fetchone() is None:
            print("Account not found.")
            return

        cursor.execute(
            """
            UPDATE accounts
            SET balance = balance + %s
            WHERE account_number = %s
            """,
            (amount, account_number)
        )

        cursor.execute(
            """
            INSERT INTO transactions
            (account_number, transaction_type, amount)
            VALUES (%s, 'DEPOSIT', %s)
            """,
            (account_number, amount)
        )

        connection.commit()
        print("Deposit successful!")

    except ValueError:
        print("Invalid amount. Please enter a valid number.")

    except Exception as e:
        connection.rollback()
        print("Error during deposit:", e)

    finally:
        if cursor:
            cursor.close()
        connection.close()


def withdraw():
    connection = create_connection()
    if connection is None:
        return

    cursor = None

    try:
        account_number = input("Enter account number: ").strip()
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        cursor = connection.cursor()

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = %s",
            (account_number,)
        )

        account = cursor.fetchone()

        if account is None:
            print("Account not found.")
            return

        if amount > account[0]:
            print("Insufficient balance.")
            return

        cursor.execute(
            """
            UPDATE accounts
            SET balance = balance - %s
            WHERE account_number = %s
            """,
            (amount, account_number)
        )

        cursor.execute(
            """
            INSERT INTO transactions
            (account_number, transaction_type, amount)
            VALUES (%s, 'WITHDRAWAL', %s)
            """,
            (account_number, amount)
        )

        connection.commit()
        print("Withdrawal successful!")

    except ValueError:
        print("Invalid amount. Please enter a valid number.")

    except Exception as e:
        connection.rollback()
        print("Error during withdrawal:", e)

    finally:
        if cursor:
            cursor.close()
        connection.close()


def transaction_history():
    connection = create_connection()
    if connection is None:
        return

    cursor = None

    try:
        account_number = input("Enter account number: ").strip()

        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT transaction_type, amount, transaction_date
            FROM transactions
            WHERE account_number = %s
            ORDER BY transaction_date DESC
            """,
            (account_number,)
        )

        rows = cursor.fetchall()

        if rows:
            print("\n--- Transaction History ---")

            for row in rows:
                print(
                    row[0],
                    "| ₹", row[1],
                    "|", row[2]
                )
        else:
            cursor.execute(
                "SELECT account_number FROM accounts WHERE account_number = %s",
                (account_number,)
            )

            if cursor.fetchone():
                print("No transactions found.")
            else:
                print("Account not found.")

    except Exception as e:
        print("Error retrieving transaction history:", e)

    finally:
        if cursor:
            cursor.close()
        connection.close()


def main():
    while True:
        print("\n===== BANK ACCOUNT MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account()

        elif choice == "2":
            check_balance()

        elif choice == "3":
            deposit()

        elif choice == "4":
            withdraw()

        elif choice == "5":
            transaction_history()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
    main()
