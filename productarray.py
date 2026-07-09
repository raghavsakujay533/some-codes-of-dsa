arr=[1,2,3,4,5,6]
n=len(arr)
prefix=1
ans=[1]*n
for i in range(0,n):
    ans[i]*=prefix
    prefix*=arr[i]
suffix=1
for i in range(n-1,-1,-1):
    ans[i]*=suffix
    suffix*=arr[i]
print(ans)