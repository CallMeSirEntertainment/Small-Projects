from time import sleep
while True:
    try:
        old = float(input("Old number: "))
        new = float(input("New number: "))
        decimal = input("Decimal place to round to: ")
        if decimal == '':
            decimal = 0
        else:
            decimal = int(decimal)
        if old == 0:
            poc = "undefined (division by zero)"
            status = "N/A"
        else:
            poc = round(abs((new - old) / old * 100), decimal)
            status = "decrease" if old > new else "increase" if old < new else "equal"
            if status == "equal":
                poc = 0
        if input(f"\n{poc}% {status}.\nPress enter to continue or 'quit' to quit.\n").lower() == 'quit':
            print("\nProgram created by CallMeSirEntertainment.\nThanks for using!")
            sleep(2.5)
            quit()
    except ValueError:
        print("Invalid input. Please enter numeric values.")