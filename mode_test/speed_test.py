from time import time, sleep
from random import randrange
import v1, v2, v3

methods = [v1, v2, v3]

# Alter these variables to change the testing environment
num_trials = 3
num_items = 1000
num_possible_unique_items = 100000

for trial in range(1, (num_trials + 1)):
    test_list = [randrange(num_possible_unique_items) for x in range(num_items)]

    print("Trial", trial, ":", str(num_items) + " items")
    for method in methods:
        start = time()
        mode = method.mode(test_list)
        speed = time() - start
        print(method.name, str(speed) + " seconds")

    print("---------------")
