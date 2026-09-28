class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #if they don't have the same amount of letters
        if len(s) != len(t):
            return False

        #one slot for each letter of alphabet
        counts = [0] * 26

   
        for i in range (len(s)):
            # count each s letter
            counts[ord(s[i]) - ord('a')] += 1
            # Remove s letter from t
            counts[ord(t[i]) - ord('a')] -= 1

        # if at 0 is anagram
        return all(count == 0 for count in counts)

        