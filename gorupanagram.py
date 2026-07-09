arr=["eat,tea,ate,eta,tae,aet"]
word={
    
}
for i in arr:
    keys="".join(sorted(i))
    if keys in word:
        word[keys].append(i)
    else:
        word[keys]=[i]
print(word.values())