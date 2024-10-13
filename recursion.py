""" Python implementation of recursion algorithm and call stack """


def countdown(i: int):
    """
    Recursion is used to make the solution clearer; there's no performance benefit
    Countdown function prints all counts down all numbers, beginning with "i".

    @param i: the number from which the function should start the count down
    """
    print(i)
    # base case - the function doesn't call itself again to avoid infinite loop
    if i <= 1:
        return
    # recursive case - the function calls itself
    else:
        countdown(i - 1)


countdown(4)


def greet(name: str):
    """
    Illustration of the call stack (together with greet2()).
    This is NOT a recursive function. Stack is a LIFO data structure.
    LIFO - Last In, First Out
    
    @param name: name which the function should print
    """
    print("Hello, " + name)
    greet2(name)


def greet2(name):
    """
    The calling function greet() is now paused in a partially completed state.
    All the values of its variables are still stored on the call stack (i.e., in memory),
    and we have access to them in greet2().
    """
    print("How are you, " + name + "?")

greet("Zuzanna")


def factorial(x: int):
    """
    Each call to factorial() has its own copy of x. 
    You can't access a different function's copy of x.
    
    @param x: the number which factorial the function should calculate
    """
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print("Factorial of 6 is:", factorial(6))
