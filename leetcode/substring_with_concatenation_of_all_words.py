class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        def are_all_words_accounted_for(hash_table):
            for word, val in hash_table.items():
                if val != 1:
                    return False

            return True

        # Now iterate through the string to find out if any of the words are in
        # the hash table
        results = []
        start_pos = 0
        curr_pos = 0
        while curr_pos < len(s):
            # Initialize all the word counts encountered so far to 0
            hash_table = {}
            word_len = 0
            for word in words:
                word_len = len(word)
                hash_table[word] = 0
            word_accounted_for = 0

            curr_word = ""
            no_intervening_word = True
            while no_intervening_word and curr_pos < len(s):
                curr_word += s[curr_pos]
                if len(curr_word) == word_len:
                    if curr_word in hash_table and hash_table[curr_word] < 1:
                        hash_table[curr_word] = 1
                        word_accounted_for += 1
                    else:
                        start_pos = curr_pos + 1

                    # Check if we have encountered all the words
                    if word_accounted_for == len(words):
                        results.append(start_pos)
                        no_intervening_word = False

                    curr_word = ""

                curr_pos += 1

        return results
    
soln = Solution()
# s = "barfoothefoobarman"
# words = ["foo", "bar"]
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
# answer = [6, 9, 12]
results = soln.findSubstring(s, words)
print(results)