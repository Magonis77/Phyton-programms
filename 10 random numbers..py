from random import randint

print("Hello person!")
print()

print("This program will show you 10 random numbers depending on what numbers you entered as minimum and maximum!")
print()

print("Enjoy :)")
print()

print("Enter number minimum and number maximum!")
print()

print(" Keep in mimnd to have at least 10 numbers in between maximum and minimum")
print()

min_str = input("Number Minimim: ")
max_str = input("Number Maximum: ")


minimum = int(min_str)
maximum = int(max_str)

if maximum > minimum:
    random1 = randint(minimum, maximum)
    random2 = randint(minimum, maximum)
    random3 = randint(minimum, maximum)
    random4 = randint(minimum, maximum)
    random5 = randint(minimum, maximum)
    random6 = randint(minimum, maximum)
    random7 = randint(minimum, maximum)
    random8 = randint(minimum, maximum)
    random9 = randint(minimum, maximum)
    random10 = randint(minimum, maximum)
    print(str(random1) + " " + str(random2) + " " + str(random3) + " " + str(random4)+ " " + str(random5)+ " " + str(random6)+ " " + str(random7)+ " " + str(random8)+ " " + str(random9)+ " " + str(random10))
else:
    print(str(maximum) + " is less than " + str(minimum))

print()
input("Press return to continue ...")
