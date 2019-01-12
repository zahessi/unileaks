# https://www.codewars.com/kata/playing-with-passphrases

def play_pass(s, n):
    result = ''
    for i, c in enumerate(s.upper()):
        if c.isalpha():
            c = ord(c) + n % 26 
            shift = chr(c if 65 <= c <= 90 else c - 26)
            result += shift if not i % 2 else shift.lower()
        elif c.isdigit():
            result += str(9 - int(c))
        else:
            result += c
    return result[::-1]

assert play_pass("I LOVE YOU!!!", 1) == "!!!vPz fWpM J"