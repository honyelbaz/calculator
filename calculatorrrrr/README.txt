Calculator

# User

Demands: python3.6

There are 3 ways to start the application.

1. run the "startCalculator.bat" file.
2. open a cmd in the "Calculator2" directory and run the command "python main.py"
3. open the *"calculator2"!!! project in a python editor that can run
python files and run the main.py file


dear user
This application is a calculator application.

Once the application is running you enter your equations in the command line
and receive results.
to stop it, insert stop.
if the equations is not valid the calculator will print
the reason.
the application supports 11 different base operators.
int 3 categories and strengths
The strongest operator operates first

-- in between two numbers operators
    + = adding          1 (strengths)
    - = subtracting     1
    * = multiplying     2
    / = dividing        2
    ^ = powering        3
    % = modulus         4
    @ = average         5
    $ = maximum         5
    & = minimum         5

-- to the right of a number
    ! = factorial       6

-- to the left of a number
    ~ - multiply by minus one but strong priority   6

- this application supports correct usage of brackets
((5 + 5)) unnecessary brackets will not be accepted

- this application supports big numbers at the form of (number1)e+(number2)
which means : number1 multiplied by ten to the power of number2

- this application does not support complex numbers at all


# Developer

Dear developer
you need to read the User section too.

--The solving technique:
after checking if a string is valid, we go over all the minuses and
if they are in a streak we cut them into one or a  plus or none.
having a string representing the equation.
we try to convert that string into list so instead of chars we now will have
strings with meanings.
Example: 234+324
instead of 2 3 4 + 3 2 4 now we have 234 + 324
which is meaningful
instead of 7 chars now we have a list: [ number, operator , number ]

if we had brackets we would convert them into expressions
Example: (234+324)*4
after conversion will be: [expression, operator, number]
                          ['(234+324)', '*', '4']

after we convert everything no we search all the expressions
and solve them as they where equations themselves (they are)
we convert them into numbers.

now we have a list of numbers and operators.
-- operators
we have a module that saves the operators in three dictionaries
the operator is the key and the value is it's strength

-left_operators
-middle_operators
-right_operators
some operators come to the left of a number
some come to the right
and some come in between
(adding an operator will be explained soon)

back to the list. having a list of the equation we search the
strongest operator and operate according to what kind it is
minus is a special case because it is a middle operator
that can come not in between two numbers so the code handle it differently
let's go over it,

if it's a middle operator we check left and right to see if its between
two numbers, the argument that if it is between operators then they can
be operated into numbers is not valid because we checked that it is in
fact the first strongest operator

if it's a minus and it's not in between two numbers we operate 0-number
, we delete the node of the number and replace the minus with the result
else it's a regular middle operator

if it's a middle we check that it's good and we operate number op number
then delete the two numbers nodes and replace the operator with the result

if it's a left then there is a possibility that a left with the same strength
is to the right of it, so we run right while there is a same strength operator
and we operate it replacing similar to the middle but only one node
deleted of course.

right operator simply checks if there's a number to the left and replace and
deletes what needs to be.

we do all this a few times until we have one node in the list which is
the result if we have more then one then an operator is missing

------- adding an operator -------

two lines needed barely to do so.

-first decide what kind of operator it is.
Examples: + is a middle operator, ! is a right operator.

-go to the operators.py module
-add to the dictionary of your choice the operator and it's strength
(you are not allowed to add an already existing operator!!!)

- now go to the solver_helper.py, find the function called "get_result"
and add one more elif of your choice and the operation
(frankly, it should be pretty oblivious once you found the function)

that's it.

--- tests ----
Demands: pytest-6.2.1 and an editor software that can run 
the tests
with that editor, run tests.py with pytest.


