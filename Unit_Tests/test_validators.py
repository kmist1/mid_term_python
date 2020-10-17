
from Validators.same_currency_validator import is_same
from Validators.is_page_valid import is_code_valid
from Validators.is_page_valid import is_page_valid


def test_sameCurrencyCode():
    assert is_same("USD","USD",2.0) == 2.0
    assert is_same("INR","INR",5.0) == 5.0

def test_lowerCaseInputCode():
    assert is_code_valid("ert") == False
    assert is_code_valid("usd") == False

def test_upperCaseInputCode():
    assert is_page_valid(" https://api.exchangerate-api.com/v4/latest/", "TTT") == False
