def find_max_palindrome(minimum=100, maximum=999):
    max_palindrome = 0
    for i in range(maximum, minimum, -1):
        for r in range(maximum, minimum, -1):
            x = str(i * r)
            if x == x[::-1]:
                if int(x) > max_palindrome:
                    max_palindrome = int(x)

    return max_palindrome

print(find_max_palindrome())

