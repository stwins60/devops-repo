def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

def is_palindrome(s):
    """Check if string is palindrome"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_words(s):
    """Count words in string"""
    return len(s.split())

def capitalize_words(s):
    """Capitalize all words"""
    return s.title()
