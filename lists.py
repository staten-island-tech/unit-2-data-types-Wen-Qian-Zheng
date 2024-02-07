# animals = ["Zebra", "Camel", "Ape"]
# stars count at 0, reference each element with []
# print(animals[0])
# for animal in animals:
#     print(animal)

# for animal in animals:
#     if(animal == "Camel"):
#         print("We're in the desert")

# # Strings operate like lists
# x = "Hello Freshman, you all smell"
# print(x[0])

# So when you do that ^ since the count starts at 0, it takes the first letter, H

# y = x.upper()
# print(y)

# ^ NOW THEY'RE ALL IN CAPS WOAH

# words_list = x.split(",")
# print(words_list)

# So here, it found that comma and split the string based on where the comma is

# words_list = x.split(" ")
# print(words_list)

# ^ In this way, we can find how many spaces there are and it would separate
# Das cool

# words_list = x.split()
# print(len(words_list))

# So if you do that you find how many words there are in a sentence

# THE END

# temp = 75
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:
#     print('cold')



# Let's create a function that determines if a number is odd or even
# number = 5
# if number%2 == 0:
#     print('Even')
# else:
#     print('Odd')


# Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ".

bill = int(input("How much was your bill in integer?: "))
service = input("Service was:")

total = 0

if service == "bad":
    print("0% tip")
    total = round(bill, ndigits=2)
    print(f"Your total is ${total}.00")
elif service == "okay":
    print("15% tip")
    total = round(bill * 1.15, ndigits=2)
    print(f"Your total is ${total}0")
elif service == "good":
    print("20% tip")
    total = round(bill * 1.20, ndigits=2)
    print(f"Your total is ${total}0")
elif service == "great":
    print("25% tip")
    total = round(bill * 1.25, ndigits=2)
    print(f"Your total is ${total}0")


# x = input("Tree")
# if(int(x) < 5)