# map, filter, zip, and reduce

from functools import reduce
my_list = [1,2,3]


def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))

print(my_list)

# map, filter, zip, and reduce

from functools import reduce
my_list = [1,2,3]


def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 10))

print(my_list)

