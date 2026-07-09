# arr=[10,20,30,60,70,80,40,50]
# n=len(arr)
# largest=0
# secondlarge=0
# thirdlargest=0
# for i in range(0,len(arr)):
#     if arr[i]>largest:
#         thirdlargest=secondlarge
#         secondlarge=largest
#         largest=arr[i]
#     elif arr[i]>secondlarge:
#         secondlarge=arr[i]
# print(thirdlargest)
# print(secondlarge)

arr=[80,40,50,20,10,30]
n=len(arr)
small=arr[0]
secondsmall=0
for i in range(1,len(arr)):
    if arr[i]<small:
        secondsmall=small
        small=arr[i]    
print(secondsmall)
print(small)