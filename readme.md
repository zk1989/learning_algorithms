Initially this repo was meant to record my progress while going through the "Grokking Algorithms", but in the process it's expanded to include stuff beyond the book's content. All comments in the files are mine, I also renamed some variables and made sure the code is correct. Unless stated otherwise, core of the code snippets comes from the book.

# Grokking Algorithms (2nd edition, 2024)

> **NOTE:** I do NOT recommend this book. 
> It turned out to be full of mistakes, mostly regarding code.
> It includes multitude of repetitions and blank pages, just in order to make it look larger.
> I learned more by hunting those mistakes rather than reading the book.

These are the questions I asked myself while reading _Grokking Algorithms_. 
I have a Python background therefore most questions use Python for better understanding.

# Chapter 1

### What does it mean that something is "binary"?
- using a system of numbers that uses only 0 and 1
- relating to or consisting of two things, in which everything is either one thing or the other 
(Source: https://dictionary.cambridge.org/dictionary/english/binary)

### What is an algorithm?

### Introduction to logarithms
https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-intro/v/logarithms

## Chapter 2

### Do linked lists exist in Python?
Python doesn’t ship with a built-in linked list data type in the “classical” sense. (...)
Python does however include the collections.deque class which provides a double-ended queue and is implemented as a doubly-linked list internally. 
Under some specific circumstances you might be able to use it as a “makeshift” linked list. 
(Source: https://dbader.org/blog/python-linked-list)

### What kind of arrays are there in Python?
Lists and tuples both belong to a class of data structures called arrays.
(Source: https://www.oreilly.com/library/view/high-performance-python/9781449361747/ch03.html#:~:text=Lists%20and%20tuples%20are%20a,data%20with%20some%20intrinsic%20ordering)

### What does it mean that Python's list type is a dynamic array?
It means that it would typically over-allocate their backing store slightly to speed up element insertions in the average case, 
thus increasing the memory footprint. 
(Source: https://dbader.org/blog/python-linked-list)

### What does it mean that a Python's tuple type is a static array?
Tuples are preferable when data is static as tuples do not use any extra headroom. 
A list of size 100,000,000 created with append will actually use 112,500,007 size worth memory. 
On the other hand, a tuple of 100,000,000 size will only use 100,000,000 memory which makes tuples lightweight.
(Source: https://medium.com/@ninads79shukla/high-performance-python-part1-tuples-and-lists-85a203db34f8)

## Chapter 3

### What is a factorial?
5! = 5 x 4 x 3 x 2 x 1 = 120
https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/the-factorial-function

### So what does the famous stack-overflow mean? :)
A stack overflow occurs when a program exceeds the amount of memory that is allocated for its execution. 
This can occur in different scenarios especially when a function keeps calling itself.
(Source: https://martinxpn.medium.com/what-is-stack-overflow-really-40-100-days-of-python-e5e129416d33#:~:text=A%20stack%20overflow%20occurs%20when,a%20function%20keeps%20calling%20itself)

## Chapter 4

### Why is there no IndexError for x[1:] when x=[]?
https://stackoverflow.com/questions/70456783/why-is-there-no-indexerror-thrown-and-why-the-output-is-an-empty-list-when-the-i

## Chapter 6

### What is a double-ended queue?
It means that an element can be inserted or removed from both ends of the queue, unlike the other queues in which it can be done only from one end. Because of this property, it may not obey the First In First Out property. Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over a list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to a list that provides O(n) time complexity
(Source: https://www.geeksforgeeks.org/deque-in-python/)

### It appears that algorithms can be divided. How?
by their purpose: there are search algorithms, sorting algorithms,
on what sort of data structure they can be run on: graph algorithms.

### What is a topological sorting?
It's a way to make an ordered list out of a graph.

## Chapter 8

### What does AVL in AVL trees stand for?
The AVL tree is named after its inventors: Adelson-Velsky and Landis.
(Source: https://en.wikipedia.org/wiki/AVL_tree)