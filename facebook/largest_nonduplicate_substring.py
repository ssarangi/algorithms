"""
The MIT License (MIT)

Copyright (c) <2015> <sarangis>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

def largest_nonduplicate_substr_simple(str):
    """
    Complexity of this algorithm is O(n^3)
    :param str:
    :return:
    """
    start_char = 0
    max_nonrepeated = 0
    nonrepeated_substr = ""

    while start_char < len(str):
        substr = str[start_char]
        for end in range(start_char + 1, len(str)):
            new_char = str[end]
            if new_char not in substr:
                substr += new_char
                if max_nonrepeated < len(substr):
                    nonrepeated_substr = substr
                max_nonrepeated = max(max_nonrepeated, len(substr))
            else:
                break

        start_char += 1

    return nonrepeated_substr

def largest_nonduplicate_substr_linear(str):
    str.upper()
    start_char = 0
    max_nonrepeated = 0
    nonrepeated_substr = ""
    chars_seen = 0

    while start_char < len(str):
        substr = str[start_char]
        for end in range(start_char + 1, len(str)):
            new_char = str[end]
            if chars_seen & (1 << (ord(new_char) - ord('A'))) == 0:
                substr += new_char
                chars_seen |= (1 << (ord(new_char) - ord('A')))
                if max_nonrepeated < len(substr):
                    nonrepeated_substr = substr
                max_nonrepeated = max(max_nonrepeated, len(substr))
            else:
                break

        start_char += end

    return nonrepeated_substr



def main():
    input_str = "GEEKSFORGEEKS"
    substr = largest_nonduplicate_substr_simple(input_str)
    print(substr, len(substr))

    substr = largest_nonduplicate_substr_linear(input_str)
    print(substr, len(substr))

if __name__ == "__main__":
    main()