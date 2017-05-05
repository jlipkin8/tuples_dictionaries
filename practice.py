"""
Complete the code to pass all the tests
"""


def get_first_element_of_tuple(employee):
    """Return the first element of a tuple.

    >>> employee_record = ('Brighticorn', 1)
    >>> get_first_element_of_tuple(employee_record)
    'Brighticorn'
    """

    # ADD YOUR CODE HERE
    return employee[0] 


def get_number_of_horses(animals):
    """Given a dict of animals and counts, return the number of horses.

    >>> my_animals = {'horses': 3, 'ducks': 12, 'iguanas': 103}
    >>> get_number_of_horses(my_animals)
    3
    """

    # ADD YOUR CODE HERE
    return animals["horses"]


def change_number_of_ducks(animals, duck_number):
    """Change the value for the 'ducks' key in the dict animals to duck_number.

    >>> my_animals = {'horses': 3, 'ducks': 12, 'iguanas': 103}
    >>> change_number_of_ducks(my_animals, 23)
    >>> my_animals['ducks']
    23
    """

    # ADD YOUR CODE HERE
    pass


def neigh_for_horses(animals):
    """If horses exists in the animals dict, print "neigh". Otherwise print "no".

    >>> my_animals = {'horses': 3, 'ducks': 12, 'iguanas': 103}
    >>> neigh_for_horses(my_animals)
    neigh
    
    >>> my_animals = {'hipsters': 3, 'ducks': 12, 'iguanas': 103}
    >>> neigh_for_horses(my_animals)
    no
    """

    # ADD YOUR CODE HERE
    pass



#####################################################################
# Don't touch the code below!
# This is just allowing us to run the doctests

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
