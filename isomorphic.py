# Learn Python together
"""Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
"""
# Solution
def isIsomorphic(s: str, t: str) -> bool:
    # return False if the length of the strings isn't equal
    if len(s) != len(t):
            return False
    # create empty dicts for mapping
    s_dict, t_dict = {}, {}
    # loop through the length of the first string
    for i in range(len(s)):
        # check if the current character in s has been mapped before
        if s[i] in s_dict:
            # if yes, check if the mapping is consistent
            if s_dict[s[i]] != t[i]:
                # if the mapping is not consistent, return False 
                return False
        # check if the current character in t has been mapped before
        elif t[i] in t_dict:
            # if yes and mapping isn't consistent
            if t_dict[t[i]] != s[i]:
                #return False because the strings are not isomorphic
                return False
        # otherwise create a new mapping
        else:
            s_dict[s[i]] = t[i]
            t_dict[t[i]] = s[i]    
    return True  

# check                
print(isIsomorphic("badc", "baba")) # Output -> False
print(isIsomorphic("egg", "add"))   # Output -> True
print(isIsomorphic("paper", "title")) # Output -> True
print(isIsomorphic("foo", "bar"))   # Output -> False
print(isIsomorphic("abacba", "xpxcpx" )) # Output -> True
                   