from testpackage import sum_array
from testpackage import fibonacci
from testpackage import factorial
from testpackage import reverse
from testpackage import bubble_sort
from testpackage import merge_sort
from testpackage import quick_sort

def sum_array(array):
    assert sum_array.sum_array([1,2,3,4,5]) == 15

def fibonacci(n):
    assert fibonacci.fibonacci(15) == 610

def factorial(n):
    assert sum_array.factorial(9) == 362880

def reverse(word):
    assert reverse.reverse(["Jason Kannemeyer"]) == "reyemennaK nosaJ"

def bubble_sort(items):
    assert bubble_sort.bubble_sort([1,5,2,7,3]) == [1, 2, 3, 5, 7]

def quick_sort(items):
    assert quick_sort.quick_sort([1,6,5,9,8,7]) == [1, 5, 6, 7, 8, 9]

def merge_sort(item):
    assert merge_sort.merge_sort(([1,6,5,9,8,7]) == [1, 5, 6, 7, 8, 9])
