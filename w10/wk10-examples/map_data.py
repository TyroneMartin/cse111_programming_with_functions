# Author: Brother Keers
# Copyright 2023 Brigham Young University Idaho.

import csv

NAME_INDEX    = 0
EMAIL_INDEX   = 1
PHONE_INDEX   = 2
COUNTRY_INDEX = 3

def main():

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

        for customer in customers:
            print(customer)
        print()

    # We only want the customers names
    # customer_names = [] # This is how you would normally think to solve this.
    
    with open("customers.csv", "r") as customers_file:

        # Use pythons built-in CSV reader to read the CSV into a list of rows.
        csv_reader = csv.reader(customers_file)

        # Skip the file header.
        next(csv_reader)

        # Cast (convert) the CSV reader object into a plain old list.
        csv_reader = list(csv_reader)
        
        # This is how you would normally think to solve this.
        # for row in csv_reader:
        #     customer_names.append(row[NAME_INDEX])

        # Use pythons map function to do the same as the commented out for loop above.
        customer_names = list(map(lambda row: row[NAME_INDEX], csv_reader))

    # Show the various results.
    print_customers(customer_names, "Unsorted")
    customer_names = sorted(customer_names)
    print_customers(customer_names, "Sorted")

if __name__ == "__main__":
    main()