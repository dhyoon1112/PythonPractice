array = [0,1,2,3,4]

def comparison():
    array = [0,1,2,3,4,5]
    user = int(input("Enter a number to see if it's in the array: "))

    while True:
        median = int(len(array)/2)
        #print(array)
        #print(median)

        if user > median:
            array = array[median:]
        elif user < median:
            array = array[:median]

        if len(array) == 1:
            break

    if user in array:
        print('Your number is in the array' + str(array))
    elif user not in array:
        print('Your number is not in the array' + str(array))            

comparison()
