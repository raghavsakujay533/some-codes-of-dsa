arr=[80,60,50,70,10,30,20,40]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j+1],arr[j]=arr[j],arr[j+1]
        print(arr)


# APPROACH TO PERFORM BUBBLE SORT:
# 1.YOU HAVE GIVEN AN ARRAY IT CAN BE SORTED OR IT CAN BE UNSORTED.
# 2.AT THE SECOND STEP YOU HAVE AN APPROACH OF TWO POINTERS WHERE THE FIRST POINTER WILL START TILL THE END.
# 3.THE J POINTER LOOP WILL RUN AT THE END OF SECOND LAST ELEMENT.
# 4.THERE WILL BE THE J POINTER AND IT WILL WORK AS THE ADJACENT OF EVERY ELEMENT.
# 5.THROUGH WHICH IT WILL CHECK EVERY ELEMENT ADJACENT TO THE NEXT ELEMENT.
# 6.WITH CHECKING THE CONDITIONS OF THE ELEMENT WHETHER IT IS GREATER THEN THE CURRENT ELEMENT.
# 7.AFTER THAT SWAP ACCORDING TO THE GIVEN CONDITION.

# Challenge Faced:
# 

# 1. Understanding why two nested loops are required.
# 2. Figuring out why the inner loop runs only up to (Len(arr)- 1).
# 3. Understanding how the largest element reaches the end after each pass.
# 4. Remembering the correct swap logic.
# 5. Tracing the algorithm pass by pass without getting confused.