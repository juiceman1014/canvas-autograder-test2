def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

if __name__ == "__main__":
    import sys
    input_str = sys.stdin.read().strip()
    print(is_palindrome(input_str))