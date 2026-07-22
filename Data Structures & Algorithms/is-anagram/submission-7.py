class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myDict1 = {}
        myDict2 = {}
        for char in s:
            if char in myDict1:
                myDict1[char] += 1
            else:
                myDict1[char] = 1
        for char in t:
            if char in myDict2:
                myDict2[char] += 1
            else:
                myDict2[char] = 1
        for key in myDict1.keys():
            if key in myDict2 and myDict1[key] == myDict2[key]:
                continue
            else:
                return False
        return True
        