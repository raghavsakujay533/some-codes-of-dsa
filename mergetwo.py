arr1=[2,3,4,5,7]
arr2=[1,6,8,9,10]
result=[]
i=0
j=0
while i <len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        result.append(arr1[i])
        
        i+=1
        j+=1
        
    else:
        result.append(arr2[j])
        j+=1
        
while i<len(arr1):
    result.append(arr1[i])
    i+=1
while j <len(arr2):
    result.append(arr2[j])
    j+=1
print(result)