#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num > 0 :
        print (num)
        num -= 1
    print("Happy New Year!")
    

def square_integers(int_list):
    return [int * int for int in int_list]
    # code goes here!


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    # code goes here!
