# Given a random string S = "adobecodebanc" and another string T with unique elements. Find the minimun consecutive
# substring if it exists

def min_cons_substr(S, T):
    start = 0

    while start < len(S):
        current_str = ""
        dict = {}
        for e in dict:
            dict[e] = True

        end_pos = start
        while len(dict.keys()) > 0 or end_pos < len(S):
            if S[end_pos] in dict:
                del dict[S[end_pos]]

def main():
    S = "adobecodebanc"
    T = "abc"
    print(min_cons_substr(S, T))
    
if __name__ == "__main__":
    main()