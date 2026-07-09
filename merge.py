# def mergesort(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left=mergesort(arr[:mid])
#     right=mergesort(arr[mid:])
#     result=[]
#     i=j=0
#     while i<len(left)and j<len(right):
#         if left[i]<right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#         result.extend(left[i:])
#         result.extend(right[j:])
#         return result
# arr=[60,30,20,50,50]
# print(mergesort(arr))


arr=[40,50,20,10,30]
left=0
right=0
n=len(arr)
mid=len(arr)//2
left=arr[:mid]
right=arr[mid:]
result=[]
i=0
j=0
while i<len(left) and j<len(right):
    if left[i]<right[j]:
        result.append(left[i])
        i+=1
    else:
        result.append(right[j])
        j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    print(result)
        
    