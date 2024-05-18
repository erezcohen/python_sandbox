# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function (default args )
def sayHello(name="Sam"):
    print(f"Hello {name}")


# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total


# Docstrings  // help(getSum1)  # will print the docstring
def getSum1(num1, num2):
    """
    Return the sum of num1 and num2
    >>> getSum(1,2)
    3
    """
    total = num1 + num2
    return total


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Very similar to JS arrow functions

getSum2 = lambda num1, num2: num1 + num2

print(getSum2(1, 2))


# None // Null (there is no undefied)
def noRet(a, b):
    c = a + b


print(noRet(10, 20))


#################################################################

# print stuff

print("bla " * 5)

print(14, 15, sep="\n")
