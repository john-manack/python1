#Ex M - 4: Print a box.

# Given a height and width, input by the user, print a box consisting of * characters as its border.

width = int(input("Enter width:"))
height = int(input("Enter height:"))

print("*" * width)

val1 = 1
while val1 < (height - 1):
    print("*" + (" " * (width - 2) + "*"))
    val1 += 1
    
print("*" * width)