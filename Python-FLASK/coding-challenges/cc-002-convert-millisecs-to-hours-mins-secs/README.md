# Coding Challenge - 002 : Convert Milliseconds into Hours, Minutes, and Seconds

Purpose of the this coding challenge is to write program that converts the given milliseconds into hours, minutes, and seconds.

## Learning Outcomes

At the end of the this coding challenge, students will be able to;

- analyze a problem, identify and apply programming knowledge for appropriate solution.

- design, implement `while` loops effectively in Python to solve the given problem.

- control loops effectively by using `if` and `control` statements.

- apply arithmetic operations on basic data types in Python.

- demonstrate their knowledge of string manipulations and formatting in Python.

- demonstrate their knowledge of algorithmic design principles by using function effectively.

   
## Problem Statement

- Write program that converts the given milliseconds into hours, minutes, and seconds. The program should convert only from milliseconds to hours/minutes/seconds, not vice versa and during the conversion following notes should be taken into consideration.

   - If the calculated time of hours is 0, it should not be shown in the output.

   - If the calculated time of minutes is 0, it should not be shown in the output.

   - If the calculated time of seconds is 0, it should not be shown in the output.

   - If the milliseconds is greater than 1000, remainder milliseconds should not be shown in the output.

   - If milliseconds given is less than 1000, only milliseconds should be shown in the output.

   - Output should always be string in the format shown in the examples.

- Program should ask user for the input, after giving information text show as below.

```text
###  This program converts milliseconds into hours, minutes, and seconds ###
(To exit the program, please type "exit")
Please enter the milliseconds (should be greater than zero) :  
```

- User input can be either integer or string, thus the input should be checked for the followings,

   - The input should be a decimal number greater then zero.
   
   - If the input is less then 1, user should be warned and asked for input again.

   - If the input is string and can not be converted to decimal number, user should be warned and asked for input again.

- Program should run until the user types `exit` in case insensitive manner.
   
- Example for user inputs and respective outputs

```
Input             Output
(milliseconds)    (Calculated Time) 
--------------    -----------------
555               just 555 millisecond/s
2001              2 second/s
60011             1 minute/s
122011            2 minute/s 2 second/s
3661011           1 hour/s 1 minute/s 1 second/s
7200011           2 hour/s
7322011           2 hour/s 2 minute/s 2 second/s
-8                "Not Valid Input !!!"
Ten               "Not Valid Input !!!"
Exit              "Exiting the program... Good Bye"
```
