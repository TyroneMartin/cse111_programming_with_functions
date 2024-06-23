import csv

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
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

def main():
    # Read products into a dictionary
    products_dict = read_dictionary('products.csv', 0)
    
    # Print the products dictionary
    print("All Products")
    print(products_dict)

    # Open and read the request.csv file
    with open('request.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        print("\nRequested Items")
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            product_info = products_dict.get(product_number, None)
            
            if product_info:
                product_name = product_info[1]
                product_price = product_info[2]
                print(f"{product_name}: {quantity} @ {product_price}")

if __name__ == "__main__":
    main()
