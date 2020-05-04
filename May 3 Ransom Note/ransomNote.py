class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_magazine = {}
        
        for letter in magazine:
            if letter in hash_magazine:
                hash_magazine[letter] += 1
            else:
                hash_magazine[letter] = 1
        
        for letter in ransomNote:
            if letter in hash_magazine and hash_magazine[letter]>0:
                hash_magazine[letter] -= 1
            else:
                return False
        return True
