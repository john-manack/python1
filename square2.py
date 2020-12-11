#Ex. S-10

user_number = input("How big is the square?")

number = int(user_number)
def square(num1):
    line = num1 * "*"
    print((line + "\n") * num1)

square(number)