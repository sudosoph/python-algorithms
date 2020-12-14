#!/usr/bin/env python3

"""
Author : Sophia
Date   : 2020-12-14
Purpose: Binary Search implementation in Python
"""


# --------------------------------------------------
def binary_search(list, item):
    """ Divides sorted list in half and changes bound until item is found """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# --------------------------------------------------
def main():
    """ Call algorithm function """
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))  # => 1, found at index 1
    print(binary_search(my_list, -1))  # => None, not found


# --------------------------------------------------
if __name__ == "__main__":
    main()
