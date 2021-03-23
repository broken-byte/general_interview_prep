# Mock Interview Solutions
A collection of solutions to problems I've attempted in the context of 
either 1 on 1, 45/35/30 minute mock programming interviews
using [Pramp](https://www.pramp.com/dashboard#/) and [LeetCode](https://leetcode.com/),
or just questions I've attempted solo that I feel are beneficial to me. 


### Installation
If, for some reason, you want to use the dynamic test creator I use here infrequently, than
simply follow the instructions below:

----------------------------------------------------------------------------


1. Clone the repo!

2. Navigate to the generated directory and within your terminal, run:

    `python3 -m venv env`
    
    if you haven't installed python virtual environments before, look up just that, then run:
    
    `pip install virtualenv`
    
    If you haven't installed pip, it's a package manager for Python, so look it up and install :)
3. run:

    `source env/bin/activate`
    
    to activate your virtual environment. You should see a `(env)` in front of your terminal
    prompt now.
    
4. run:
    
    `pip install -r dependencies.txt`
    
    to install the dependencies for the test environment. 
    
5. Specify the source/root directory in your IDE. This is super important as Python needs a
    root directory so that it can import things correctly. 
    
    I use PyCharm Community Edition (I highly suggest you do the
    same for Python development) so to specify the source I go to Preferences -> Project -> 
    Project Structure and right click the top level of this git repo and check "Sources". The
    top level directory should now be blue, or some such color depending on your IDE theme. 
    
6. Specify your SDK. This synchronizes your IDE with the virtual environment we created in step 3.
    
    in Pycharm, simply go to Preferences -> Project -> Project Interpreter and in the python interpreter
    drop-down select the Python source that lies in your virtual env directory. Mine is in 
    env/bin/python.
    
5. You're all set! :)

How to Use
------------
 I've already written test data for the challenges I've done. all the test data is in the 
 respective directories of each challenge, inside the test_resources folder. I've separated
 the functionality tests from the time complexity tests in their respectively named files.
 
 #### Example (if you want to add a new problem from Hacker Rank)
 I have a challenge called Fraudulent Activity, and it has some functional tests, and some time
 complexity tests on Hacker Rank. So, I get the functional tests from the problem page, and the 
 time complexity tests from the test file download link on that same page that appears once you run
 the tests in their web IDE. I make a functionality_test_data dictionary as such:
 ```
functionality_test_data: dict = {
    "test_0": {
        "params": {
            "expenditure": [2, 3, 4, 2, 3, 6, 8, 4, 5],
            "d": 5
        },
        "expected": 2
    },
    "test_1": {
        "params": {
            "expenditure": [1, 2, 3, 4, 4],
            "d": 4
        },
        "expected": 0
    },
    "test_2": {
        "params": {
            "expenditure": [10, 20, 30, 40, 50],
            "d": 3
        },
        "expected": 1
    }
}
```
As you can see, the params for the function you want to test need to be specified explicitly here.
That's important for the dynamic test creation part. Also, every test name NEEDS to start with "test",
since im using the built-in unittest framework, and it will only run tests named "test_...".

I then make a time complexity test file like so:
```
import os

from test_utilities.time_complexity_file_processing_functions import \
    process_test_file_where_single_line_is_an_int_array

current_path = os.path.dirname(__file__)

time_complexity_test_data: dict = {
    "test_time_complexity_0": {
        "params": {
            "expenditure": process_test_file_where_single_line_is_an_int_array(current_path +
                                                                               "/time_complexity_test_0.txt"),
            "d": 10000
        },
        "expected": 633
    },
}
```
Notice how I'm importing/using that process_file function. I created a text file which holds the
insanely long time complexity test data (the expenditure list in this case). The process file function
is simply how I load it into Python's main memory for use. 

Now, I create a brute_force.py function and import my test data, and the dynamic test creator/runner
that rests in the test_utilities directory, like so:
```
from sorting.medium_problems.fraudulent_activity.test_resources.functionality_test_data import \
    functionality_test_data
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests

def fraudulent_notifications(expenditure: list, d: int) -> int:
    pass
```
Once I have that, I can use those imported functions/data as such:
```
if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, fraudulent_notifications)
    run_dynamic_tests()
```
And Voilà! I now simply run the file, and a full, data driven suite of tests is automatically 
generated and run, with full text output in you console!

For the time complexity tests, I like to combine the functional and time complexity tests into one
dictionary so that they all run in the same test suite, like so:
```
functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, fraudulent_notifications)
    run_dynamic_tests()
```
The dynamic_test generator has some additional configurability, such as timing and a timeout so
your computer doesn't crash on those crazy long time complexity tests.

For example, if I wanted to add timing to the tests, I would simply do the following:
```
if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, fraudulent_notifications, timed=True)
    run_dynamic_tests()
```
Now, when you run the tests, you should see how long your function took in your IDE console. 
(in seconds). By default, there exists a timeout of 60 seconds, so if your function takes longer
than that, it will stop and save your computer. To reduce or increase that number, simply
specify the timeout parameter:
```
if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, fraudulent_notifications, timeout=3)
    run_dynamic_tests()
```
Here I set it to 3 seconds!

Of course, you can time AND have a timeout:
```
if __name__ == "__main__":
    functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, fraudulent_notifications, timed=True, timeout=3)
    run_dynamic_tests()
```
