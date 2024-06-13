import csv

def main():
    # student_list = read_dictionary("students.csv")
    # print(student_list)

    student_dict = read_compound_dictionary("students.csv", 0)
    print(student_dict)

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters:
        filename: the name of the CSV file to read.
    Return:
        A dictionary that contains the contents of the CSV file.
    """
    student_dict = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            student_dict[row[0]] = row[1]
    return student_dict

def read_compound_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return:
        A compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            compound_dict[key] = row
    return compound_dict

# Call main to start this program.
if __name__ == "__main__":
    main()
