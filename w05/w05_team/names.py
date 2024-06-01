# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def make_full_name(given_name, family_name):
    """Return a string in this form "family_name; given_name". For
    example, if this function were called like this:
    make_full_name("Sally", "Brown"), it would return "Brown; Sally".

    Parameters
        given_name: a string that contains a person's given name
        family_name: a string that contains a person's family name
    Return: a string in the form "family_name; given_name"
    """
    full_name = f"{family_name}; {given_name}"

    return full_name

print(make_full_name("Brown", "Sally"))

def extract_family_name(full_name):
    """Extract and return the family name from a string in this form:
    "family_name; given_name". For example, if this function were
    called like this:
    extract_family_name("Brown; Sally"), it would return "Brown".

    Parameter:
        full_name: a string in the form "family_name; given_name"
    Return: a string that contains a person's family name
    """
    # Split the full name string by "; " and return the first part.
    family_name = full_name.split("; ")[0]
    return family_name

# Test the function with a sample input
print(extract_family_name("Brown; Sally"))



def extract_given_name(full_name):
    """Extract and return the given name from a string in this form:
    "family_name; given_name". For example, if this function were
    called like this:
    extract_given_name("Brown; Sally"), it would return "Sally".

    Parameter:
        full_name: a string in the form "family_name; given_name"
    Return: a string that contains a person's given name
    """
    # Split the full name string by "; " and return the second part.
    given_name = full_name.split("; ")[1]
    return given_name

# Test the function with a sample input
print(extract_given_name("Brown; Sally"))

