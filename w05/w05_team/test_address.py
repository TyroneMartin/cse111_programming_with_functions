from address import extract_city, \
   extract_state, extract_zipcode
import pytest


# test_extract_city 

def test_extract_city():
    city = extract_city("123 Main Street, Anytown, USA 12345")
    assert city == "Anytown"
    # or 
    assert extract_city("123 Main Street, Anytown, USA 12345") == "Anytown"
def test_extract_state():
    state = extract_state("123 Main Street, Anytown, USA 12345")
    assert state == "USA"
    # or 
    assert extract_state("123 Main Street, Anytown, USA 12345") == "USA"
    
def test_extract_zipcode():
    assert extract_zipcode("123 Main Street, Anytown, USA 12345") == "12345"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])