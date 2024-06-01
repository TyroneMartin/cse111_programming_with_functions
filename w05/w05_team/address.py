# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def extract_city(full_address):
    """Extract and return the name of a city from
    a properly formatted U.S. mailing address.
    Parameter
        full_address: a U.S. mailing address in this format:
            number and street, city, state zipcode
    Return: the city name
    """
    city = full_address.strip().split(", ")[1]
    return city
print(extract_city("123 Main Street, Anytown, USA 12345"))


def extract_state(full_address):
    """Extract and return the two letter abbreviation for
    a state from a properly formatted U.S. mailing address.
    Parameter
        full_address: a U.S. mailing address in this format:
            number and street, city, state zipcode
    Return: the two letter state abbreviation
    """
    state = full_address.strip().split(", ")[2].split(" ")[0]
    return state
print(extract_state("123 Main Street, Anytown, USA 12345"))



def extract_zipcode(full_address):
    """Extract and return the ZIP code from
    a properly formatted U.S. mailing address.
    Parameter
        full_address: a U.S. mailing address in this format:
            number and street, city, state zipcode
    Return: the ZIP code
    """
  
    zipcode = full_address.strip().split(", ")[2].split(" ")[1]
    
    return zipcode
print(extract_zipcode("123 Main Street, Anytown, USA 12345"))
