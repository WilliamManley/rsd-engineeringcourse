def is_palindrome(string):
    chars = list(string)
    chars.reverse()
    flipped = ''.join(chars)
    return string == flipped
