class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Here we must use a variable sized sliding window since
        we want to extend it as most as possible.
        "[AAAB]BBB" k = 1

        We also must use a fixed vector of 26 characters to count frequencies inside the sliding window
        we then check: window_length - most_frequent_character_count <= k ?
        to see if we can apply replacements.
        ex. "AAAB" 4 - 3 <= 1? were good.

        Window length = (right - left) + 1
        """

        freq_letters = [0] * 26 # each index tracks a letter. max(freq_letters) is O(26).
        left, right = 0, 0 # starting with a window of size 1
        max_length = 0

        # we travel until our exterior border hits the end.
        while right < len(s):
            # increase the encoutered letter frequency.
            freq_letters[ord(s[right]) - ord('A')] += 1
            window_length = (right - left) + 1

            if window_length - max(freq_letters) > k:
                # shrinking the window
                freq_letters[ord(s[left]) - ord('A')] -= 1
                left += 1
                window_length = (right - left) + 1

            right += 1
            max_length = max(max_length, window_length)

        return max_length


            





        
