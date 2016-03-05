from itertools import permutations

# Palindromes have a property that all the charcters have 2 elements and only 1 or 0 character can
# have frequency 1 or 0
def is_palindrome(string):
    freq = [0] * 26
    l = len(string)

    for c in string:
        freq[ord(c) - ord('a')] += 1

    odd = 0

    for i in range(0, 26):
        if freq[i] % 2 == 1:
            odd += 1

    # Palindrome condition
    if (l % 2 == 1 and odd == 1) or (l % 2 == 0 and odd == 0):
        return True, freq
    else:
        return False, freq

def reverse(string):
    return string[::-1]

def palindrome(string):
    is_palin, freq = is_palindrome(string)
    if not is_palin:
        return

    l = len(string)
    half = ""
    oddC = ""

    for i in range(0, 26):
        if freq[i] % 2 == 1:
            oddC += chr(i + ord('a'))

        half += (freq[i] // 2) * chr(i + ord('a'))

    palin = ""
    pm = permutations(half)
    for el in pm:
        half = "".join(el)
        palin = half
        if l % 2 == 1:
            palin += oddC

        palin += reverse(half)
        print(palin)

def main():
    ss = "aabcdb"
    palindrome(ss)

if __name__ == "__main__":
    main()