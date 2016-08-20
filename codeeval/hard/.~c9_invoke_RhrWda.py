import sys

class Char:
    def __init__(self, c):
        self.c = c
        self.repeat = False
    
    def set_repeat(self):
        self.repeat = True
        
    def match(self, char):
        if self.c == char:
            return True
        elif self.repeat is True:
            return True
        
        return False

def create_characters(substr):
    char_list = []
    for idx, c in enumerate(substr):
        if c == '\\':
            continue
        if c == '*' and substr[idx-1] == '\\':
            char_cls = Char('*')
        elif c == '*':
            curr_char = char_list[-1]
            curr_char.set_repeat()
    
    return char_list

def string_searching_helper(orig, orig_idx, char_list, char_list_idx):
    curr_match = char_list[char_list_idx].match(orig[orig_idx])
    
    if char_list[char_list_idx].repeat is True:
        if curr_match is not False:
            curr_match, new_idx = string_searching_helper(orig, orig_idx + 1, char_list, char_list_idx)
            
        if char_list_idx < len(char_list):
            curr_match, new_idx |= string_searching_helper(orig, orig_idx, char_list, char_list_idx + 1)
            
    return curr_match, new_idx

def string_searching(orig, char_list):
    start_idx = 0
    found_match = False
    
    while start_idx < len(orig) and found_match is False:
        curr_match = True # Start with temp match = true for substring from current location
        substr_idx = 0
        while curr_match is True:
            

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        orig, substr = test.split(",")
        char_list = create_characters(substr)
        string_searching(orig, char_list)