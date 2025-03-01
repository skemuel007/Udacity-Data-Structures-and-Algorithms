"""
Palindrome
A palindrome is a word that is the reverse of itself—that is, it is the same
word when read forwards and backwards.

For example:

"madam" is a palindrome
"abba" is a palindrome
"cat" is not
"a" is a trivial case of a palindrome
The goal of this exercise is to use recursion to write a function
is_palindrome that takes a string as input and checks whether that string is
a palindrome. (Note that this problem can also be solved with a non-recursive
solution, but that's not the point of this exercise.)
"""


def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """

    if len(input) == 0:
        return True

    else:
        return input == reverse_string(input)

def reverse_string(input):
    if len(input) == 0:
        return ''
    else:
        input[-1] + reverse_string(input[1:-1])


# Test Cases
print("Pass" if (is_palindrome("")) else "Fail")
print("Pass" if (is_palindrome("a")) else "Fail")
print("Pass" if (is_palindrome("madam")) else "Fail")
print("Pass" if (is_palindrome("abba")) else "Fail")
print("Pass" if not (is_palindrome("Udacity")) else "Fail")
