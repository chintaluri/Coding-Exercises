# Fizz Buzz
# This is a children's game where player's take turns to count, replacing any number divisible by three
# with the word "fizz" and any number divisible by five with the word "buzz".
# Write a program that does this for the first 100 numbers.
# Example output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11


for i in range(1,101):

    if i % 3 == 0:
        print('Fizz')
        i = i + 1

    elif i % 5 == 0:
        print("Buzz")
        i = i + 1

    else:
        print(i)

