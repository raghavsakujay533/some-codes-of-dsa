def permutation():
    
    s="raghav"

    a="ha"
    n=len(a)
    target=sorted(a)
    for i in range(len(s)-n+1):
    
        window=sorted(s[i:i+n])
        if window==target:
            return True     
        else:
            return False
print(permutation)