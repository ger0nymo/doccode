def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_palindromes(start, end):
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome(num):
            palindromes.append(num)
    return palindromes

def main():
    start = 100
    end = 999
    palindromes = find_palindromes(start, end)
    print(f"Palindromic numbers between {start} and {end}:")
    for num in palindromes:
        print(num)

if __name__ == "__main__":
    main()