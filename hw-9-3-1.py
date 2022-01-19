# MEE 1/18/22


def temp():
    while True:
        try: 
            temp = float(input("Input the temperature: "))
            type = input("Do you want to convert to (f/C)").upper()
            if type == "C":
                result = (temp - 32) * 5 / 9
                print("The temperature is {0} degrees celcius.".format(result))
            elif type == "F":
                result = temp / 5 * 9 + 32
                print("The temperature is {0} degrees fahrenheit.".format(result))
            else:
                print("Bad input, enter either f for fahrenheit or c for celsius.")
        except ValueError:
            print("Bad input, enter a numerical value for the temperature")


temp()