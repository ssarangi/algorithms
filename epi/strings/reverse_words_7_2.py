# Use O(1) space
def reverse_words(sentence):
    sentence = [c for c in sentence]
    sent_len = len(sentence) - 1
    # 2 pass approach
    for i in range(0, len(sentence) // 2):
        c1 = sentence[i]
        c2 = sentence[sent_len - i]
        sentence[sent_len - i] = c1
        sentence[i] = c2

    # 2nd Pass: Reverse the individual words
    start = 0
    for i, c in enumerate(sentence):
        if c == " " or i == len(sentence) - 1:
            if i == len(sentence) - 1:
                i += 1

            end = i - 1
            length = end - start
            for j in range(0, (length // 2) + 1):
                sentence[end - j], sentence[start + j] = sentence[start + j], sentence[end - j]

            start = end + 2
    sentence = "".join(sentence)
    return sentence

def main():
    print(reverse_words("Alice likes Bob"))
    print(reverse_words("Where am I going"))

if __name__ == "__main__":
    main()
