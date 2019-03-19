def sum_array(array):

    '''Return sum of all items in array'''

    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])


def fibonacci(n):

    '''Return nth term in fibonacci sequence

       The Rule is x(n) = x(n-1) + x(n-2)

    '''

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)



def factorial(n):

    '''Return n!

    n! = n x (n−1)!

    the factorial of any number is that number
    times the factorial of (that number minus 1)

    '''

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



def reverse(word):

    '''Return any string/word in reverse'''

    if word == "":
        return word
    else:
        return reverse(word[1:]) + word[0]
