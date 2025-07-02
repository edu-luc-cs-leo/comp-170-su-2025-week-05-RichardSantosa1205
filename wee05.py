def intersection(foo: str, bar: str) -> str:
    # This will hold all the letters that appear in both strings 
    common_letters = "" 
    results = ""

    # Check if either foo or bar is None
    if foo == None or bar == None:
        results = None
    else:
        # Go through each letter in the first string 
        for letter in foo:
            # Check if the letter is also in the second string
            if letter in bar:
                # Check if the letter is not already in the result
                if letter not in common_letters:
                        # Add the letter to the result 
                        common_letters += letter

        # if no common letters were found, set results to None
        results = common_letters
        if results == "":
            results = None

    # Only one return statement at the end 
    return results

print( intersection("longhorn", "badminton") )
print( intersection("longhorn", "apple") )
print( intersection("apple", "nothing") )
print( intersection("none", None) )


def is_alphabetical(string: str) -> bool:
     # Start by assuming the string is alphabetical
    result = True

    if  string == None:
          # Check to make sure that it is not null
          result = False 
    else:
        # Check each character in the string 
        for ch in string:
             # Get the ASCII value of the character 
             ascii_value = ord(ch)

             # Check if it's NOT an uppercase (65-90) or lowercase (97-122) letter
             if not (65 <= ascii_value <= 90 or 97 <= ascii_value <= 122):
                  result = False
    return result 
print(is_alphabetical('abcdeFQ') )
print( is_alphabetical('Bde1') )
print( is_alphabetical('1adbcs') )
print( is_alphabetical(None) )


def letters_only(string: str) -> str:
    # This will hold only the letters
    result_string = ""
    result = ""

    if string == None:
        result = None
    else:
        # Go through each character in the input
        for ch in string:
            ascii_value = ord(ch)

            # Check if the character is a letter (A–Z or a–z)
            if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
                result_string += ch

        # If no letters were found, return None
        if result_string == "":
            result = None
        else:
            result = result_string

    return result

print( letters_only("A man, a plan, a canal: Panama") )
print( letters_only("12345!@#") )
print( letters_only("hello world") )
print( letters_only(None) )


def generate_palindrome(string: str) -> str:
    # If the string is empty or None, return None
    if string == "" or string == None:
        result = None
    else:
        # This creates the reverse of the string without the last character
        reversed_part = ""
        index = len(string) - 1  # Start from second to last character

        while index >= 0:
            reversed_part += string[index]
            index -= 1

        # Combine the original and the reversed part to make a palindrome
        palindrome = string + reversed_part
        result = palindrome

    # Return the result
    return result

print( generate_palindrome("sturgeon") )
print( generate_palindrome("canoe") )
print( generate_palindrome("") ) 
print( generate_palindrome(None) )


def is_palindrome(string: str) -> bool:
    # Build a clean version of the string: only letters and digits, all lowercase
    cleaned = ""
    result = ""

    if string == None:
        result = False
    else:
        for ch in string:
            ascii_value = ord(ch)

            # Check if the character is a letter (A–Z or a–z)
            if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
                # Convert uppercase to lowercase
                if 65 <= ascii_value <= 90:
                    cleaned += ch.lower()
                else:
                    cleaned += ch

            # Check if the character is a digit (0–9)
            elif 48 <= ascii_value <= 57:
                cleaned += ch

        # Now check if the cleaned string is the same as its reverse
        reversed_string = ""
        index = len(cleaned) - 1
        while index >= 0:
            reversed_string += cleaned[index]
            index -= 1

        # One return statement at the end
        if cleaned == reversed_string:
            result = True
        else:
            result = False

    return result

print( is_palindrome("raCecar") )
print( is_palindrome("A man, a plan, a canal: Panama") )
print( is_palindrome("n00n") )
print( is_palindrome("port") ) 
print( is_palindrome(None) )

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
