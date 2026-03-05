array=[-2,-1,10,-23]
largest=array[0]
second_largest=array[0]
for num in array:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
print("Second Largest number is : ",second_largest)
