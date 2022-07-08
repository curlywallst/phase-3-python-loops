#!/usr/bin/env python3

def happy_new_year():
    for i in range(10):
        print(10 - i)
    print("Happy New Year!")

def square_integers(int_list):
    new_list = []
    for num in int_list:
        new_list.append(num * num)
    return new_list


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)


