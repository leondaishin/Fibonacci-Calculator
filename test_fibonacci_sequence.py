### test fibonacci sequence code 

import pytest
from fibonacci_sequence import (
    fibonacci, 
    fibonacci_sequence, 
    is_fibonacci, 
    fibonacci_index, 
    fibonacci_sum, 
    fibonacci_square_sum, 
    fibonacci_divisible, 
    fibonacci_mod, 
    fibonacci_cassini, 
    fibonacci_doubling, 
    fibonacci_doubling_pair, 
)

def test_fibonacci(): 
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55

def test_fibonacci_sequence(): 
    assert fibonacci_sequence(0) == []
    assert fibonacci_sequence(1) == [0]
    assert fibonacci_sequence(2) == [0, 1]
    assert fibonacci_sequence(3) == [0, 1, 1]
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_is_fibonacci(): 
    assert is_fibonacci(1) == True 
    assert is_fibonacci(3) == True 
    assert is_fibonacci(7) == False 
    assert is_fibonacci(9) == False 
    assert is_fibonacci(5) == True 
    assert is_fibonacci(0) == True 
    assert is_fibonacci(54) == False 
    assert is_fibonacci(55) == True

def test_fibonacci_index(): 
    assert fibonacci_index(0) == 0
    assert fibonacci_index(1) == 1 and 2
    assert fibonacci_index(2) == 3
    assert fibonacci_index(3) == 4
    assert fibonacci_index(5) == 5
    assert fibonacci_index(8) == 6

def test_fibonacci_sum(): 
    assert fibonacci_sum(0) == 0
    assert fibonacci_sum(1) == 1
    assert fibonacci_sum(5) == 12
    assert fibonacci_sum(10) == 143

def test_square_sum():
    assert fibonacci_square_sum(0) == 0
    assert fibonacci_square_sum(1) == 1
    assert fibonacci_square_sum(5) == 40
    assert fibonacci_square_sum(10) == 4895

def test_fibonacci_divisible(): 
    assert fibonacci_divisible(6, 3) == True 
    assert fibonacci_divisible(10, 5) == True 
    assert fibonacci_divisible(5, 4) == False

def test_fibonacci_mod(): 
    assert fibonacci_mod(10, 7) == 6
    assert fibonacci_mod(20, 10) == 5
    assert fibonacci_mod(15, 5) == 0

def test_cassini(): 
    assert fibonacci_cassini(1) == True 
    assert fibonacci_cassini(2) == True 
    assert fibonacci_cassini(5) == True 
    assert fibonacci_cassini(10) == True
    assert fibonacci_cassini(12) == True 
    assert fibonacci_cassini(100) == False

def test_fibonacci_doubling():
    assert fibonacci_doubling(0) == 0
    assert fibonacci_doubling(1) == 1
    assert fibonacci_doubling(5) == 5
    assert fibonacci_doubling(10) == 55
    assert fibonacci_doubling(20) == 6765

def test_fibonacci_doubling_pair(): 
    assert fibonacci_doubling_pair(0) == (0, 1)
    assert fibonacci_doubling_pair(1) == (1, 1)
    assert fibonacci_doubling_pair(5) == (5, 8)
    assert fibonacci_doubling_pair(10) == (55, 89)
