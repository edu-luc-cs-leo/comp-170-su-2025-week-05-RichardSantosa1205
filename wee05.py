def intersection(foo: str, bar: str) -> str:
    # Return the letters that appear in both strings, in order of `foo`, consuming letters in `bar` as used.
    if not foo or not bar:
        return ""
    common_letters = ""
    bar_list = list(bar)  # So we can remove used letters
    for letter in foo:
        if letter in bar_list:
            common_letters += letter
            bar_list.remove(letter)
    return common_letters


def is_alphabetical(string: str) -> bool:
    # Return True if the string only contains A-Z or a-z letters.
    if not string:
        return False
    for ch in string:
        ascii_value = ord(ch)
        if not (65 <= ascii_value <= 90 or 97 <= ascii_value <= 122):
            return False
    return True


def letters_only(string: str) -> str:
    # Return only the letters A-Z or a-z from the string.
    if not string:
        return ""
    result_string = ""
    for ch in string:
        ascii_value = ord(ch)
        if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
            result_string += ch
    return result_string

def generate_palindrome(string: str) -> str:
    # Generate a palindrome: mirror entire string if even-length, drop last char if odd-length.
    if not string:
        return None
    if len(string) == 1:
        return string
    if len(string) % 2 == 0:
        reversed_part = string[::-1]
    else:
        reversed_part = string[:-1][::-1]
    return string + reversed_part


def is_palindrome(string: str) -> bool:
    # Return True if the string is a palindrome (letters/digits only, ignore case).
    if not string:
        return False
    cleaned = ""
    for ch in string:
        ascii_value = ord(ch)
        if 65 <= ascii_value <= 90:
            cleaned += ch.lower()
        elif 97 <= ascii_value <= 122:
            cleaned += ch
        elif 48 <= ascii_value <= 57:
            cleaned += ch
    return cleaned == cleaned[::-1]

print(intersection("longhorn", "badminton"))
print(intersection("longhorn", "apple"))
print(intersection("apple", "nothing"))
print(intersection("none", None)

print(is_alphabetical('abcdeFQ'))
print(is_alphabetical('Bde1'))
print(is_alphabetical('1adbcs'))
print(is_alphabetical(None))

print(letters_only("A man, a plan, a canal: Panama"))
print(letters_only("12345!@#"))
print(letters_only("hello world"))
print(letters_only(None))

print(generate_palindrome("sturgeon"))
print(generate_palindrome("canoe"))
print(generate_palindrome(""))
print(generate_palindrome(None))

print(is_palindrome("raCecar"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("n00n"))
print(is_palindrome("port"))
print(is_palindrome(None))


# ✅ Unit tests — properly indented and aligned

import unittest

class TestStringMethods(unittest.TestCase):

    def test_intersection(self):
        self.assertEqual(intersection("airplanes", "repairman"), "airpne")
        self.assertEqual(intersection("abc", "def"), "")
        self.assertEqual(intersection("hello", "hello"), "hello")
        self.assertEqual(intersection("aaaa", "aaa"), "aaa")  # Consumes only 3 'a's
        self.assertEqual(intersection("", "abc"), "")
        self.assertEqual(intersection("abc", ""), "")
        self.assertEqual(intersection("", ""), "")
        self.assertEqual(intersection("abc", "cab"), "abc")

    def test_is_alphabetical(self):
        self.assertTrue(is_alphabetical("abcXYZ"))
        self.assertFalse(is_alphabetical("abc1"))
        self.assertFalse(is_alphabetical("hello!"))
        self.assertFalse(is_alphabetical(" "))
        self.assertFalse(is_alphabetical(""))
        self.assertFalse(is_alphabetical(None))
        self.assertTrue(is_alphabetical("ZzAaBb"))

    def test_letters_only(self):
        self.assertEqual(letters_only("abc123XYZ!@#"), "abcXYZ")
        self.assertEqual(letters_only("!@#$%^&*()"), "")
        self.assertEqual(letters_only(""), "")
        self.assertEqual(letters_only(None), "")
        self.assertEqual(letters_only("LettersONLY"), "LettersONLY")

    def test_generate_palindrome(self):
        self.assertEqual(generate_palindrome("mice"), "miceecim")
        self.assertEqual(generate_palindrome("mad"), "madam")
        self.assertEqual(generate_palindrome("a"), "a")
        self.assertEqual(generate_palindrome(""), None)
        self.assertEqual(generate_palindrome(None), None)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("Palindrome"))
        self.assertFalse(is_palindrome(""))
        self.assertFalse(is_palindrome(None))


if __name__ == '__main__':
    unittest.main()
#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
