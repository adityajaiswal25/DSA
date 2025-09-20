def pall(s):
    
    def check(s, start, end):
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return check(s, start + 1, end - 1)
    return check(s,0,len(s)-1)
print(pall("abbab"))