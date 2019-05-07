# Mode Speed Test
### Steps:
#### Method 1:
1. Download this folder with all files inside.
2. Run the [*speed_test.py*](https://github.com/abir-taheer/learnination-fruition/blob/master/mode_test/speed_test.py) file `python3 speed_test.py`
    * Make sure that the [*v1.py*](https://github.com/abir-taheer/learnination-fruition/blob/master/mode_test/v1.py), [*v2.py*](https://github.com/abir-taheer/learnination-fruition/blob/master/mode_test/v2.py), and [*v3.py*](https://github.com/abir-taheer/learnination-fruition/blob/master/mode_test/v3.py) are located in the same directory

#### Method 2:
1. Download the [*mode_test.zip*](https://raw.githubusercontent.com/abir-taheer/learnination-fruition/master/mode_test/mode_test.zip) file
2. Unzip the file
3. Run the [*speed_test.py*](https://github.com/abir-taheer/learnination-fruition/blob/master/mode_test/speed_test.py) file `python3 speed_test.py`

#### Testing Environments
Alter these variables at the top of the [*speed_test.py*](https://github.com/abir-taheer/learnination-fruition/blob/master/mode_test/speed_test.py) file and see how the runtime for the different methods change

`num_trials`: This will alter the number of times that the trials are run. Use this to test consistency and precision.

`num_items`: This is how many items are in the sample space. It will change the number of items the mode functions need to iterate through. Changes quantity.

`range_possible_unique_items`: The range of possible values in the sample space. Does not affect quantity of items in sample space. Affects how varied the numbers are and how many times the mode might appear.