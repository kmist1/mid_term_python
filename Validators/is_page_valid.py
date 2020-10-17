from Validators.currenecy_is_valid import page_exists
import re


def is_page_valid(page, currencyCode):
    if not is_code_valid(currencyCode):
        return False
    if not page_exists(page):
        print("Invalid Currency code {}".format(currencyCode))
        return False
    return True


def is_code_valid(currencyCode):
    regexp = re.compile("^[A-Z]{3}$")
    if not regexp.search(currencyCode):
        print("Invalid Currency code {}".format(currencyCode))
        return False
    else:
        return True