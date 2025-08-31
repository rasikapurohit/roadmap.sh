"""
Build a simple expense tracker application to manage your finances. The application should allow users to add, delete, and view their expenses. The application should also provide a summary of the expenses.

Requirements
Application should run from the command line and should have the following features:

Users can add an expense with a description and amount.
Users can update an expense.
Users can delete an expense.
Users can view all expenses.
Users can view a summary of all expenses.
Users can view a summary of expenses for a specific month (of current year).
Here are some additional features that you can add to the application:

Add expense categories and allow users to filter expenses by category.
Allow users to set a budget for each month and show a warning when the user exceeds the budget.
Allow users to export expenses to a CSV file.
"""

import datetime
import argparse

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument('filename')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag
args = parser.parse_args()
print(args.filename, args.count, args.verbose)