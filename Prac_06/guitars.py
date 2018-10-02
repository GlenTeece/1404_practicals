from Prac_06.guitar import Guitar

MENU = "Would you like to:\n(A)dd a guitar\n(L)ist guitars\n(Q)uit"


def main():
    guitars = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "A":
            # name = input("Name: ")
            # year = input("Year: ")
            # cost = input("Cost: ")
            # new_guitar = Guitar(name,year,cost)
            # guitars.append(new_guitar)
            guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
            guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
        elif choice == "L":
            print("These are my guitars")
            for i, guitar in enumerate(guitars):
                vintage_string = " (vintage)" if guitar.is_vintage() else ""
                print("Guitar {}: {:>15} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                          vintage_string))
        else:
            print("Invalid Option")
        print(MENU)
        choice = input(">>> ").upper()


main()
