from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest



def test_make_full_name():
   
   """Verify that the make_full_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
   full_name = make_full_name("Sally", "Brown")
   assert full_name == "Brown; Sally"
   assert make_full_name("Ava", "Smith-Jones") == "Smith-Jones; Ava"


# This passed test_extract_family_name()
def test_extract_family_name(): 
    """Verify that the extract_family_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    family_name = extract_family_name("Brown; Sally")
    assert family_name == "Brown"
    assert extract_family_name("Madison; James") == "Madison"

def test_extract_given_name():
    """Verify that the extract_given_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    given_name = extract_given_name("Brown; Sally")
    assert given_name == "Sally"
    assert extract_given_name("Madison; James") == "James"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
