"""Python implementation of recursion algorithm and call stack"""


def countdown(i: int):
    """Recursion is used to make the solution clearer; there's no performance benefit
    Countdown function prints all counts down all numbers, beginning with "i".
    """
    print(i)
    # base case - the function doesn't call itself again to avoid infinite loop
    if i <= 1:
        return
    # recursive case - the function calls itself
    else:
        countdown(i - 1)


countdown(4)


def greet(name):
    """Illustration of the call stack"""
    print("Hello, " + name)
    greet2(name)


def greet2(name):
    # the calling function greet() is now paused in a partially completed state
    # all the values of its variables are still stored on the call stack (i.e., in memory)
    print("How are you, " + name + "?")


def factorial(x):
    """ Each call to factorial() has its own copy of x; you can't access a different function's copy of x"""
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print("Factorial of 6 is: ", factorial(6))
