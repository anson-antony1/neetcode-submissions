class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        if len(s) == len(t):
            for i in range (len(s)):
                if s[i] in dictS:
                    if dictS[s[i]] != t[i]:
                        return False
                else:
                    dictS[s[i]] = t[i]
                if t[i] in dictT:
                    if dictT[t[i]] != s[i]:
                        return False
                else:
                    dictT[t[i]] = s[i]
            return True
        else:
            return False