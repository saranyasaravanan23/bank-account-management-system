# Bank Account Management System

## 1. Project Overview
The Bank Account Management System is a Python-based application connected to a MySQL database. It allows users to manage bank accounts and perform basic transactions.

## 2. Technologies Used
- Python
- MySQL
- MySQL Connector/Python
- Visual Studio Code

## 3. Project Features
- Create Account
- Check Balance
- Deposit Money
- Withdraw Money
- View Transaction History
- Validate Account Details
- Check Insufficient Balance

## 4. Database Structure
**Accounts Table:** Stores account number, customer name, phone number, account type, balance, and creation date.

**Transactions Table:** Stores transaction ID, account number, transaction type, amount, and transaction date.

## 5. How to Run the Project
1. Install Python and MySQL.
2. Install the MySQL connector using `python -m pip install mysql-connector-python`.
3. Create the database and tables in MySQL Workbench.
4. Configure the database connection in `database.py`.
5. Run `python main.py` in the terminal.

## 6. Testing
The application was tested for account creation, balance checking, deposit, withdrawal, transaction history, insufficient balance, and invalid account number.

## 7. Conclusion
This project demonstrates Python programming, MySQL connectivity, database operations, and basic banking transaction management.
