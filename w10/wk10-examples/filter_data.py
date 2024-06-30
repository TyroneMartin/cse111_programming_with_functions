# Author: Brother Keers
# Copyright 2023 Brigham Young University Idaho.

import csv

NAME_INDEX    = 0
EMAIL_INDEX   = 1
PHONE_INDEX   = 2
COUNTRY_INDEX = 3

def main():

    # This is a nested function.
    def print_customers(customers, title):
        """
        Prints a list of customer data in an easy to view format.

        Parameters:
            customers (list): A list of customers to print.
            title (str): What to title the print out.
        """
        print(f"\n{'=' * 30}")
        print(title.upper())
        print(f"{'=' * 30}")

        for cus in customers:
            print(f"{cus[NAME_INDEX]:<18} {cus[EMAIL_INDEX]:<28} {cus[PHONE_INDEX]}")
        print()

    # Get all Americans and Canadians so we can send them a discount code.
    americans = []
    canadians = []
    
    with open("customers.csv", "r") as customers_file:

        # Use pythons built-in CSV reader to read the CSV into a list of rows.
        csv_reader = csv.reader(customers_file)

        # Remove file header
        next(csv_reader) 

        # Cast (convert) the CSV reader object into a plain old list.
        csv_reader = list(csv_reader)

        # Get all Americans.
        usa_filtered = filter(lambda customer: customer[COUNTRY_INDEX].strip().upper() == "USA", csv_reader)
        # Get all Canadians.
        can_filtered = filter(lambda customer: customer[COUNTRY_INDEX].strip().upper() == "CAN", csv_reader)

        # Filter returns a filter object, cast (convert) it to a list.
        americans = list(usa_filtered)
        canadians = list(can_filtered)

    # Sort the lists alphabetically.
    americans = sorted(americans, key=lambda customer: customer[NAME_INDEX])
    canadians = sorted(canadians, key=lambda customer: customer[NAME_INDEX])

    # Show the results.
    print_customers(americans, "Americans")
    print_customers(canadians, "Canadians")


if __name__ == "__main__":
    main()