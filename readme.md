These are the questions I asked myself while reading "Grokking Algorithms (2nd Edition)". I have a Python background therefore most questions use Python for better understanding.

# Chapter 1

## What does it mean that something is "binary"?
- using a system of numbers that uses only 0 and 1
- relating to or consisting of two things, in which everything is either one thing or the other (Source: https://dictionary.cambridge.org/dictionary/english/binary)

## Introduction to logarithms
https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-intro/v/logarithms

# Chapter 2

## Do linked lists exist in Python?
Python doesn’t ship with a built-in linked list data type in the “classical” sense. (Source: https://dbader.org/blog/python-linked-list)

## What kind of arrays are there in Python?
Lists and tuples both belong to a class of data structures called arrays. Tuples are immutable so they cannot be modified or resized.

## What does it mean that Python's list type is a dynamic array?
It means that it would typically over-allocate their backing store slightly to speed up element insertions in the average case, thus increasing the memory footprint. (Source: https://dbader.org/blog/python-linked-list)

## What does it mean that a Python's tuple type is a static array?
Tuples are preferable when data is static as tuples do not use any extra headroom. A list of size 100,000,000 created with append will actually use 112,500,007 size worth memory, on the other hand, a tuple of 100,000,000 size will only use 100,000,000 memory which makes tuples lightweight.
(Source: https://medium.com/@ninads79shukla/high-performance-python-part1-tuples-and-lists-85a203db34f8)

# calculating factorials 