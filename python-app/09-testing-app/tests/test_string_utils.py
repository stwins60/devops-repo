from string_utils import reverse_string, is_palindrome, count_words, capitalize_words

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True

def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("") == 1  # empty string splits to ['']
    assert count_words("one") == 1

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python") == "Python"
