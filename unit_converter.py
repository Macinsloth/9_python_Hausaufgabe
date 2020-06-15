print("Hello! I convert kilometers to miles for you.")

while True:
    print("Please enter the number of kilometers you would like to convert into miles. Only numbers are allowed.")
    km = input("Kilometer:")
    km = float(km.replace(",", "."))
    miles = km * 0.621371
    print("{0} kilometers is {1} miles.".format(km, miles))
    choice = input("Would you like to do another conversion (y/n):")
    if choice.lower() != "y" and choice.lower() != "yes":
        print("Goodbye!")
        break