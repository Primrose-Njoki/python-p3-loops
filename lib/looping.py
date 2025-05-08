#!/usr/bin/env python3

def happy_new_year():
    counter=10
    while counter >0:
        print (counter)
        counter-=1
    print("Happy New Year!")
happy_new_year()

    # code goes here!
    #pass

def square_integers(int_list):
    return [num ** 2 for num in int_list]
print(square_integers([1,2,3,4,5]))
# def square_integers(int_list):
#     return [num ** 2 for num in int_list]
    
# print(square_integers([1,2,3,4,5]))  # Should output [1, 4, 9, 16, 25]

    
    # code goes here!
    #pass

def fizzbuzz():
    for num in range(1,101):
        if num % 3==0 and num % 5==0:
            print('FizzBuzz')
        elif num % 3==0:
            print("Fizz")
        elif num % 5==0:
            print("Buzz")
        else :
            print(num)

fizzbuzz()
        
    # code goes here! pass
