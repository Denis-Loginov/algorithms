def is_palindrome(line: str) -> bool:
    clear_line = "".join(c for c in line if c.isalnum()).lower()
    reversed_string = clear_line[::-1]
    return clear_line == reversed_string


print(is_palindrome(input().strip()))