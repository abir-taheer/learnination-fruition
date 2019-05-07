from time import time
from random import randrange
import v1, v2, v3

methods = [v1, v2, v3]

# Alter these variables to change the testing environment

# This will alter the number of times that the trials are executed (For Precision)
num_trials = 3

# This will alter the number of items in the test_list
num_items = 1000

# The range of possible numbers that can be items in the test_list
range_possible_unique_items = 1000

for trial in range(1, (num_trials + 1)):
    test_list = [randrange(range_possible_unique_items) for x in range(num_items)]

    print("Trial", trial, ":", str(num_items) + " items")
    for method in methods:
        start = time()
        mode = method.mode(test_list)
        speed = time() - start
        print(method.name, str(speed) + " seconds")

    print("---------------")
