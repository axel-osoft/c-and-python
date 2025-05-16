#!/usr/bin/python

def my_badly_indented_function():
    returned_value = 0
    for index in range(20):
        returned_value += index * 2
        return returned_value  # indentation error

def my_correctly_indented_function():
    returned_value = 0
    for index in range(20):
        returned_value += index * 2
    return returned_value

print(my_badly_indented_function())
print(my_correctly_indented_function())
