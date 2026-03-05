array=[10,9,8,7,6,5,4,3,2,1,0]
left=0
right=len(array)-1
temp=0
while left < right:
        temp=array[left]
        array[left]=array[right]
        array[right]=temp
        left+=1
        right-=1

print("Reversed array is : ", array)