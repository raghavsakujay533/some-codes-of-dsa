# arr = [23,44,55,66,77,77]
# arr.append(0)

# for i in range(len(arr)-1,2,-1):
#     arr[i]=arr[i-1]
# arr[2]=24
# print(arr)
        
# for i in range(len(arr)-1,-1,-1):
#     print(arr[i])

##two pointer 

# def find_two_numbers(numbers,target):
#     left = 0
#     right = len(numbers)-1
    
#     while left < right:
#         total = numbers[left]+numbers[right]
        
#         if total == target:
#             return[numbers[left],numbers[right]]
        
#         elif total > target:
#             right = right-1
        
#         else:
#             left = left+1
#     return[]  

# numbers = [1,3,5,6,8,11]
# print(find_two_numbers(numbers,19))   

##two pointer same direction       

# def clean_duplicates(names):
#     left = 0
#     for right in range(1,len(names)):
#         if names[right] != names[left]:
#             left+=1
#             names[left] = names[right]
#     return left + 1
  

# names = ["Anjan","ballu","chirag","chirag","deep","deep","diya"]
# count = clean_duplicates(names)   
# print(names[:count]) 

##    
                

