print("Make your string lowercase")

while True:
    string_1 = input("Paste your string here:")

    print(string_1.lower())

    choice = input("Do you want to continue? (y/n)")
    if choice.lower() != "y" and choice.lower() != "yes":
            print("Goodbye")
            break
