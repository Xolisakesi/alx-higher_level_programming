#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x integers from the list and returns the real number of integers printed."""
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print("")
    except (IndexError, ValueError, TypeError):
        pass
    return count
