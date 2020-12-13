# Ex. M - 6

# Print the multiplication table for numbers from 1 up to 10.

val1 = 1
val2 = 1
while val1 <= 10:
    while val2 <= 10:
        val3 = val1 * val2
        print("%d x %d = %d" % (val1, val2, val3))
        val2 += 1
    print("*" * 15)
    val2 = 1
    val1 += 1