# Created by: Zack Isingoma
# Created on: 24th Jan 2022.
# Works as a nomal calculator

def calculate(sign, num1, num2):
    if sign in ('1', '2', '3', '4'):
        if sign == '1':
            print(num1, "+", num2, "=", (num1 + num2))

        elif sign == '2':
            print(num1, "-", num2, "=", (num1 - num2))

        elif sign == '3':
            print(num1, "*", num2, "=", (num1 * num2))

        elif sign == '4':
            print(num1, "/", num2, "=", (num1 / num2))


def main():

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    sign = input("Enter choice(1/2/3/4): ")
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if sign in ('1', '2', '3', '4'):
        try:
            num1_float = float(num1)
            num2_float = float(num2)
        except Exception:
            print("Invalid input")

    calculate(sign, num1_float, num2_float)


if __name__ == "__main__":
    main()
