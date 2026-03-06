array = [50,25,100,20,25]
target=50
seen=set()
for number in array:
    needed=target-number
    if needed in seen:
        print("pair found")
        print(needed," and ", number ," are the required numbers!!")
    else:
        seen.add(number)
