import urllib.request, ssl
import json
from Validators.string_is_float import isfloat
from Validators.is_page_valid import is_page_valid
from Validators.same_currency_validator import is_same
from Decorators.run_time import time_take


@time_take
def currency_conversion(from_page,from_currency,to_currecny,amt):
    content = from_page.read().decode("utf-8")
    data = json.loads(content)
    exchange_rate = data["rates"][to_currecny]
    converted_value = float(exchange_rate)*amt
    print("{} in {} = {} in {}".format(amt, from_currency, converted_value,to_currecny ))

def main():
    api_endpoint = "https://api.exchangerate-api.com/v4/latest/"
    ssl._create_default_https_context = ssl._create_unverified_context
    while True:
        amt = input("Please Enter Amount to be converted | 'q' or 'Q' to Quit: ")
        if amt == 'q' or amt == 'Q':
            print("See you Again!!")
            break
        if not isfloat(amt):
            print("Invalid amount {}".format(amt))
            continue
        amt = float(amt)
        # check if FROM currency valid
        from_currency = input("\nPlease Enter FROM Currency 3 letter code: ")
        temp1 = api_endpoint + from_currency
        if not is_page_valid(temp1, from_currency): continue
        from_page = urllib.request.urlopen(temp1)

        # check if TO currency valid
        to_currency = input("\nPlease Enter TO Currency 3 letter code: ")
        temp2 = api_endpoint + to_currency
        if not is_page_valid(temp2, to_currency): continue

        #Currency Conversion
        if not is_same(from_currency,to_currency,amt):
            currency_conversion(from_page,from_currency, to_currency, amt)
        else:
            print("{} in {} = {} in {}".format(amt,from_currency,amt,to_currency))


if __name__ == '__main__':
    main()
