import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
        print()
        print(f"Here is your itemized receipt of your order of {len(dictionary)} items found in your invoice.")
    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
        exit()
    return dictionary

def main():
    try:
        # Read products into a dictionary
        products_dict = read_dictionary('products.csv', 0)

        # Print the store name
        print()
        print("Inkom Emporium\n")

        # Open and read the request.csv file
        with open('request.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            
            # print("Requested Items")
            total_items = 0
            subtotal = 0.0
            sales_tax_rate = 0.06
            
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                
                try:
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    product_price = float(product_info[2])
                    
                    total_items += quantity
                    subtotal += product_price * quantity

                    print(f"{product_name}: {quantity} @ {product_price:.2f}")
                except KeyError as e:
                    print(f"Error: unknown product ID in the request.csv file\n{e}")
                    exit()

            sales_tax = subtotal * sales_tax_rate
            total = subtotal + sales_tax

            # Print totals and thank you message
            print(f"\nNumber of Items: {total_items}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales Tax: {sales_tax:.2f}")
            print(f"Total: {total:.2f}\n")
            print("Thank you for shopping at the Inkom Emporium.")


            # Print the current date and time
            current_datetime = datetime.now()
            print(current_datetime.strftime("%a %b %d %H:%M:%S %Y"))

            # Print survey invitation
            print("\nPlease complete our online survey at www.inkomemporium.com/customers/survey")
            print("to help us serve you better.")
            print()

    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file\n{e}")

if __name__ == "__main__":
    main()
