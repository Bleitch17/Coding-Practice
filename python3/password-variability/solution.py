class Solution:
    def password_variability(self, pwd: str) -> int:
        n: int = len(pwd)
        num_substrings: int = (n * (n + 1)) // 2
        num_pairs: int = 0

        letter_frequencies: dict[str, int] = {}

        for i in range(len(pwd)):
            if pwd[i] in letter_frequencies:
                num_pairs += letter_frequencies[pwd[i]]
                letter_frequencies[pwd[i]] += 1
            
            else:
                letter_frequencies[pwd[i]] = 1
        
        return num_substrings - n + 1 - num_pairs
