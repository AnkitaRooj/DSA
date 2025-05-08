class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap1,hashMap2={},{}
        for e in s:
            if e in hashMap1:
                hashMap1[e] += 1
            else:
                hashMap1[e] = 1
        for e in t:
            if e in hashMap2:
                hashMap2[e] += 1
            else:
                hashMap2[e] = 1
        print(hashMap1)
        print(hashMap2)
        for e in hashMap1:
            if e not in hashMap2:
                return False
            if e in hashMap2:
                if hashMap1[e] != hashMap2[e]:
                    return False
        return True