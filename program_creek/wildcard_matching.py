"""
The MIT License (MIT)

Copyright (c) 2015 <Satyajit Sarangi>

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

"""
Implement wildcard pattern matching with support for '?' and '*'.
To understand this solution, you can use s="aab" and p="*ab".
"""

def wildcard_match(pattern, string):
    string_idx = 0
    pattern_idx = 0
    while pattern_idx < len(pattern):
        p = pattern[pattern_idx]
        if p == '*':
            string_idx = pattern_idx
            original_idx = pattern_idx
            pattern_idx += 1
            p = pattern[pattern_idx]
            s = string[string_idx]
            while s == p:
                string_idx += 1
                s = string[string_idx]

            if string_idx - original_idx == 0:
                return False
            pattern_idx += 1
        elif p == '?':
            string_idx = pattern_idx
            pattern_idx += 1
            s = string[string_idx]
            p = pattern[pattern_idx]
            if s == p:
                string_idx += 1
            pattern_idx += 1
        else:
            if p != string[string_idx]:
                return False
            string_idx += 1
            pattern_idx += 1

    if pattern_idx == string_idx:
        return True

    return False

def main():
    pattern = "*ab"
    string = "aaaab"
    print(wildcard_match(pattern, string))

    pattern = "?ab"
    string = "bb"
    print(wildcard_match(pattern, string))

if __name__ == "__main__":
    main()