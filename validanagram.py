s="raghav"
j="vahgar"
hsh={
    
}
hosh={
    
}
for i in s:
    if i in hsh:
        hsh[i]+=1
        
    else:
        hsh[i]=1
for l in j:
    if l in hosh:
        hosh[l]+=1
    else:
        hosh[l]=1

if hsh==hosh:
    print("valid")
else :
    print("invalid")