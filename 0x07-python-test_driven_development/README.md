# 0x07. Python -
## Test Driven Development
This project introduced us to Test Driven Development in Python  
Test-Driven Development (TDD) is a software development methodology that emphasizes writing tests   before the actual code.   
It's a cyclical process that involves writing a failing test, writing the minimum code to pass the test, and then refactoring the code.  

The process of TDD can be summarized into the following steps:
    - Write a single unit test describing an aspect of the program.  
    - Run the test, which should fail because the program lacks that feature.  
    - Write just enough code, the simplest possible, to make the test pass.  
    - Refactor the code until it conforms to the simplicity criteria.  

TDD is considered a specification technique as it ensures that your source code is thoroughly tested at the confirmatory level. By focusing on writing only the code necessary to pass tests, designs can often be cleaner and clearer than is achieved by other methods 2.

### Benefits of TDD include:

    Improved code quality: 
        - TDD ensures that all written code is covered by at least one test, providing a greater level of confidence in the code.
    Early bug detection: 
        - The early and frequent nature of the testing helps to catch defects early in the development cycle.
    Simplified code:   
        - TDD often results in simpler and clearer code because it encourages developers to write only the code necessary to pass tests.
    Easier refactoring:   
        -The presence of a good set of unit tests makes refactoring, or improving the code structure, a lot easier and safer.
    Improved productivity:   
        Studies have shown that programmers who wrote more tests tended to be more productive.

## Project Tasks
### Task 0: Integers addition
Implemented a function that adds two integers and wrote several test cases. These cases were run using doctest  
### Task 1: Divide Matrix
Here, we have a function that divides every element of a given matrix by a given value. Test cases were written and run with doctest to check for as many error possibilities as i cou;d think off
### Task 2: Say my name  
The function here is meant to print a sentence with given format  
Test cases written and run with doctest method, while handling exceptions
### Task 3: Print square
This program consists of a function that prints a square with '#' character.  
Test cases were implemented and exceptions handled for invalid input data  
### Task 4: Text indentation
Our program here is meant to handle given text with indentation and print two newlines everytime  
it comes across a ., : or ?  
As with the above, its own test cases were implemented and run with doctest  
### Task 5: Max integer  
This program returns highest integer from among list of integers.  
The test cases here were implemented using unittest module  
### Task 6: Matrix multiplication  
As the name suggests, this program carries out matrix multiplication  
It's test cases for the possible errors were written and implemented with doctest.  
### Task 7: Lazy matrix multiplication   
This program works same as in task 6 but we used the Numpy module to implemented the multiplication  
Test cases are the same as in  task 6, implemented with doctest  
### Tests:  
All test cases are saved in their respective corresponding files in the tests folder  
