# 1. Why should we use functions at all?
We use functions so that we could reuse them at several times without having to rewrite the whole blocks

# 2. How to define/declare a function?
Use the following: 
def <function name>([parameters]):
    ...
    [return]

# 3. How to call/use a function?
Write the function name. EG: print(say_hi())

# 4. What is return? Why and How do we use it?
return allows you to retain the result of an equation or of the function for later use.
We use return when we want to reuse the result of the function for another use.
Place return at the end of the defining function with the result you want to maintain. EG: return a+bi

# 5. Do we have to use return for every function?
No. As mentioned above, we only use it whenever we want to retain the result.

# 6. What are the function arguments/parameters? Why and How do we use it?
Function arguments/parameters are what represent our later variables when we call the function for use.
There are some functions that require variables to work; therefore, if we want to produce one that can be reused, we need something - parameters - to represent our variables.
We place function arguments in the () of the function. EG: evaluate(a,b,c) - a,b, and c are parameters

# 7. How to use a function from a different file other than our currently working file?
We can use a function from another file by importing it (with the condition that both files are .py):
EG: We have two files class.py and test.py:
In lalala.py file: def evaluate(a,b) return a + b
In test.py file: 
import lalala 
lalala.evaluate(1,1)