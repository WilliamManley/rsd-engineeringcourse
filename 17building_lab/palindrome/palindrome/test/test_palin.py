from palin import is_palindrome

def test_empty_string_is_palindrome():
    assert(is_palindrome("") == True)

def test_single_character_is_palindrome():
    assert(is_palindrome("a") == True)

def test_non_palindromic_string_returns_false():
    assert(is_palindrome("Michael Palin") == False)

def test_palindromic_string_returns_true():
    assert(is_palindrome("detartrated") == True)
