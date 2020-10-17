from Validators.string_is_float import isfloat
import urllib


def main():
    api_endpoint = "https://api.exchangerate-api.com/v4/latest/"
    while True:
        amt = input("Please Enter Amount to be converted | 'q' or 'Q' to Quit: ")
        if amt == 'q' or amt == 'Q':
            print("See you Again!!")
            break
        if not isfloat(amt):
            print("Invalid amount {}".format(amt))
            continue
        from_currency = input("\nPlease Enter FROM Currency 3 letter code: ")
        #check if currency valid
        from_page = urllib.request.urlopen(api_endpoint+from_currency)
        

        to_currency = input("\nPlease Enter TO Currency 3 letter code: ")


if __name__ == '__main__':
    main()
