class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in range(len(s)): 
            if s[i] not in hashmap:
                for val in hashmap.values(): 
                    if t[i] == val: 
                        return False
                hashmap[s[i]] = t[i]
            else: 
                if hashmap[s[i]] != t[i]: 
                    return False
        return True
