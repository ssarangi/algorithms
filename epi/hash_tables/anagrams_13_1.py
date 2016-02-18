def is_anagram(w1, w2):
    chash = {}

    # Now find all the characters in w1 and create a hash table
    for c in w1:
        if c in chash:
            chash[c] += 1
        else:
            chash[c] = 1

    for c in w2:
        if c not in chash:
            return (w1, w2, False)

        if chash[c] == 0:
            return (w1, w2, False)

        chash[c] -= 1

    return (w1, w2, True)

def anagrams(*words):
    for i, word in enumerate(words):
        for j in range(i+1, len(words)):
            print(is_anagram(word, words[j]))

if __name__ == "__main__":
    anagrams("heir",
             "hewn",
             "hoes",
             "host",
             "hubs",
             "icon",
             "idea",
             "idle",
             "inch",
             "inks",
             "item",
             "jest",
             "juts",
             "kale",
             "keen",
             "kiln",
             "kiss",
             "knee",
             "lags",
             "lake",
             "lamb",
             "lamp",
             "laps",
             "last",
             "lays",
             "lead",
             "leak",
             "leek",
             "left",
             "legs",
             "liar",
             "lied",
             "lime",
             "link",
             "lips",
             "list",
             "loco",
             "loin",
             "loot",
             "lots",
             "hire",
             "when",
             "hose",
             "shoe",
             "shot",
             "bush"
             )